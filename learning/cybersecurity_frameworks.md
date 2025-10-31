# A Guide to Essential Cybersecurity Frameworks

This document provides an overview of key cybersecurity frameworks and standards. Understanding and utilizing these frameworks is crucial for building a robust cybersecurity posture, ensuring compliance, and speaking a common language with other security professionals.

## 1. MITRE ATT&CK®

**What it is:** The [MITRE ATT&CK](https://attack.mitre.org/) framework is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. It is not a set of standards or a compliance checklist, but a model of how adversaries operate.

**Why it's important:**
*   **Threat-Informed Defense:** It helps organizations to understand how attackers operate, enabling them to build defenses that are tailored to real-world threats.
*   **Common Language:** It provides a common lexicon for security professionals to describe and discuss adversary behaviors.
*   **Security Assessment:** It can be used to assess the effectiveness of existing security controls and to identify gaps in coverage.

**Key Components:**
*   **Tactics:** The adversary's technical goals. Examples include:
    *   **Initial Access:** Gaining a foothold in the network.
    *   **Execution:** Running malicious code.
    *   **Persistence:** Maintaining access across restarts.
    *   **Privilege Escalation:** Gaining higher-level permissions.
    *   **Defense Evasion:** Avoiding detection.
    *   **Credential Access:** Stealing account names and passwords.
    *   **Discovery:** Figuring out the environment.
    *   **Lateral Movement:** Moving through the environment.
    *   **Collection:** Gathering data of interest.
    *   **Command and Control:** Communicating with compromised systems.
    *   **Exfiltration:** Stealing data.
    *   **Impact:** Manipulating, interrupting, or destroying systems and data.
*   **Techniques:** The specific methods used by adversaries to achieve their goals. For example, under the "Initial Access" tactic, techniques include:
    *   **Phishing:** Sending emails with malicious attachments or links.
    *   **External Remote Services:** Exploiting services like VPNs or RDP.
    *   **Drive-by Compromise:** Infecting users who visit a malicious website.

## 2. NIST Cybersecurity Framework (CSF)

**What it is:** The [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) is a set of voluntary guidelines developed by the U.S. National Institute of Standards and Technology (NIST) to help organizations manage and reduce cybersecurity risk.

**Why it's important:**
*   **Risk Management:** It provides a structured approach to identifying, assessing, and managing cybersecurity risk.
*   **Flexibility:** It is designed to be flexible and can be adapted to any organization, regardless of size, sector, or geography.
*   **Communication:** It provides a common language for communicating cybersecurity risk to both technical and non-technical stakeholders.

**Key Components:**
*   **The Core:** A set of cybersecurity activities, outcomes, and informative references that are common across critical infrastructure sectors. The Core is composed of five functions:
    *   **Identify:** Understand the business context, the resources that support critical functions, and the related cybersecurity risks.
    *   **Protect:** Develop and implement appropriate safeguards to ensure delivery of critical infrastructure services.
    *   **Detect:** Develop and implement the appropriate activities to identify the occurrence of a cybersecurity event.
    *   **Respond:** Develop and implement the appropriate activities to take action regarding a detected cybersecurity event.
    *   **Recover:** Develop and implement the appropriate activities to maintain plans for resilience and to restore any capabilities or services that were impaired due to a cybersecurity event.
*   **Implementation Tiers:** These provide context on how an organization views cybersecurity risk and the processes in place to manage that risk. The tiers are:
    *   **Tier 1: Partial:** Risk management is ad-hoc and reactive.
    *   **Tier 2: Risk-Informed:** Risk management practices are approved by management but may not be established as organization-wide policy.
    *   **Tier 3: Repeatable:** Risk management practices are formally approved and expressed as policy.
    *   **Tier 4: Adaptive:** The organization adapts its cybersecurity practices based on lessons learned and predictive indicators.
*   **Profiles:** A representation of the outcomes that a particular system or organization has selected from the Framework Core and how it has tailored them to its specific needs.

## 3. CIS Critical Security Controls (CIS Controls)

**What it is:** The [CIS Controls](https://www.cisecurity.org/controls/) are a prioritized set of actions that form a defense-in-depth set of best practices that mitigate the most common attacks against systems and networks.

**Why it's important:**
*   **Prioritization:** The controls are prioritized to help organizations focus on the most critical actions first.
*   **Actionable Guidance:** The controls provide specific and actionable guidance that can be implemented to improve security.
*   **Community-Driven:** The controls are developed and maintained by a community of experts from government, industry, and academia.

**The 18 CIS Critical Security Controls:**
1.  Inventory and Control of Enterprise Assets
2.  Inventory and Control of Software Assets
3.  Data Protection
4.  Secure Configuration of Enterprise Assets and Software
5.  Account Management
6.  Access Control Management
7.  Continuous Vulnerability Management
8.  Audit Log Management
9.  Email and Web Browser Protections
10. Malware Defenses
11. Data Recovery
12. Network Infrastructure Management
13. Network Monitoring and Defense
14. Security Awareness and Skills Training
15. Service Provider Management
16. Application Software Security
17. Incident Response Management
18. Penetration Testing

## 4. ISO/IEC 27001

**What it is:** [ISO/IEC 27001](https://www.iso.org/isoiec-27001-information-security.html) is an international standard for information security. It specifies the requirements for establishing, implementing, maintaining, and continually improving an Information Security Management System (ISMS).

**Why it's important:**
*   **International Recognition:** It is the most widely recognized international standard for information security.
*   **Compliance:** Certification to ISO/IEC 27001 can help organizations to meet legal and regulatory requirements.
*   **Customer Confidence:** It can provide customers and partners with confidence that an organization is following best practices for information security.

**Key Components:**
*   **Information Security Management System (ISMS):** A systematic approach to managing sensitive company information so that it remains secure. It includes people, processes, and technology.
*   **Clauses 4-10:** These are the mandatory requirements of the standard, covering topics such as the context of the organization, leadership, planning, support, operation, performance evaluation, and improvement.
*   **Annex A:** A list of 114 security controls in 14 domains that can be used to address information security risks.

## 5. OWASP Top 10

**What it is:** The [OWASP Top 10](https://owasp.org/www-project-top-ten/) is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.

**Why it's important:**
*   **Developer Awareness:** It raises awareness among developers about the most common web application security risks.
*   **Actionable Guidance:** It provides actionable guidance on how to prevent and mitigate these risks.
*   **Industry Standard:** It is widely used as a benchmark for web application security.

**The OWASP Top 10 2021:**
1.  **A01:2021 - Broken Access Control:** Failures to properly enforce restrictions on what authenticated users are allowed to do.
2.  **A02:2021 - Cryptographic Failures:** Failures related to cryptography (or lack thereof), which often lead to exposure of sensitive data.
3.  **A03:2021 - Injection:** Flaws that allow untrusted data to be interpreted and executed as part of a command or query.
4.  **A04:2021 - Insecure Design:** A new category focusing on risks related to design flaws.
5.  **A05:2021 - Security Misconfiguration:** Missing or insecure configuration of security settings.
6.  **A06:2021 - Vulnerable and Outdated Components:** Using components with known vulnerabilities.
7.  **A07:2021 - Identification and Authentication Failures:** Incorrect implementation of functions related to user identity, authentication, and session management.
8.  **A08:2021 - Software and Data Integrity Failures:** A new category focusing on making assumptions about software updates, critical data, and CI/CD pipelines without verifying integrity.
9.  **A09:2021 - Security Logging and Monitoring Failures:** Insufficient logging and monitoring to detect and respond to security incidents.
10. **A10:2021 - Server-Side Request Forgery (SSRF):** Flaws that allow an attacker to induce the server-side application to make requests to an unintended location.
