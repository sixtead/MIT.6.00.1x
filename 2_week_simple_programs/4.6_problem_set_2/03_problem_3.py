# -*- coding: utf-8 -*-
"""
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

`balance` - the outstanding balance on the credit card

`annualInterestRate` - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance * (1 + Monthly interest rate)^12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
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


def calculate_monthly_payment(balance, annualInterestRate, months):
    """Calculates fixed monthly payment required to pay off credit card debt.

    Args:
        balance (int or float): Balance at the beginning of month
        annualInterestRate (float): Interest charged on unpaid balance
        months (int): Number of months for which to guess the payment

    Returns:
        string: Guesses monthly payment and increases it if it's too small,
            e.g. blance is greater than 0. Or decreases it if balance is to
            less than 0. Returns concatenated string with text and value
            rounded to 2 decimal points.
    """
    monthlyInterestRate = annualInterestRate / 12
    lowerMonthlyPayment = balance / 12
    upperMonthlyPayment = (balance * (1 + monthlyInterestRate)**12) / 12.0

    while True:
        guess = (lowerMonthlyPayment + upperMonthlyPayment) / 2
        totalBalance = balance_after_n_months(balance, guess,
                                              annualInterestRate, 12)

        if totalBalance > 0:
            lowerMonthlyPayment = guess
        elif totalBalance < 0:
            upperMonthlyPayment = guess
        else:
            break

    return "Lowest Payment: " + str(round(guess, 2))


# Test Case 1:
balance = 320000
annualInterestRate = 0.2
print(calculate_monthly_payment(balance, annualInterestRate, 12))
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 29157.09

# Test Case 2:
balance = 999999
annualInterestRate = 0.18
print(calculate_monthly_payment(balance, annualInterestRate, 12))
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 90325.03
