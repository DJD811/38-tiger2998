---
layout: default
title: Projects
---

# Capstone Project: Project Trinity (Advanced Web, ERP, & Cloud Penetration)
## Executive Summary
Project Trinity is a comprehensive offensive security and remediation ecosystem designed to simulate and defend against real-world, high-consequence cyber incidents. By replicating three distinct 2025–2026 breach scenarios—Collins Aerospace vMUSE (Aviation), Jaguar Land Rover (Manufacturing), and WWE (Cloud)—this project acts as a live fire exercise for modern security testing. It bridges the gap between offensive web application exploitation and architectural Zero-Trust remediation, proving that modern vulnerabilities can be identified and neutralized before they impact physical operations.

## Problem Statement
Modern organizations suffer from "Flat Networks" and a heavy reliance on third-party supply chain vendors. Entry-level security testing often focuses on isolated, automated web scans while ignoring how attackers chain minor vulnerabilities to pivot into critical operational technology (OT) or harvest misconfigured cloud data lakes. This project solves these gaps by providing a documented repository of manual exploit chains and engineering-level Zero-Trust blueprints to stop lateral movement.

## Technical Architecture
#### System Components
Offensive Suite (Burp Suite Pro & OWASP ZAP): Manual interception, API fuzzing, and unauthenticated request smuggling.

Payload Generators (ysoserial & Python): Weaponizing insecure Java deserialization flaws and automating HTTP upload requests.

Infrastructure & AD (Windows Server & BloodHound): Active Directory mapping, privilege escalation modeling, and Group Policy manipulation.

Cloud Simulator (LocalStack & AWS CLI): Emulating insecure Amazon S3 bucket permissions and automated data exfiltration.

Defensive Hub (pfSense & Wireshark): Micro-segmentation firewalls and deep packet forensics.

#### High-Level Logic
Reconnaissance: An attacker maps public-facing web infrastructure (IIS / Apache Tomcat) and open cloud endpoints using Nmap and AWS discovery tools.

Exploitation: The attacker intercepts HTTP traffic via Burp Suite, uploading a JSP webshell (JLR scenario) or brute-forcing legacy FTP endpoints (vMUSE scenario).

Lateral Movement & Impact: The attacker leverages the compromised web server as a jump-host to scan internal factory/kiosk VLANs or query Active Directory for Domain Admin credentials.

Remediation Action: The engineer implements Zero-Trust ACLs on the pfSense firewall to block cross-subnet communication, rotates credentials, and enforces account-level AWS public block policies.

##### Project Objectives (SMART)
Exploitation: Successfully chain unauthenticated web flaws to achieve Remote Code Execution (RCE) and Active Directory takeovers across three isolated lab subnets.

Mapping: Map all simulated attack paths to the MITRE ATT&CK framework to ensure realistic threat emulation.

Containment: Prove that micro-segmentation can reduce the "blast radius" of a compromised server by successfully blocking lateral movement to production zones.

Professional Reporting: Produce a client-facing penetration testing report featuring CVSS 10.0 risk calculations and step-by-step code remediation guidelines.

##### Implementation Roadmap
Month 1 (Bones): Virtualization setup, Active Directory deployment, isolated network segmentation, and Kali Linux environment spinning.

Month 2 (Exploitation): Execution of the vMUSE (Identity/Aviation) and JLR (Java/ERP) manual attack chains using Burp Suite and ysoserial.

Month 3 (Cloud & Response): Simulation of the WWE S3 cloud exposure via LocalStack, Python automated audit scripts, and final Zero-Trust remediation deployment.