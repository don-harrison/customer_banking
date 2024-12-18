"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
import math
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account = Account(balance, interest_rate)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    newBalance = balance * math.exp((interest_rate/100)*months/12)
    
    interestAccrued = newBalance - balance

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_balance(newBalance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(interestAccrued)

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return account.balance, account.interest
