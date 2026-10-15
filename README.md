<div align="center">

# 👁️ GOD'S EYE

**OSINT • Exploitation • Anonymity • Device Control • Recon**

*"The eye that sees everything, but is seen by no one."*

**Developed by VAISHNAV**

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20Kali-557C94?style=for-the-badge&logo=linux&logoColor=white)
![ADB](https://img.shields.io/badge/Requires-ADB-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Tor](https://img.shields.io/badge/Anonymity-Tor-7D4698?style=for-the-badge&logo=tor-browser&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-ACTIVE-brightgreen?style=for-the-badge)

> ⚠️ **For Educational & Authorized Testing Only.**  
> Use only on devices and networks you own or have explicit written permission to test.

</div>

---

## 🕶️ What is God's Eye?

**God's Eye** is a unified offensive-security framework that consolidates **reconnaissance, exploitation, post-exploitation, phishing, IoT hardware hacking, and network anonymity** into a single color-coded interactive CLI.

Two flagship modules are wired in:

- 🦅 **PEGASUS v1.3** — Android Device Management & Security Audit over ADB
- 🔁 **IPHOPPR** — Multi-node Tor IP rotation engine

Everything else (nmap, sqlmap, hydra, aircrack-ng, theHarvester, and more) is orchestrated from the same menu.

---

## 📖 Table of Contents

- [Feature Matrix](#-feature-matrix)
- [Menu Structure](#-menu-structure)
- [PEGASUS Module](#-pegasus-module)
- [IPHOPPR Module](#-iphoppr-module)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Output Files](#-output-files)
- [Legal Notice](#️-legal-notice)
- [Credits](#-credits)

---

## ⚡ Feature Matrix

| Category | Module | Status |
|---|---|---|
| Host OSINT | theHarvester, Sherlock, phoneinfoga | ✅ |
| DNS Recon | dnsrecon, dnsenum, fierce | ✅ |
| Web Scan | whatweb, wafw00f, nikto | ✅ |
| Web Vuln | sqlmap, XSStrike, wpscan, nuclei | ✅ |
| Wireless Audit | aircrack-ng, wifite, reaver | ✅ |
| Exploitation | Metasploit, searchsploit | ✅ |
| Post-Exploit / Pivot | responder, bettercap, chisel | ✅ |
| Phishing / Social Eng | zphisher, setoolkit | ✅ |
| IoT & Hardware | adb, fastboot, hardware probes | ✅ |
| Audio Surveillance (PoC) | ADB-based mic capture | ✅ |
| **Android Device Control** | **PEGASUS v1.3** | ✅ |
| **Tor IP Rotation** | **IPHOPPR** | ✅ |
| Network Anonymity | MAC changer, IP changer, **GOD'S FIX** | ✅ |

---

## 🗺️ Menu Structure

```
╔══════════════════════════════════════════════════════════════════╗
║                    G O D ' S   E Y E                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   [ RECONNAISSANCE ]                                             ║
║   [1] Host OSINT      [2] DNS Recon      [3] Web Scan           ║
║   [4] Web Vuln        [5] Wireless Audit                         ║
║                                                                  ║
║   [ EXPLOITATION / POST-EXPLOIT ]                                ║
║   [6] Exploitation    [7] Post-Exploit   [8] Phishing            ║
║                                                                  ║
║   [ IoT / AUDIO / DEVICE ]                                       ║
║   [9] IoT & Hardware  [10] Audio Surveillance                    ║
║   [11] PEGASUS (Android Control Suite)                           ║
║                                                                  ║
║   [ ANONYMITY ]                                                  ║
║   [12] IPHOPPR (Tor IP Rotation)                                 ║
║   [13] GOD'S FIX (Rollback MAC / IP)                             ║
║                                                                  ║
║   [0] Exit                                                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 🦅 PEGASUS Module

> Android Device Management & Security Audit over ADB — **no app required on the target device.**

### 📱 Device Management

| # | Feature | Description |
|---|---|---|
| 1 | Check Device | Model, Android version, battery |
| 2 | Connect Device | USB or wireless ADB (TCP/IP) |
| 3 | Disconnect Device | Clean wireless teardown |
| 4 | Screen Recording | Record + auto-pull to PC |
| 5 | Screen Mirror | Live via `scrcpy` |
| 6 | Show APK List | Export clean package list |
| 7 | Take Screenshot | Instant capture + pull |
| 8 | Power Off | Remote shutdown |
| 15 | Reboot Device | Remote reboot |
| 18 | Toggle Wi-Fi | Enable/disable remotely |
| 19 | Check Storage | Human-readable `df -h` |
| 20 | Take Photo | Camera trigger + auto-pull |
| 21 | Troubleshoot | Kill/restart ADB server |
| 23 | Connection History | Session log with timestamps |

### 📦 App Management

| # | Feature | Description |
|---|---|---|
| 9 | Install APK | Sideload from PC |
| 10 | Delete APK | Uninstall by package name |
| 16 | Start App | Launch package remotely |

### 📂 File Transfer

| # | Feature | Description |
|---|---|---|
| 11 | Pull File | Device → PC |
| 12 | Push File | PC → Device |

### 🗂️ Data & Logs

| # | Feature | Description |
|---|---|---|
| 13 | Send SMS | Pre-filled intent dispatch |
| 14 | Dump Contacts | Name + Number → `.txt` |
| 17 | Get Device Logs | Full `logcat` dump |

### 🔐 Advanced Security Audit *(Option 22)*

| Sub | Feature |
|---|---|
| 1 | Root Detection (multi-method) |
| 2 | APK Permissions Dump |
| 3 | Device Security Audit (patch level, encryption, build tags) |
| 4 | Debuggable Apps Scanner |
| 5 | Interactive ADB Shell |
| 6 | Network Security Check (+ optional nmap) |
| 7 | Dump SMS / Call Logs |
| 8 | Security Log Filter |
| 9 | Vulnerability Scanner (patch-date threshold) |
| 10 | Network Connections Monitor (`netstat`) |

---

## 🔁 IPHOPPR Module

> **Multi-node Tor IP rotation engine for anonymous operations.**

### 🎯 What it does

Launches **5 Tor nodes in parallel**, routes all traffic through a centralized **Privoxy** proxy, and rotates your public exit IP on a custom interval using `SIGNAL NEWNYM`.

### 🔥 Features

- 🔁 Auto IP rotation via Tor
- 🧠 **5 simultaneous Tor nodes** for load distribution
- 🔒 All traffic funneled through Privoxy
- 🧱 **No root required** — runs fine in Termux
- ⏱️ Custom rotation timer (seconds)
- 🧰 Self-contained config — clean reinit each run
- 💻 Termux + Linux compatible
- 🌐 Live public IP display via `api64.ipify.org`

### ⚙️ How it works

```
  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ Tor #1   │   │ Tor #2   │   │ Tor #3   │   │ Tor #4   │   │ Tor #5   │
  │ :9050    │   │ :9051    │   │ :9052    │   │ :9053    │   │ :9054    │
  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
       │              │              │              │              │
       └──────────────┴──────┬───────┴──────────────┴──────────────┘
                             │
                      ┌──────▼──────┐
                      │  PRIVOXY    │  :8118
                      │  (proxy)    │
                      └──────┬──────┘
                             │
                    ┌────────▼────────┐
                    │  YOUR TERMINAL  │
                    │  curl / browser │
                    └─────────────────┘

  Rotation Loop → SIGNAL NEWNYM → all 5 control ports
```

---

## 🧩 Requirements

| Dependency | Required | Purpose |
|---|---|---|
| Python 3.7+ | ✅ Yes | Run the framework |
| colorama | ✅ Yes | ANSI color output |
| ADB | ✅ Yes | Android communication (PEGASUS) |
| Tor | ✅ Yes | Anonymity (IPHOPPR) |
| Privoxy | ✅ Yes | Proxy frontend (IPHOPPR) |
| scrcpy | ⚠️ Optional | Screen mirror |
| nmap | ⚠️ Optional | Network scans |
| git | ✅ Recommended | Clone repo |

---

## 🚀 Installation

### 🐧 Kali / Debian / Ubuntu

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip adb scrcpy nmap git tor privoxy
git clone https://github.com/YOUR-USERNAME/GODS-EYE.git
cd GODS-EYE
pip3 install -r requirements.txt
python3 godseye.py
```

### 📱 Termux (One-Shot)

```bash
pkg update && pkg upgrade -y
pkg install -y python git android-tools tor privoxy nmap
git clone https://github.com/YOUR-USERNAME/GODS-EYE.git
cd GODS-EYE
pip install -r requirements.txt
python godseye.py
```

### 🏴‍☠️ Arch / BlackArch

```bash
sudo pacman -Syu
sudo pacman -S python android-tools scrcpy nmap git tor privoxy
git clone https://github.com/YOUR-USERNAME/GODS-EYE.git
cd GODS-EYE
pip install -r requirements.txt
python3 godseye.py
```

### 🍎 macOS

```bash
brew install python android-platform-tools scrcpy nmap tor privoxy git
git clone https://github.com/YOUR-USERNAME/GODS-EYE.git
cd GODS-EYE
pip3 install -r requirements.txt
python3 godseye.py
```

---

## 🎮 Usage

```bash
python3 godseye.py
```

**Standalone modules:**

```bash
python3 pegasus_v_1.3.py      # Android suite only
bash iphopper.sh              # Tor rotation only
```

### 📱 Phone Setup (one-time, for PEGASUS)

```
Settings → About Phone
→ Tap "Build Number" 7×
→ Developer Options ON
→ USB Debugging ON
→ Connect phone → "Allow" popup
```

### 📡 Switch to Wireless ADB

```bash
adb tcpip 5555
# unplug USB
adb connect <PHONE_IP>:5555
```

Then in God's Eye: `[11] PEGASUS → [2] Connect a Device`

---

## 📁 Output Files

| File | Produced By |
|---|---|
| `screen.png` | PEGASUS — Screenshot |
| `record.mp4` | PEGASUS — Screen Recording |
| `apk_list.txt` | PEGASUS — APK List |
| `contacts.txt` | PEGASUS — Contact Dump |
| `device_log.txt` | PEGASUS — Logcat Dump |
| `storage_info.txt` | PEGASUS — Storage Check |
| `sms_logs.txt` | PEGASUS — SMS Dump |
| `call_logs.txt` | PEGASUS — Call Logs |
| `connection_log.txt` | PEGASUS — Session History |
| `godseye.log` | God's Eye — Global log |

---

## ⚖️ Legal Notice

```
  This software is provided for EDUCATIONAL and AUTHORIZED
  SECURITY TESTING purposes ONLY.

  ✔  Use only on devices you own, or on networks you have
     explicit written permission to test.
  ✘  Unauthorized access, surveillance, or interception is
     a criminal offense under:

        • Information Technology Act, 2000 (India)
        • Computer Fraud and Abuse Act (USA)
        • Computer Misuse Act 1990 (UK)
        • Equivalent legislation worldwide

  The author assumes ZERO liability for misuse. You are
  solely responsible for your actions.
```

**IPHOPPR disclaimer:** Tor does **not** guarantee full anonymity — DNS leaks, misconfigurations, and operator mistakes can expose identity.

**PEGASUS disclaimer:** All data-extraction features (contacts, SMS, call logs, camera) are intended strictly for **personal backup** and **security audit on your own device**.

---

## 👤 Credits

| Role | Name |
|---|---|
| 🎨 Framework Author | **VAISHNAV** |
| 🦅 PEGASUS Author | **Alok Thakur** ([@thakur2309](https://github.com/thakur2309)) |
| 🔁 IPHOPPR Author | **Alok Thakur** ([@thakur2309](https://github.com/thakur2309)) |
| 📺 YouTube | [Firewall Breaker](https://www.youtube.com/@FirewallBreaker09) |
| 💬 WhatsApp Channel | [Join](https://whatsapp.com/channel/0029VbAiqVMKLaHjg5J1Nm2F) |
| 📸 Instagram | [@sudo_xploit](https://www.instagram.com/sudo_xploit) |

---

## 📜 License

MIT — see [`LICENSE`](./LICENSE).

---

<div align="center">

```
   ▄████▄   ▒█████  ▓█████▄      ██████  ▓█████▓██   ██▓▓█████ 
  ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌   ▒██    ▒  ▓█   ▀ ▒██  ██▒▓█   ▀ 
  ▒▓█    ▄ ▒██░  ██▒░██   █▌   ░ ▓██▄    ▒███    ▒██ ██░▒███   
  ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌     ▒   ██▒▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ 
  ▒ ▓███▀ ░░ ████▓▒░░▒████▓    ▒██████▒▒░▒████▒ ░ ██▒▓░░▒████▒
  ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
    ░  ▒     ░ ▒ ▒░  ░ ▒  ▒    ░ ░▒  ░ ░ ░ ░  ░▓██ ░▒░  ░ ░  ░
  ░        ░ ░ ░ ▒   ░ ░  ░    ░  ░  ░     ░   ▒ ▒ ░░     ░   
  ░ ░          ░ ░     ░             ░     ░  ░░ ░        ░  ░
  ░                  ░                       ░  ░             
```

**⭐ If this project helped you, star the repo. It fuels the next release.**

</div>
