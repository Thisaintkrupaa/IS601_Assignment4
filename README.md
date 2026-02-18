# IS601 Assignment 2 — Command-Line Calculator

A modular, professional-grade calculator with a REPL interface, comprehensive error handling, 100% test coverage, and GitHub Actions CI.

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew --version
```

---

# 🧩 2. Install and Configure Git

```bash
brew install git
git --version
```

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --list
```

## Generate SSH Keys and Connect to GitHub

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub | pbcopy
```

Add key at [GitHub SSH Settings](https://github.com/settings/keys), then test:

```bash
ssh -T git@github.com
```

---

# 🧩 3. Clone the Repository

```bash
git clone git@github.com:Thisaintkrupaa/IS601_Assignment2.git
cd IS601_Assignment2
```

---

# 🛠️ 4. Install Python 3.10+

```bash
brew install python
python3 --version
```

## Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# 🚀 5. Running the Calculator

```bash
python main.py
```

### Supported Operations

| Command         | Description               |
| --------------- | ------------------------- |
| `add 10 5`      | Adds two numbers → 15.0   |
| `subtract 20 3` | Subtracts → 17.0          |
| `multiply 7 8`  | Multiplies → 56.0         |
| `divide 20 4`   | Divides → 5.0             |
| `help`          | Shows help message        |
| `history`       | Shows calculation history |
| `exit`          | Exits the calculator      |

---

# 🧪 6. Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=app tests/

# Enforce 100% coverage
coverage report --fail-under=100
```

---

# ⚙️ 7. GitHub Actions CI

Every push to `main` automatically runs all tests and enforces 100% coverage via `.github/workflows/python-app.yml`.

---

# 🎯 Design Patterns Used

| Pattern             | Where Applied                                                 |
| ------------------- | ------------------------------------------------------------- |
| **LBYL**            | `CalculationFactory` checks operation name before creating    |
| **EAFP**            | `calculator()` uses try/except for parsing and execution      |
| **Factory Pattern** | `CalculationFactory` centralizes Calculation creation         |
| **DRY Principle**   | Operations defined once in `app/operation`, reused everywhere |

---

# 📝 8. Submission Instructions

```bash
git add .
git commit -m "Complete Assignment 2"
git push origin main
```

Then submit your GitHub repository link on Canvas.

---

# 🔥 Useful Commands Cheat Sheet

| Action                       | Command                                            |
| ---------------------------- | -------------------------------------------------- |
| Clone Repository             | `git clone <repo-url>`                             |
| Activate Virtual Environment | `source venv/bin/activate`                         |
| Install Python Packages      | `pip install -r requirements.txt`                  |
| Run Calculator               | `python main.py`                                   |
| Run Tests                    | `pytest tests/`                                    |
| Run Tests with Coverage      | `pytest --cov=app tests/`                          |
| Push Code to GitHub          | `git add . && git commit -m "message" && git push` |

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
