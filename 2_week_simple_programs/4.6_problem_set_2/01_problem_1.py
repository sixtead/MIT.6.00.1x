# -*- coding: utf-8 -*-
"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

`balance` - the outstanding balance on the credit card

`annualInterestRate` - annual interest rate as a decimal

`monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

`Remaining balance: 813.41`

instead of

`Remaining balance: 813.4141998135`

So your program only prints out one thing: the remaining balance at the end of the year in the format:

`Remaining balance: 4784.0`

A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) * (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate * Monthly unpaid balance)

We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.
"""


def balance_after_n_months(
        balance,
        annualInterestRate,
        monthlyPaymentRate,
        months):
    month_balance = balance_after_one_month(balance,
                                            annualInterestRate,
                                            monthlyPaymentRate)
    for m in range(months - 1):
        month_balance = balance_after_one_month(month_balance,
                                                annualInterestRate,
                                                monthlyPaymentRate)
    return "Remaining balance: " + str(round(month_balance, 2))


def balance_after_one_month(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = (monthlyUnpaidBalance
                      + monthlyInterestRate * monthlyUnpaidBalance)
    return updatedBalance


# Testing
print("# Test Case 1:")
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print(balance_after_n_months(balance,
                             annualInterestRate,
                             monthlyPaymentRate,
                             12))
# Result Your Code Should Generate Below:
# Remaining balance: 31.38

print("Test Case 2:")
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print(balance_after_n_months(balance,
                             annualInterestRate,
                             monthlyPaymentRate,
                             12))
# Result Your Code Should Generate Below:
# Remaining balance: 361.61
