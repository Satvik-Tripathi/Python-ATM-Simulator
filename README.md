# Python ATM Machine Simulator (OOP Project)

This is a console-based ATM (Automated Teller Machine) simulator built using Python.
The project demonstrates fundamental Object-Oriented Programming (OOP) concepts by
creating a `BankAccount` class and then utilizing it within an interactive menu-driven
application.

## Features

* **Account Creation:** Instantiates a `BankAccount` object for a new user.
* **Deposit:** Allows users to add funds to their balance.
* **Withdrawal:** Allows users to withdraw funds, with validation to prevent overdrawing.
* **Check Balance:** Displays the current account balance.
* **Interactive Menu:** Guides the user through options to perform banking operations.
* **Robust Input Handling:** Uses `try-except` blocks to handle invalid (non-numeric) input gracefully and ensures positive transaction amounts.

## Key Concepts Demonstrated

* **Object-Oriented Programming (OOP):**
    * **Classes & Objects:** Defined a `BankAccount` class with `__init__` (constructor) and created instances (objects) of it.
    * **Encapsulation:** Grouped data (`name`, `balance`) and methods (`deposit`, `withdraw`, `display`) within a single class.
    * **Methods:** Implemented functions that operate on the object's data.
* **Control Flow:** Utilized `if/elif/else` statements for menu navigation and transaction logic.
* **Loops:** Employed a `while True` loop to keep the ATM operational until the user chooses to exit.
* **Error Handling:** Implemented `try-except ValueError` for robust handling of user input.

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Download the `atm_simulator.py` file from this repository.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command:
    ```bash
    python atm_simulator.py
    ```
6.  Follow the on-screen prompts to interact with the ATM.
