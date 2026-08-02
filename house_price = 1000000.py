"""Re-call 02-08-26 Amma"""
house_price = 1000000
has_good_grade = True
has_bad_grade = False

if has_good_grade:
    down_payment = 0.1 * house_price
    print(f"Down payment: {down_payment}")
else:
    down_payment = 0.2 * house_price
    print(f"Down payment: {down_payment}")
