# Program 2: Car Loan Payment

def calculate_car_loan_payment(
    principal_amount: float,
    years_to_pay_off: int,
    annual_interest_rate: float,
) -> float:
    """Calculate the fixed monthly loan payment."""
    number_of_payments = years_to_pay_off * 12
    monthly_interest_rate = annual_interest_rate / 100 / 12

    if principal_amount < 0 or years_to_pay_off <= 0 or annual_interest_rate < 0:
        raise ValueError("Loan amount/rate must be non-negative and years must be positive.")

    if monthly_interest_rate == 0:
        return principal_amount / number_of_payments

    rate_factor = (1 + monthly_interest_rate) ** number_of_payments
    return principal_amount * monthly_interest_rate * rate_factor / (rate_factor - 1)


try:
    principal_amount = float(input("Enter the principal loan amount in rupees: "))
    years_to_pay_off = int(input("Enter the duration to pay off the loan in years: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))

    monthly_payment = calculate_car_loan_payment(
        principal_amount, years_to_pay_off, annual_interest_rate
    )
    print(f"Monthly car loan payment: {monthly_payment:.2f}")
except ValueError as error:
    print(f"Invalid input: {error}")
