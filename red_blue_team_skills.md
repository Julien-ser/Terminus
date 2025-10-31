# Red and Blue Team Skills

This document provides a summary of essential skills for both Red and Blue teams in cybersecurity, with references to the Not The Hidden Wiki (NTHW) repository for further learning.

## Red Team Skills (Offensive Security)

Red teams simulate attacks to identify vulnerabilities. Key skills include:

*   **Penetration Testing:** Proficiency in testing networks, web applications, and mobile applications to find and exploit vulnerabilities. The NTHW repository has extensive resources in the `Red Team/Web Hacking` and `Red Team/Mobile` sections.
*   **Social Engineering:** The ability to manipulate individuals to gain unauthorized access. This includes phishing, smishing, and other tactics.
*   **Malware Analysis and Reverse Engineering:** Understanding how to analyze and reverse engineer malware to understand its functionality and exploit vulnerabilities. The `Red Team/Malware` and `Blue Team/Reverse Engineering` sections in the NTHW repository are relevant here.
*   **Evasion Techniques:** Bypassing security controls like firewalls, Intrusion Detection Systems (IDS), and antivirus software.
*   **Open-Source Intelligence (OSINT):** Gathering information from publicly available sources to support attack simulations. The `Red Team/OSINT` section in the NTHW repository is a great starting point.
*   **Scripting and Programming:** Writing scripts and tools to automate tasks and develop custom payloads. Python and PowerShell are common languages for this.
*   **Active Directory Exploitation:** Attacking and compromising Active Directory environments. The `Red Team/Active Directory` section in the NTHW repository has a wealth of information on this topic.

### Red Team Tools

*   **Metasploit:** A popular penetration testing framework. Use case: Exploiting a vulnerable SMB service on a Windows server using the EternalBlue module to gain remote code execution.
*   **Burp Suite:** A suite of tools for web application security testing. Use case: Intercepting and modifying HTTP requests to test for SQL injection vulnerabilities in a login form.
*   **Nmap:** A network scanner for discovering hosts and services. Use case: Scanning a target network to identify open ports, running services, and potential vulnerabilities like unpatched SSH servers.
*   **Wireshark:** A network protocol analyzer. Use case: Capturing and analyzing network traffic to identify unencrypted credentials or sensitive data being transmitted.
*   **John the Ripper:** A password cracking tool. Use case: Cracking hashed passwords from a leaked database dump to demonstrate weak password policies.

## Blue Team Skills (Defensive Security)

Blue teams defend against attacks and protect an organization's assets. Key skills include:

*   **Incident Response:** Responding to security incidents in a timely and effective manner. The `Blue Team/Incident Response` section in the NTHW repository provides a good overview.
*   **Digital Forensics:** Collecting and analyzing digital evidence to investigate security incidents. The `Blue Team/Forensics` section has resources for this.
*   **Threat Hunting:** Proactively searching for threats and vulnerabilities in the network. The `Blue Team/Threat Hunting` section is a good place to start.
*   **Security Information and Event Management (SIEM):** Using SIEM tools to collect, analyze, and correlate security event data. Popular tools include Splunk, LogRhythm, and IBM QRadar.
*   **Vulnerability Management:** Identifying, assessing, and mitigating vulnerabilities in systems and applications. The `Blue Team/Vulnerability Management` section in the NTHW repository has more information on this.
*   **Network Security Monitoring:** Monitoring network traffic for suspicious activity and anomalies.
*   **Log Analysis:** Analyzing logs from various sources to identify security events and indicators of compromise.

### Blue Team Tools

*   **Splunk:** A popular SIEM and log management platform. Use case: Creating custom dashboards to monitor failed login attempts and detect brute-force attacks in real-time.
*   **Wireshark:** A network protocol analyzer. Use case: Analyzing captured network packets to identify and block malicious traffic, such as data exfiltration attempts.
*   **Snort:** An open-source Intrusion Detection System (IDS). Use case: Configuring rules to detect and alert on known attack patterns, like SQL injection attempts in web traffic.
*   **Zeek (formerly Bro):** A network security monitoring platform. Use case: Monitoring network logs for indicators of compromise, such as unusual outbound connections to command and control servers.
*   **Volatility:** A memory forensics framework. Use case: Analyzing memory dumps from compromised systems to extract malware samples and understand the attacker's persistence mechanisms.
