# Basic-Banking-System-Python

This Code is written in Python and was made as a basic project while learning Python and OOPS(Object Oriented Programming System) in Python. It allows users to create bank accounts, log in to existing accounts, and perform basic banking operations such as credit, debit, and balance checks.This system is for educational/demo purposes only. It stores data in-memory (i.e., not in a database) and does not implement encryption or real-world security features.

🚀 Features

✅ Create a new account with a unique account number

🔐 Secure login using a password

💰 Deposit (credit) and withdraw (debit) money

📊 Check current balance

🚪 Exit banking operations securely

📂 How It Works:

1. Menu Options
Option 1: Create a new account

Option 2: Login to an existing account

2. Account Creation
Requires a mobile number (used to check for duplicates)

Asks for user's name and password

Generates a random 4-digit account number

Initializes the account with a balance of Rs. 0

3. Login
Enter your account number and password

If valid, enter into banking session

4. Banking Session
DEBIT: Withdraw money (if balance permits)

CREDIT: Deposit money (amount must be > 0)

CHECK BALANCE: View current account balance

EXIT: Exit banking session

🧾 Code Structure
Account class handles banking operations like credit(), debit(), and bank().

User data is stored in a dictionary user, with account number as the key.

Balances are updated and maintained throughout the session.

🛠️ Dependencies
Standard Python libraries only:

random for account number generation

time for adding small delays for realism
