# Password Strength Checker with Suggestions

## Client: SafeBank

### Request
SafeBank, a startup building a secure banking app, aims to educate users on creating strong passwords. This Python script evaluates password strength based on length, character variety, and common patterns, then provides specific improvement suggestions.

## Features
- Checks password strength using predefined security criteria.
- Uses regex to detect common patterns and weaknesses.
- Provides actionable suggestions for stronger passwords.
- Ensures passwords are at least 8 characters long and encourages 16+ characters for added security.
- Identifies and warns against common weak patterns like "123", "qwerty", and "1qaz2wsx".

## Skills Used
- **Python Scripting**: Core logic implementation.
- **Regex (Regular Expressions)**: Detecting patterns in passwords.
- **Security Best Practices**: Ensuring robust password recommendations.

## Installation
```sh
# Clone the repository
git clone https://github.com/junecodes767/Password-Strength-Checker.git
cd password-strength-checker


## Usage
Run the script and enter a password to analyze its strength:
```sh
python password_checker.py
```

Example output:
```
Please enter password: password123
Your Password: password123 needs to be over 8 digits.
Must include special characters
Must have uppercase Letters
Must have lower_case letters
Must include digits.
Please make the password 16 characters or more: SecurePassword!123
Thank you! 'SecurePassword!123' is now a good password.
'YourSecurePass!1234' is now a strong password!
```

## Portfolio Focus
This project showcases skills in **security** and **user guidance**, demonstrating expertise in writing scripts that help users create stronger passwords.
 
