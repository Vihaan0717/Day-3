"""RE-call 5-08-26//lets start with a question"""
price_house = 10000000
has_good_cridit = True
has_bad_cridt = False

if has_good_cridit:
    down_pyment = 0.1 * price_house
    print(f"Down Payment = {down_pyment}")
else:
    down_payment = 0.2 * price_house
    print(f"Down Payment = {down_payment}")
    
"""Weight"""

weight = input("weight: ")
unit = input("(L)lb or (K)kg: ")
if unit.upper() == "L":
    converted = float(weight) * float(0.453592)
    print(f'Weight is: {converted:.2f}')
else:
    converted = float(weight) * float(2.20462)
    print(f"weight is: {converted:.2f}")