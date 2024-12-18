# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("User Balance: ")
    while(not savings_balance.isdigit()):
        savings_balance = input("Please input Balance as a number")

    savings_interest = input("Interest Rate: ")
    while(not savings_interest.isdigit()):
        savings_interest = input("Please input interest rate as a number")

    savings_maturity = input("Months: ")
    while(not savings_maturity.isdigit()):
        savings_maturity = input("Please input months as a number")

    savings_balance = float(savings_balance)
    savings_interest = float(savings_interest)
    savings_maturity = float(savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings Account Balance: {updated_savings_balance:.2f} Interest Accrued:  {interest_earned:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("User Balance: ")
    while(not cd_balance.isdigit()):
        cd_balance = input("Please input Balance as a number")

    cd_interest = input("Interest Rate: ")
    while(not cd_interest.isdigit()):
        cd_interest = input("Please input interest rate as a number")

    cd_maturity = input("Months: ")
    while(not cd_maturity.isdigit()):
        cd_maturity = input("Please input months as a number")

    cd_balance = float(cd_balance)
    cd_interest = float(cd_interest)
    cd_maturity = float(cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD Account Balance: {updated_cd_balance:.2f} Interest Accrued:  {interest_earned:.2f}")


if __name__ == "__main__":
    # Call the main function.
    main()