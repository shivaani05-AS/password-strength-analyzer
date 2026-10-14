# password-strength-analyzer
A Python-based tool that evaluates password strength using length, character diversity, and common password patterns.
# Password Strength Analyzer Using Python

## Project Overview
The Password Strength Analyzer is a Python-based cybersecurity project that evaluates password strength using length, character diversity, and common password patterns.

## Objectives
- Understand password security fundamentals.
- Evaluate password length and character variety.
- Identify common and easily guessed passwords.
- Provide suggestions for creating stronger passwords.

## Technologies Used
- Python 3
- Regular Expressions (`re`)
- `getpass` module

## Features
- Checks password length.
- Checks uppercase and lowercase letters.
- Checks numeric and special characters.
- Detects a small list of common passwords.
- Displays a strength rating and improvement suggestions.
- Hides password input in a compatible terminal.

## Project Structure
```text
password-strength-analyzer/
├── password_analyzer.py
├── README.md
└── .gitignore
```

## Requirements
- Python 3.x
- No external packages required.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python password_analyzer.py
```

5. Enter a sample password and review the result.

## Security Note
This project is for educational purposes. Analyze sample passwords rather than reusing real account passwords. The program performs a basic heuristic check and cannot guarantee that a password is secure. Use unique passwords and a reputable password manager.

## Author
**Shivaani Shree SR**

## Conclusion
This project demonstrates basic password-strength evaluation using Python and provides feedback to encourage better password practices.
