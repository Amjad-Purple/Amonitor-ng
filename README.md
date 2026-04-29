# Amonitor-ng 🛡️

> **Next-Generation Network Defense Tool** — Real-time threat detection for WiFi and local networks

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Amjad-Purple/Amonitor-ng/graphs/commit-activity)
[![Made with 💜 by a 13-year-old Moroccan Developer](https://img.shields.io/badge/Made%20with%20%F0%9F%92%9C%20by%20a%2013--year--old-Moroccan%20Developer-purple.svg)](https://github.com/Amjad-Purple)

---

## 👨‍💻 About This Project

**Amonitor-ng** is a powerful, multithreaded network monitoring and defense tool created by **Amjad**, a 13-year-old Moroccan cybersecurity enthusiast and developer. This project demonstrates exceptional passion for cybersecurity at a young age and serves as a testament to what young talent can achieve with dedication and curiosity.

---

## 🎯 Overview

Built with **Python** and **Scapy**, Amonitor-ng provides real-time detection and analysis of malicious network activities on WiFi and local networks.

Perfect for **Purple Team operations**, network security audits, and cybersecurity education across Morocco and beyond.

---

## ✨ Key Features

### 🔍 **Advanced Threat Detection**
- **ARP Spoofing Detection** — Identifies Man-in-the-Middle (MITM) attacks
- **Deauthentication Attack Monitoring** — Detects WiFi disconnection attacks
- **TCP/TLS Traffic Analysis** — Deep inspection of encrypted and unencrypted traffic
- **DNS Monitoring** — Analyzes DNS queries for suspicious activity

### ⚡ **Performance & Scalability**
- **Multithreaded Packet Sniffing** — Non-blocking, high-performance packet capture
- **Real-time Processing** — Instant threat alerts and notifications
- **Lightweight Design** — Minimal resource consumption

### 🎮 **User-Friendly Interface**
- **CLI-Based Tool** — Simple yet powerful command-line interface
- **Intuitive Output** — Clear, actionable threat reports
- **Educational Focus** — Designed with learning in mind

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Linux/Unix-based system (macOS, Ubuntu, Kali, etc.)
- Root or administrator privileges (for packet sniffing)
- Scapy library

### Installation

```bash
# Clone the repository
git clone https://github.com/Amjad-Purple/Amonitor-ng.git
cd Amonitor-ng

# Install dependencies
pip install -r requirements.txt

# Or install Scapy directly
pip install scapy
```

### Basic Usage

```bash
# Run with root privileges
sudo python amonitor-ng.py

# Monitor specific interface
sudo python amonitor-ng.py --interface wlan0

# Enable verbose output
sudo python amonitor-ng.py --verbose
```

---

## 📋 Features in Detail

### 1. **ARP Spoofing Detection**
Continuously monitors ARP traffic to identify:
- Suspicious MAC address changes
- Gratuitous ARP packets
- Potential Man-in-the-Middle attacks

### 2. **Deauthentication Attack Detection**
Detects WiFi deauth floods and rogue access points attempting to:
- Disconnect clients from networks
- Force downgrade attacks
- Create denial-of-service conditions

### 3. **DNS Analysis**
Monitors DNS queries for:
- Unusual query patterns
- Domain reputation checks
- DNS spoofing attempts

### 4. **TCP/TLS Inspection**
Analyzes network connections for:
- Suspicious port usage
- Certificate anomalies
- Encrypted traffic patterns

---

## 🏗️ Architecture

```
Amonitor-ng/
├── amonitor-ng.py          # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── docs/                  # Documentation & guides
```

---

## 🔐 Security & Privacy

- **No Data Retention** — Packets are analyzed in real-time and not stored
- **GPL v3 Licensed** — Free, open-source software
- **Privacy-Focused** — Designed for network monitoring on your own networks only
- **Ethical Use** — Educational and authorized security testing only

⚠️ **Disclaimer:** This tool is intended for educational purposes and authorized security testing only. Unauthorized network monitoring is illegal in many jurisdictions.

---

## 📚 Use Cases

✅ **Cybersecurity Education** — Learn network security fundamentals  
✅ **Penetration Testing** — Conduct authorized security assessments  
✅ **Network Security Audits** — Identify vulnerabilities in your infrastructure  
✅ **Purple Team Operations** — Simulate both attack and defense scenarios  
✅ **Purple Teaming in Morocco** — Build local security communities  

---

## 🛠️ Configuration

Create a `config.ini` file for custom settings:

```ini
[monitoring]
interface = wlan0
timeout = 60
verbose = true
alert_level = high

[threats]
detect_arp_spoofing = true
detect_deauth = true
detect_dns_anomalies = true
```

---

## 📊 Output Example

```
[+] Amonitor-ng Network Defense Tool Started
[*] Monitoring interface: wlan0
[*] Starting packet capture...

[!] THREAT DETECTED: ARP Spoofing
    Source IP: 192.168.1.50
    Target IP: 192.168.1.1
    Timestamp: 2026-04-29 18:30:45

[!] ALERT: Deauthentication Attack
    Target BSSID: AA:BB:CC:DD:EE:FF
    Reason Code: 2
    Count: 8

[*] Real-time monitoring active...
```

---

## 🤝 Contributing

Contributions are welcome! Help us improve Amonitor-ng:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.

---

## ⚡ Performance Tips

- Run with the `-v` (verbose) flag for detailed logging
- Use specific interface names for better performance
- Monitor during peak network hours for comprehensive analysis
- Combine with external tools for extended threat intelligence

---

## 🐛 Troubleshooting

**Permission Denied Error**
```bash
sudo python amonitor-ng.py
```

**Interface Not Found**
```bash
# List available interfaces
sudo python -m scapy.all
```

**Dependency Issues**
```bash
pip install --upgrade scapy
```

---

## 📞 Support & Community

- **Issues & Bugs** — [GitHub Issues](https://github.com/Amjad-Purple/Amonitor-ng/issues)
- **Discussions** — [GitHub Discussions](https://github.com/Amjad-Purple/Amonitor-ng/discussions)
- **Security Reporting** — Please report security vulnerabilities responsibly

---

## 🎓 Educational Resources

Learn more about network security:
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [ARP Spoofing Explained](https://www.cloudflare.com/learning/ddos/arp-spoofing/)
- [WiFi Security Best Practices](https://www.wireshark.org/docs/)

---

## 🌟 Roadmap

- [ ] Web dashboard interface
- [ ] Machine learning-based threat detection
- [ ] Automated threat response module
- [ ] Integration with SIEM systems
- [ ] Mobile app companion
- [ ] Cloud-based threat intelligence

---

## 👨‍💼 Author

**Amjad-Purple** — 13-year-old Moroccan Cybersecurity Enthusiast & Developer

*Inspiring young minds in Morocco to pursue cybersecurity excellence*

---

## ⭐ Show Your Support

If Amonitor-ng helps you, please give us a ⭐ on GitHub and share with your network!

---

**Made with 💜 by a young Moroccan developer**

*Amonitor-ng — Defend Your Network. Monitor Your Assets. Secure Your Future.*
