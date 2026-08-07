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
    
