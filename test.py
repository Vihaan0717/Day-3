price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: {down_payment}")

"""22/7/2026-Problem-AND"""
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print('Eligible for loan')
else:
    print('not eligible for loan')