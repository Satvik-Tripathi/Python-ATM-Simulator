"""
Basic ATM Machine Simulator

This project uses an object-oriented approach to create a simple
BankAccount class and then simulates an ATM interface in the console,
allowing a user to deposit, withdraw, and check their balance.
"""

# ---BankAccount Class---
class BankAccount:
    def __init__(self,name):
        self.name=name
        self.balance=0
        print(f'Hello {self.name}! Your account has been created.')
        print(f'Your starting balance is {self.balance} $')
   
    def deposit(self,amt):
        self.balance = self.balance + amt
        print(f'Deposited {amt} $. Your new balance is {self.balance} $')
    
    def withdraw(self,amt):
        if amt > self.balance:
            print(f'Kangaal ho jaayega bhai RUK JAA!! Insufficient funds.')
            print(f'You only have {self.balance} $')
        else:
           self.balance = self.balance - amt
           print(f'Withdrew {amt} $. Your new balance is {self.balance} $')
    
    def display(self):
        print(f'Account Holder: {self.name}')
        print(f'Your current Balance is {self.balance} $')

# --- Main Application Logic (The "ATM Machine") ---

print("\n--- Welcome to the Basic ATM ---")
# Get the account holder's name
holder_name = input("Please enter your name: ").strip()

# Create an instance (an object) of your BankAccount class
my_account = BankAccount(holder_name)

# This is the main application loop
while True:
    print("\nWhat would you like to do?")
    print("  1. Deposit")
    print("  2. Withdraw")
    print("  3. Check Balance")
    print("  4. Exit")
    
    try:
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # --- Deposit Logic ---
            try:
                amt = int(input("Enter amount to deposit: "))
                if amt <= 0:
                    print("Deposit amount must be positive.")
                else:
                    my_account.deposit(amt) # Calling the object's method
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == '2':
            # --- Withdraw Logic ---
            try:
                amt = int(input("Enter amount to withdraw: "))
                if amt <= 0:
                    print("Withdrawal amount must be positive.")
                else:
                    my_account.withdraw(amt) # Calling the object's method
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            # --- Display Balance Logic ---
            my_account.display() # Calling the object's method
        
        elif choice == '4':
            # --- Exit Logic ---
            print(f"Thank you for banking with us, {my_account.name}. Goodbye!")
            break # This exits the 'while True' loop
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
