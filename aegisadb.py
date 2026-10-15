#!/usr/bin/env python3
"""
PEGASUS SOFTWARE 
============================================================
Developed by Vaishnav Rajeev | Co-developed by Rishabh Gurnani

A terminal-based, ADB-driven toolkit for managing and diagnosing
Android devices from a Kali Linux (or any Linux) workstation.

IMPORTANT / ETHICAL USE NOTICE
-------------------------------
This tool is intended for devices you own, or devices you have
explicit, written authorization to test (e.g. as part of a mobile
security / forensics coursework exercise). Only use it against a
device that is already unlocked for debugging with the owner's
knowledge and consent. Do not use this tool on a device you do not
own or do not have permission to access.

Requirements
------------
- Python 3.8+
- Android platform-tools (adb) on your PATH
    sudo apt install android-tools-adb
- Optional: scrcpy, for the Screen Mirror feature
    sudo apt install scrcpy
- Optional: pyfiglet, for the banner (falls back to plain text)
    pip install pyfiglet
"""

import os
import sys
import time
import json
import shutil
import datetime
import subprocess

try:
    import pyfiglet
    HAVE_FIGLET = True
except ImportError:
    HAVE_FIGLET = False

APP_NAME = "AegisADB"
APP_VERSION = "1.0"
DEVELOPER_LINE = "Developed by Vaishnav Rajeev | Co-developed by Rishabh Gurnani"

HISTORY_FILE = os.path.join(os.path.expanduser("~"), ".aegisadb_history.json")
WORKDIR = os.path.join(os.path.expanduser("~"), "AegisADB_output")


# ------------------------------------------------------------------
# Colors
# ------------------------------------------------------------------
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    ORANGE = "\033[38;5;214m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"


# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------
def ensure_workdir():
    os.makedirs(WORKDIR, exist_ok=True)


def run_adb(args, timeout=30):
    """Run an adb command (args is the list of arguments after 'adb')."""
    cmd = ["adb"] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except FileNotFoundError:
        return -1, "", "adb not found. Install it with: sudo apt install android-tools-adb"
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out."


def log_event(event, detail=""):
    ensure_workdir()
    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event": event,
        "detail": detail,
    }
    history = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
        except (json.JSONDecodeError, IOError):
            history = []
    history.append(entry)
    history = history[-200:]
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)
    except IOError:
        pass


def pause():
    input(f"\n{Color.DIM}Press Enter to return to the menu...{Color.RESET}")


def clear():
    os.system("clear" if os.name != "nt" else "cls")


def colorize_padded(text, width, color):
    """Pad on the plain text length first, then wrap in color codes,
    so ANSI escapes don't throw off column alignment."""
    pad = max(width - len(text), 2)
    return f"{color}{text}{Color.RESET}" + " " * pad


def banner():
    if HAVE_FIGLET:
        text = pyfiglet.figlet_format(APP_NAME, font="big")
    else:
        text = f"{APP_NAME}\n"
    print(f"{Color.CYAN}{Color.BOLD}{text}{Color.RESET}", end="")
    print(f"{Color.CYAN}{APP_NAME} v{APP_VERSION} | {DEVELOPER_LINE}{Color.RESET}")
    print(f"{Color.CYAN}Android Device Management & Diagnostics Toolkit (ADB-based){Color.RESET}")
    print(f"{Color.YELLOW}Use only on devices you own or are explicitly authorized to test.{Color.RESET}")
    print(f"{Color.BLUE}{'-' * 65}{Color.RESET}")


# ------------------------------------------------------------------
# Menu actions
# ------------------------------------------------------------------
def check_device():
    print(f"\n{Color.CYAN}[*] Checking connected devices...{Color.RESET}")
    code, out, err = run_adb(["devices", "-l"])
    if code != 0:
        print(f"{Color.RED}{err}{Color.RESET}")
        return
    print(out)
    lines = [l for l in out.splitlines() if l.strip() and "List of devices" not in l]
    if not lines:
        print(f"{Color.RED}No devices connected.{Color.RESET}")
        return
    _, model, _ = run_adb(["shell", "getprop", "ro.product.model"])
    _, manufacturer, _ = run_adb(["shell", "getprop", "ro.product.manufacturer"])
    _, android_ver, _ = run_adb(["shell", "getprop", "ro.build.version.release"])
    _, battery, _ = run_adb(["shell", "dumpsys", "battery"])
    print(f"\n{Color.GREEN}Manufacturer:{Color.RESET} {manufacturer}")
    print(f"{Color.GREEN}Model:{Color.RESET} {model}")
    print(f"{Color.GREEN}Android Version:{Color.RESET} {android_ver}")
    for line in battery.splitlines():
        if "level" in line.lower():
            print(f"{Color.GREEN}Battery:{Color.RESET} {line.strip()}")
    log_event("check_device", model)


def connect_device():
    print(f"\n{Color.CYAN}[*] Connect a device{Color.RESET}")
    print("  1. USB")
    print("  2. Wireless (IP:PORT)")
    choice = input("Select: ").strip()
    if choice == "2":
        addr = input("Enter device IP:PORT (e.g. 192.168.1.5:5555): ").strip()
        if not addr:
            print(f"{Color.RED}No address entered.{Color.RESET}")
            return
        code, out, err = run_adb(["connect", addr])
        print(out or err)
        log_event("connect_wireless", addr)
    else:
        print(f"{Color.YELLOW}Plug the device in via USB, enable USB debugging, "
              f"and accept the RSA authorization prompt on the phone.{Color.RESET}")
        code, out, err = run_adb(["devices"])
        print(out)
        log_event("connect_usb", out)


def disconnect_device():
    print(f"\n{Color.CYAN}[*] Disconnect device{Color.RESET}")
    addr = input("Enter IP:PORT to disconnect (leave blank to disconnect all): ").strip()
    args = ["disconnect"] + ([addr] if addr else [])
    code, out, err = run_adb(args)
    print(out or err or "Disconnected.")
    log_event("disconnect", addr or "all")


def screen_recording():
    duration = input("Recording duration in seconds (max 180) [10]: ").strip() or "10"
    if not duration.isdigit() or not (1 <= int(duration) <= 180):
        print(f"{Color.RED}Enter a number between 1 and 180.{Color.RESET}")
        return
    remote = "/sdcard/aegisadb_record.mp4"
    ensure_workdir()
    local = os.path.join(WORKDIR, f"screen_record_{int(time.time())}.mp4")
    print(f"{Color.CYAN}[*] Recording for {duration}s...{Color.RESET}")
    code, out, err = run_adb(
        ["shell", "screenrecord", f"--time-limit={duration}", remote],
        timeout=int(duration) + 15,
    )
    if code != 0:
        print(f"{Color.RED}{err}{Color.RESET}")
        return
    code, out, err = run_adb(["pull", remote, local])
    print(out or err)
    run_adb(["shell", "rm", remote])
    if os.path.exists(local):
        print(f"{Color.GREEN}Saved to {local}{Color.RESET}")
    log_event("screen_recording", local)


def screen_mirror():
    if shutil.which("scrcpy") is None:
        print(f"{Color.RED}scrcpy not found.{Color.RESET} Install it with: sudo apt install scrcpy")
        return
    print(f"{Color.CYAN}[*] Launching scrcpy... close its window to return here.{Color.RESET}")
    subprocess.run(["scrcpy"])
    log_event("screen_mirror")


def show_apk_list():
    print(f"\n{Color.CYAN}[*] Installed packages{Color.RESET}")
    mode = input("Show (1) all packages  (2) third-party only [2]: ").strip() or "2"
    args = ["shell", "pm", "list", "packages"]
    if mode == "2":
        args.append("-3")
    code, out, err = run_adb(args)
    print(out or err or "No packages found.")
    log_event("show_apk_list", "all" if mode == "1" else "third-party")


def take_screenshot():
    ensure_workdir()
    local = os.path.join(WORKDIR, f"screenshot_{int(time.time())}.png")
    try:
        with open(local, "wb") as f:
            subprocess.run(["adb", "exec-out", "screencap", "-p"], stdout=f, timeout=20, check=True)
        print(f"{Color.GREEN}Saved to {local}{Color.RESET}")
        log_event("screenshot", local)
    except FileNotFoundError:
        print(f"{Color.RED}adb not found.{Color.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Color.RED}Screenshot failed (exit code {e.returncode}).{Color.RESET}")
    except subprocess.TimeoutExpired:
        print(f"{Color.RED}Timed out.{Color.RESET}")


def power_off():
    confirm = input(f"{Color.RED}This will power off the connected device. Continue? (y/N): {Color.RESET}").strip().lower()
    if confirm == "y":
        code, out, err = run_adb(["shell", "reboot", "-p"])
        print(out or err or "Power-off command sent.")
        log_event("power_off")


def install_apk():
    path = input("Path to .apk file: ").strip().strip('"')
    if not os.path.isfile(path):
        print(f"{Color.RED}File not found.{Color.RESET}")
        return
    code, out, err = run_adb(["install", "-r", path], timeout=90)
    print(out or err)
    log_event("install_apk", path)


def delete_apk():
    pkg = input("Package name to uninstall (e.g. com.example.app): ").strip()
    if not pkg:
        return
    confirm = input(f"Uninstall {pkg}? (y/N): ").strip().lower()
    if confirm == "y":
        code, out, err = run_adb(["uninstall", pkg])
        print(out or err)
        log_event("delete_apk", pkg)


def pull_file():
    remote = input("Remote path on device: ").strip()
    if not remote:
        return
    ensure_workdir()
    local = input(f"Local destination [{WORKDIR}]: ").strip() or WORKDIR
    code, out, err = run_adb(["pull", remote, local], timeout=90)
    print(out or err)
    log_event("pull_file", f"{remote} -> {local}")


def push_file():
    local = input("Local file path: ").strip().strip('"')
    if not os.path.isfile(local):
        print(f"{Color.RED}File not found.{Color.RESET}")
        return
    remote = input("Remote destination on device (e.g. /sdcard/): ").strip()
    if not remote:
        return
    code, out, err = run_adb(["push", local, remote], timeout=90)
    print(out or err)
    log_event("push_file", f"{local} -> {remote}")


def reboot_device():
    confirm = input("Reboot the device? (y/N): ").strip().lower()
    if confirm == "y":
        code, out, err = run_adb(["reboot"])
        print(out or err or "Reboot command sent.")
        log_event("reboot")


def start_app():
    pkg = input("Package name to launch (e.g. com.android.settings): ").strip()
    if not pkg:
        return
    code, out, err = run_adb(["shell", "monkey", "-p", pkg, "-c", "android.intent.category.LAUNCHER", "1"])
    print(out or err)
    log_event("start_app", pkg)


def get_device_logs():
    ensure_workdir()
    local = os.path.join(WORKDIR, f"logcat_{int(time.time())}.txt")
    print(f"{Color.CYAN}[*] Dumping current log buffer...{Color.RESET}")
    code, out, err = run_adb(["logcat", "-d"], timeout=30)
    if code != 0:
        print(f"{Color.RED}{err}{Color.RESET}")
        return
    with open(local, "w") as f:
        f.write(out)
    print(f"{Color.GREEN}Saved to {local} ({len(out.splitlines())} lines){Color.RESET}")
    log_event("get_logs", local)


def toggle_wifi():
    state = input("Turn Wi-Fi (1) ON or (2) OFF: ").strip()
    if state not in ("1", "2"):
        print(f"{Color.RED}Invalid choice.{Color.RESET}")
        return
    arg = "enable" if state == "1" else "disable"
    code, out, err = run_adb(["shell", "svc", "wifi", arg])
    print(out or err or f"Wi-Fi {arg} command sent.")
    log_event("toggle_wifi", arg)


def check_storage():
    code, out, err = run_adb(["shell", "df", "/data"])
    print(out or err)
    log_event("check_storage")


def troubleshoot_connection():
    print(f"\n{Color.CYAN}[*] Running diagnostics...{Color.RESET}")
    adb_path = shutil.which("adb")
    code, out, err = run_adb(["devices"])
    checks = [
        ("adb installed on PATH", bool(adb_path)),
        ("adb server responding", code == 0),
        ("at least one device listed", "device" in out.replace("List of devices attached", "")),
    ]
    for name, ok in checks:
        status = f"{Color.GREEN}OK{Color.RESET}" if ok else f"{Color.RED}FAIL{Color.RESET}"
        print(f"  [{status}] {name}")
    retry = input("\nRestart the adb server? (y/N): ").strip().lower()
    if retry == "y":
        run_adb(["kill-server"])
        run_adb(["start-server"])
        code, out, err = run_adb(["devices"])
        print(out)
    log_event("troubleshoot")


def view_history():
    if not os.path.exists(HISTORY_FILE):
        print(f"{Color.YELLOW}No connection history yet.{Color.RESET}")
        return
    with open(HISTORY_FILE, "r") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            history = []
    if not history:
        print(f"{Color.YELLOW}No connection history yet.{Color.RESET}")
        return
    print(f"\n{Color.CYAN}Recent activity (most recent last):{Color.RESET}")
    for entry in history[-20:]:
        print(f"  {Color.DIM}{entry['timestamp']}{Color.RESET}  "
              f"{Color.ORANGE}{entry['event']}{Color.RESET}  {entry.get('detail', '')}")


# ------------------------------------------------------------------
# Menu
# ------------------------------------------------------------------
MENU_ITEMS = [
    ("1", "Check Device", check_device),
    ("2", "Connect a Device", connect_device),
    ("3", "Disconnect Device", disconnect_device),
    ("4", "Screen Recording", screen_recording),
    ("5", "Screen Mirror", screen_mirror),
    ("6", "Show APK List", show_apk_list),
    ("7", "Take Screenshot", take_screenshot),
    ("8", "Power Off", power_off),
    ("9", "Install APK", install_apk),
    ("10", "Delete APK", delete_apk),
    ("11", "Pull File", pull_file),
    ("12", "Push File", push_file),
    ("13", "Reboot Device", reboot_device),
    ("14", "Start App", start_app),
    ("15", "Get Device Logs", get_device_logs),
    ("16", "Toggle Wi-Fi", toggle_wifi),
    ("17", "Check Storage", check_storage),
    ("18", "Troubleshoot Connection", troubleshoot_connection),
    ("19", "View Connection History", view_history),
]


def print_menu():
    print()
    for i in range(0, len(MENU_ITEMS), 3):
        row = MENU_ITEMS[i:i + 3]
        line = ""
        for num, label, _ in row:
            plain = f"[{num}] {label}"
            line += colorize_padded(plain, 26, Color.ORANGE)
        print(line)
    print(f"\n{Color.GREEN}[q] Quit{Color.RESET}")
    print(f"{Color.BLUE}{'-' * 65}{Color.RESET}")


def main():
    actions = {num: fn for num, _, fn in MENU_ITEMS}
    while True:
        clear()
        banner()
        print_menu()
        choice = input(f"\n{Color.GREEN}Select an option (1-19) or q to quit: {Color.RESET}").strip().lower()
        if choice == "q":
            print(f"{Color.CYAN}Goodbye.{Color.RESET}")
            break
        fn = actions.get(choice)
        if fn is None:
            print(f"{Color.RED}Invalid option.{Color.RESET}")
            pause()
            continue
        try:
            fn()
        except KeyboardInterrupt:
            print(f"\n{Color.YELLOW}Cancelled.{Color.RESET}")
        except Exception as e:
            print(f"{Color.RED}Error: {e}{Color.RESET}")
        pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Color.CYAN}Goodbye.{Color.RESET}")
        sys.exit(0)
