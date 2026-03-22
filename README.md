# 🎭 **Ephish – AI-Powered Phishing Page Generator**

### *Educational Security Awareness Tool*

<div align="center">
  <img src="https://iili.io/qEHckKv.webp" alt="Ephish Logo" width="250"/>
  
  [![Telegram](https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/ERROR0101risback)
  [![Instagram](https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=for-the-badge&logo=instagram)](https://instagram.com/fahad0101r)
  [![GitHub](https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=for-the-badge&logo=github)](https://github.com/ERROR0101r)
  [![Telegram Channel](https://img.shields.io/badge/Channel-@aab_ho_ga_comeback-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/aab_ho_ga_comeback)
  
  <p><strong>Developer: @ERROR0101risback</strong></p>
  <p><em>Version: 1.0 (Beta)</em></p>
</div>

---

## 📋 **TABLE OF CONTENTS**
- [📌 What is Ephish?](#-what-is-ephish)
- [⚠️ Important – Educational Only](#️-important--educational-only)
- [🧪 Beta Notice](#-beta-notice)
- [✨ Features](#-features)
- [🚀 Quick Setup](#-quick-setup)
- [💻 Usage – Quick Commands](#-usage--quick-commands)
- [📁 Log Files](#-log-files)
- [🔧 Setup (Termux / Linux)](#-setup-termux--linux)
- [📢 Developer Contact](#-developer-contact)
- [🔗 Repository](#-repository)
- [📄 License](#-license)

---

## 📌 **WHAT IS EPHISH?**

**Ephish** is an AI‑powered phishing page generator built for **educational and awareness purposes only**.

It automatically creates realistic login pages for any brand using AI to fetch:

| Component | How it's Generated |
|-----------|-------------------|
| **Logo** | Live image API |
| **Brand Colors** | AI analysis of the real website |
| **Login Fields** | Dynamically generated based on brand's actual login flow |
| **Welcome Text** | AI-generated |
| **Footer Text** | AI-generated |
| **Button Labels** | AI-generated |

The tool is designed to help **security professionals, educators, and ethical hackers** understand how phishing pages are constructed and how to recognize them.

---

## ⚠️ **IMPORTANT – EDUCATIONAL ONLY**

```
THIS TOOL IS STRICTLY FOR EDUCATIONAL USE ONLY.

By using this tool, you agree to:
- Use only on systems you own or have explicit written permission to test
- Take full responsibility for your actions
- Not use for illegal activities

Misuse of this tool for phishing, credential theft, or any illegal activity 
is not supported and may violate laws in your jurisdiction.

The author (@ERROR0101risback) does not condone any illegal activities.
```

---

## 🧪 **BETA NOTICE**

This is the **first public version (v1.0 Beta)** – a "virgin" release.

- ⚠️ Not fully completed – currently in beta testing
- 🐛 You may encounter bugs, missing features, or unexpected behavior
- 📢 If you find any issues or have suggestions, please message me directly or open an issue on GitHub

**Your feedback will help make the next version better!**

---

## ✨ **FEATURES**

| Feature | Description |
|---------|-------------|
| **AI-Powered Generation** | Automatically fetches logo, colors, and fields for any brand |
| **Realistic Pages** | Creates convincing login pages that mimic real brands |
| **Local Server** | Built-in web server for testing |
| **Credential Capture** | Logs entered credentials for analysis |
| **Color Detection** | AI analyzes real website to extract brand colors |
| **Dynamic Fields** | Generates appropriate login fields (email, mobile, password, OTP) |
| **Easy Setup** | One-command installation |

---

## 🚀 **QUICK SETUP**

### **One Command Setup:**
```bash
git clone https://github.com/ERROR0101r/Ephish.git
cd Ephish
chmod +x setup.sh
./setup.sh
```

### **Termux (Android):**
```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/ERROR0101r/Ephish.git
cd Ephish
chmod +x setup.sh
./setup.sh
```

### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/ERROR0101r/Ephish.git
cd Ephish
chmod +x setup.sh
./setup.sh
```

### **Windows:**
```bash
git clone https://github.com/ERROR0101r/Ephish.git
cd Ephish
pip install flask requests colorama
python Ephish.py
```

---

## 💻 **USAGE – QUICK COMMANDS**

| Command | Description |
|---------|-------------|
| `python Ephish.py` | Run the tool |
| `/r` | Run the phishing page (starts local web server) |
| `/q` | Quit the tool |

### **Step‑by‑step inside the tool:**

1. Enter a brand name (e.g., `Flipkart`, `Amazon`, `Paytm`)
2. The AI will automatically fetch:
   - Logo
   - Brand colors
   - Login fields (email, mobile, password, OTP, etc.)
   - Welcome message
   - Footer text
   - Button label
3. After page generation, type `/r` to start the local server
4. Share the generated network link with your target **(for authorized testing only)**
5. Credentials entered on the fake page will be shown in the terminal and saved to a log file

---

## 📁 **LOG FILES**

All captured credentials are saved automatically as:

```
phish_log_YYYYMMDD_HHMMSS.txt
```

Each entry includes:

| Field | Description |
|-------|-------------|
| Brand name | Target brand |
| Field values | Email, password, mobile, OTP, etc. |
| Timestamp | Date and time of capture |

---

## 🔧 **SETUP (TERMUX / LINUX)**

### **Automatic Setup:**
```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- ✅ Install Python (if missing)
- ✅ Install required packages (`flask`, `requests`, `colorama`)
- ✅ Ask if you want to run the tool immediately

### **Manual Setup:**
```bash
pip install flask requests colorama
python Ephish.py
```

---

## 📁 **FILE STRUCTURE**

```
Ephish/
│
├── Ephish.py            # Main tool
├── setup.sh             # Auto-installer script
├── templates/           # Generated HTML templates
├── static/              # Static files (CSS, images)
└── phish_log_*.txt      # Captured credentials logs
```

---

## 👨‍💻 **ABOUT THE DEVELOPER**

<div align="center">
  <table>
    <tr>
      <td align="right"><strong>Name:</strong>    </td>
      <td><code>ERROR0101risback / Fahad</code></td>
    </tr>
     <tr>
      <td align="right"><strong>Telegram:</strong>    </td>
      <td><a href="https://t.me/ERROR0101risback">@ERROR0101risback</a></td>
     </tr>
     <tr>
      <td align="right"><strong>Instagram:</strong>    </td>
      <td><a href="https://instagram.com/fahad0101r">@fahad0101r</a></td>
     </tr>
     <tr>
      <td align="right"><strong>Telegram Channel:</strong>    </td>
      <td><a href="https://t.me/aab_ho_ga_comeback">@aab_ho_ga_comeback</a></td>
     </tr>
     <tr>
      <td align="right"><strong>GitHub Profile:</strong>    </td>
      <td><a href="https://github.com/ERROR0101r">ERROR0101r</a></td>
     </tr>
     <tr>
      <td align="right"><strong>Project Repo:</strong>    </td>
      <td><a href="https://github.com/ERROR0101r/Ephish">Ephish</a></td>
     </tr>
   </table>
</div>

---

## ⭐ **SUPPORT THE PROJECT**

If you find Ephish useful for educational purposes:
- ⭐ **Star** the repository on [GitHub](https://github.com/ERROR0101r/Ephish)
- 📢 **Share** with security enthusiasts
- 📝 **Join** the [Telegram Channel](https://t.me/aab_ho_ga_comeback)
- 👤 **Follow** on [Instagram](https://instagram.com/fahad0101r)
- 🐛 **Report bugs** to help improve the tool

---

## 📥 **DIRECT DOWNLOAD**

**Download ZIP:**
```
https://github.com/ERROR0101r/Ephish/archive/refs/heads/main.zip
```

---

## 📄 **LICENSE**

```
This project is for educational purposes only.
No license is granted for commercial or malicious use.
Use at your own risk.

You are free to:
- Use for security awareness training
- Modify for personal educational use
- Share with other security professionals

You are NOT permitted to:
- Use for actual phishing attacks
- Use to steal credentials
- Distribute as a malicious tool
```

---

<div align="center">
  <h3>🎭 Learn. Understand. Protect. 🎭</h3>
  <p><i>Made with 🔥 by @ERROR0101risback</i></p>
  
  <p>
    <a href="https://t.me/ERROR0101risback"><img src="https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=flat-square&logo=telegram" alt="Telegram"></a>
    <a href="https://instagram.com/fahad0101r"><img src="https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=flat-square&logo=instagram" alt="Instagram"></a>
    <a href="https://github.com/ERROR0101r"><img src="https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=flat-square&logo=github" alt="GitHub"></a>
    <a href="https://t.me/aab_ho_ga_comeback"><img src="https://img.shields.io/badge/Channel-@aab_ho_ga_comeback-2CA5E0?style=flat-square&logo=telegram" alt="Channel"></a>
    <a href="https://github.com/ERROR0101r/Ephish/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Download-ZIP-brightgreen?style=flat-square&logo=github" alt="Download"></a>
  </p>
  
  <p>© 2026 Ephish. All rights reserved.</p>
  <p><strong>Version 1.0 Beta</strong></p>
</div>