# 🔐 Password Strength Checker

A simple Python script that checks how strong a password is, based on common security best practices.

## 📖 About this project
This is one of my first cybersecurity-related projects. I built it to understand what actually makes a password weak or strong, and to practice basic Python along the way.

## ⚙️ What it checks
- ✅ Length (minimum 8 characters)
- ✅ At least one uppercase letter
- ✅ At least one lowercase letter
- ✅ At least one number
- ✅ At least one special character (!@#$%^&*...)

## 🚀 How to use it

1. Clone this repo:
```bash
git clone https://github.com/aic-hub/password-strength-checker.git
```

2. Run the script:
```bash
python3 password_checker.py
```

3. Enter a password when prompted, and get instant feedback on its strength.

## 📸 Example output
Enter a password to check: Test123
Password strength: 🟡 Medium

Suggestions:
❌ Add at least one special character (!@#$...)

## 🧠 What I learned
- Why length and character variety matter for password security
- Basics of regex (regular expressions) in Python
- How to structure a simple security-focused script

## 🔮 Ideas for future improvements
- [ ] Check password against common leaked password lists
- [ ] Add a GUI instead of terminal input
- [ ] Estimate time-to-crack based on strength

## 📚 Made while learning cybersecurity fundamentals
