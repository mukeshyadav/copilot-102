def calculate_amortization(principal, annual_interest_rate, loan_term_years):
    """
    Calculates the monthly payment for an amortized loan.

    Args:
        principal (float): The principal amount of the loan.
        annual_interest_rate (float): The annual interest rate as a percentage.
        loan_term_years (int): The loan term in years.

    Returns:
        float: The monthly payment for the loan.
    """
    # Convert annual interest rate to monthly and in decimal
    monthly_interest_rate = annual_interest_rate / (12 * 100)

    # Convert loan term from years to months
    loan_term_months = loan_term_years * 12

    # Calculate the monthly payment using the formula
    monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate)**loan_term_months / ((1 + monthly_interest_rate)**loan_term_months - 1)

    return monthly_payment

if __name__ == "__main__":
    print(hello_world())