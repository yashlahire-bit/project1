Password Strength Analyzer & Custom Wordlist Generator
Project Overview
This project was developed during a Cybersecurity Internship with Elevate Labs. The primary objective was to build a dual-purpose security tool that evaluates the strength of user passwords and generates targeted, attack-specific wordlists for educational and testing purposes.

Features

Password Strength Analysis: Uses the zxcvbn library to calculate entropy, crack time, and provide actionable feedback.   
Custom Wordlist Generation: Takes user-specific inputs (names, pets, dates) to generate variations used in dictionary attacks.   
Pattern Implementation: Automatically applies "leetspeak" transformations and appends common patterns like years.   
Export Functionality: Outputs the generated data into a .txt format compatible with standard penetration testing tools.


Tools & Technologies
Language: Python    

Key Libraries: zxcvbn (Entropy analysis), argparse (CLI), itertools    

Security Framework: Inspired by the OWASP top 10 checklist for credential security.

Installation & Usage
Clone the repository:
Install dependencies:

Bash
pip install zxcvbn
Run the tool:

Bash
python analyzer.py

Project Deliverables
As per the internship requirements, this repository contains:

The Python-based analysis tool.   

Exported attack-specific wordlists.   

A comprehensive project report (under 2 pages).   

Ethical Constraint
Note: This project is for educational and ethical security testing purposes only. It was built as part of an MSME India-recognized internship program to help users understand and improve their digital security.
