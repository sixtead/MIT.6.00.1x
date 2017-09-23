# -*- coding: utf-8 -*-
"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

`balance` - the outstanding balance on the credit card

`annualInterestRate` - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate * Monthly unpaid balance)
"""


def balance_after_one_month(balance, monthlyPayment, annualInterestRate):
    """Calculates credit card balance after one month

    Args:
        balance (int or float): Balance at the beginning of month
        monthlyPayment (int or float): Fixed monthly payment
        annualInterestRate(float): Interest charged on unpaid balance

    Returns:
        float: Balance at the end of the month. Calculated after
            payments and charging monthly interest
    """
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyUnpaidBalance = balance - monthlyPayment
    updatedBalance = (monthlyUnpaidBalance
                      + monthlyInterestRate * monthlyUnpaidBalance)
    return updatedBalance


def balance_after_n_months(
        balance,
        monthlyPayment,
        annualInterestRate,
        months):
    """Calculates credit card balance after specified amount of months.
       Calls `balance_after_one_month` `months`'s times

    Args:
        balance (int or float): Balance at the beginning of month
        monthlyPayment (int or float): Fixed monthly payment
        annualInterestRate(float): Interest charged on unpaid balance
        months (int): Amount of months for which the balance is calculated

    Returns:
        float: Balance after specified amount of months,
            rounded to 2 decimal digits.
    """
    month_balance = balance_after_one_month(balance, monthlyPayment,
                                            annualInterestRate)
    for x in range(months - 1):
        month_balance = balance_after_one_month(month_balance, monthlyPayment,
                                                annualInterestRate)
    return round(month_balance, 2)


def guess_monthly_payment(balance, annualInterestRate, months):
    """Roughtly guesses monthly payment needed to pay off a credit card
        balance within 12 months.

    Args:
        balance (int or float): Balance at the beginning of month
        annualInterestRate (float): Interest charged on unpaid balance
        months (int): Number of months for which to guess the payment

    Returns:
        float: Divides overall balance by number of months, adds interest rate,
            and rounds it to 10-ths
    """
    return (balance / months) * (1 + annualInterestRate) // 10 * 10


def calculate_monthly_payment(balance, annualInterestRate, months):
    """Calculates fixed monthly payment required to pay off credit card debt.

    Args:
        balance (int or float): Balance at the beginning of month
        annualInterestRate (float): Interest charged on unpaid balance
        months (int): Number of months for which to guess the payment

    Returns:
        string: Guesses monthly payment and increases it if it's too small,
            e.g. blance is greater than 0. Or decreases it if balance is to
            less than 0. Returns concatenated string with text and value.
    """
    guess = guess_monthly_payment(balance, annualInterestRate, months)
    if balance_after_n_months(balance, guess, annualInterestRate, months) > 0:
        monthlyPayment = increase_monthly_payment(balance, guess,
                                                  annualInterestRate, months)
    else:
        monthlyPayment = decrease_monthly_payment(balance, guess,
                                                  annualInterestRate, months)
    return "Lowest Payment: " + str(monthlyPayment)


def increase_monthly_payment(balance,
                             monthlyPayment,
                             annualInterestRate,
                             months):
    """Increases fixed monthly payment by 10 dollars if it's too small.

    Args:
        balance (int or float): Balance at the beginning of month
        monthlyPayment (int or float): Fixed monthly payment
        annualInterestRate(float): Interest charged on unpaid balance
        months (int): Amount of months for which the balance is calculated

    Returns:
        float: minimum monthly payment, so balance is less or equal 0.
    """
    while balance_after_n_months(balance, monthlyPayment, annualInterestRate,
                                 months) > 0:
        monthlyPayment += 10
    return monthlyPayment


def decrease_monthly_payment(balance,
                             monthlyPayment,
                             annualInterestRate,
                             months):
    """Decreases fixed monthly payment by 10 dollars if it's too large.

    Args:
        balance (int or float): Balance at the beginning of month
        monthlyPayment (int or float): Fixed monthly payment
        annualInterestRate(float): Interest charged on unpaid balance
        months (int): Amount of months for which the balance is calculated

    Returns:
        float: minimum monthly payment, so balance is less or equal 0.
    """
    while balance_after_n_months(balance, monthlyPayment, annualInterestRate,
                                 months) < 0:
        monthlyPayment -= 10
    return monthlyPayment + 10


# Test Case 1:
balance = 3329
annualInterestRate = 0.2
print(calculate_monthly_payment(balance, annualInterestRate, 12))
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

# Test Case 2:
balance = 4773
annualInterestRate = 0.2
print(calculate_monthly_payment(balance, annualInterestRate, 12))
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 440

# Test Case 3:
balance = 3926
annualInterestRate = 0.2
print(calculate_monthly_payment(balance, annualInterestRate, 12))
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 360
