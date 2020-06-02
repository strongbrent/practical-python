# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if principal * (1+rate/12) <= payment:
        payment = principal * (1+rate/12)

    month = month + 1
    total_paid = total_paid + payment
    principal = principal * (1+rate/12) - payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_paid = total_paid + extra_payment
        principal = principal - extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid:', round(total_paid, 2))
print('Months:', month)
