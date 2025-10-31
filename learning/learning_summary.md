# Cybersecurity Learning Path

This document provides a summary of the most important categories and skills from the Not The Hidden Wiki (NTHW) repository, organized into a suggested learning path.

## Foundational Skills

Before diving into specialized cybersecurity fields, it's essential to have a strong foundation in the following areas:

*   **Computer Networks:** Understand the fundamentals of networking, including TCP/IP, DNS, HTTP/S, and common network protocols. The NTHW repository has a dedicated section for this under `Computer Networks`.
*   **Linux:** Develop proficiency in the Linux command line. The NTHW repository has many resources for this, and it's a crucial skill for most cybersecurity roles. I will scrape more information on this topic as you requested.
*   **Programming:** Learn a programming language like Python. Python is widely used in cybersecurity for scripting, automation, and developing tools. The `Programming/Python` section in the NTHW repository is a good place to start.

## Core Cybersecurity Disciplines

Once you have a solid foundation, you can start exploring the core disciplines of cybersecurity. The NTHW repository is broadly divided into Red Team (offensive security) and Blue Team (defensive security).

### Red Team (Offensive Security)

Red Teaming involves simulating attacks to identify vulnerabilities. Key areas to focus on include:

*   **Web Hacking:** Learn how to find and exploit vulnerabilities in web applications. The `Red Team/Web Hacking` section is a great resource.
*   **Privilege Escalation:** Understand how to gain higher levels of access on a system. The `Red Team/Privilege Escalation` section has resources for both Linux and Windows.
*   **Active Directory:** Learn how to attack and defend Active Directory environments. See the `Red Team/Active Directory` section.
*   **CTF Platforms:** Practice your skills on platforms like Hack The Box and TryHackMe. The `CTF Platforms` section has links to many of these platforms and write-ups.

### Blue Team (Defensive Security)

Blue Teaming focuses on defending against attacks. Key areas to focus on include:

*   **Incident Response:** Learn how to respond to security incidents. The `Blue Team/Incident Response` section has valuable resources.
*   **Forensics:** Understand how to collect and analyze digital evidence. See the `Blue Team/Forensics` section.
*   **Threat Hunting:** Proactively search for threats in your network. The `Blue Team/Threat Hunting` section provides a good starting point.

## Advanced Topics

Once you have a good understanding of the core disciplines, you can explore more advanced topics like:

*   **Malware Analysis:** Learn how to reverse engineer and analyze malware. The `Red Team/Malware` section has resources for this.
*   **DevSecOps:** Understand how to integrate security into the DevOps lifecycle. The `DevSecOps` section provides a good overview.
*   **Cryptography:** Learn about the principles of cryptography and how to apply them. The `Cryptography` section has a collection of resources.

This is just a suggested learning path, and you can tailor it to your interests. The NTHW repository is a vast resource, so take your time to explore the different categories and find what you're passionate about.

## Essential Linux Commands

Here are some essential Linux commands to get you started:

### File and Directory Operations

*   **`ls`**: List directory contents. Use `ls -l` for a long format listing, `ls -a` to show hidden files, and `ls -F` to indicate file types.
*   **`pwd`**: Print the current working directory.
*   **`cd [directory]`**: Change directory. Use `cd ..` to go up one level, `cd` or `cd ~` to go to the home directory, and `cd -` to go to the previous directory.
*   **`mkdir [directory_name]`**: Create a new directory.
*   **`rmdir [directory_name]`**: Remove an empty directory.
*   **`cp [source] [destination]`**: Copy files or directories. Use `cp -r` to copy directories recursively.
*   **`mv [source] [destination]`**: Move or rename files and directories.
*   **`rm [file/directory]`**: Delete files or directories. Use `rm -r` to delete directories and their contents, and `rm -f` to force removal without confirmation. Use `rm -rf` with extreme caution as it forcefully removes an entire directory and its contents.
*   **`touch [file_name]`**: Create a new empty file or update the timestamp of an existing file.
*   **`cat [file_name]`**: Display the contents of a file.
*   **`head [file_name]`**: Display the first 10 lines of a file (use `-n` to specify a different number of lines).
*   **`tail [file_name]`**: Display the last 10 lines of a file (use `-n` to specify a different number of lines).
*   **`less [file_name]`**: View file contents page by page.

### System Information

*   **`uname -a`**: Display detailed information about the Linux kernel and system.
*   **`whoami`**: Display the current username.
*   **`df -h`**: Display disk space usage in a human-readable format.
*   **`du -sh [directory]`**: Display the disk usage of a directory in a human-readable format.
*   **`top`**: Display running processes and system resource usage dynamically.
*   **`ps aux`**: Display all running processes.

### Process Management

*   **`kill [PID]`**: Terminate a process by its Process ID (PID).
*   **`killall [process_name]`**: Terminate all processes with a given name (use with extreme caution).
*   **`bg`**: List stopped or background jobs; resume a stopped job in the background.
*   **`fg`**: Bring the most recent job to the foreground.

### Text Processing

*   **`grep [pattern] [file_name]`**: Search for a pattern within a file. Use `grep -i` for case-insensitive search, `grep -v` to invert the match, and `grep -r` to search recursively.
*   **`sort [file_name]`**: Sort lines of text files.
*   **`wc [file_name]`**: Count lines, words, and characters in a file.

### Permissions

*   **`chmod [permissions] [file_name]`**: Change file permissions.
*   **`chown [user:group] [file_name]`**: Change file owner and group.

### Networking

*   **`ping [hostname/IP]`**: Test network connectivity to a host.
*   **`ip addr`** or **`ifconfig`**: Display network interface information.

### Other Useful Commands

*   **`clear`**: Clear the terminal screen.
*   **`man [command]`**: Display the manual page for a command.
*   **`sudo [command]`**: Execute a command with superuser privileges.
*   **`echo [text]`**: Display text on the terminal.
*   **`history`**: Display a list of previously executed commands.
