weight = input("Weight is: ")
unit = input("(L)lb or (K)kg ?")
if unit.upper() == "L":
    converted = float(weight) * float(0.453592)
    print(f"Weight is: {converted:.2f}")
else:
    converted = float(weight) * float(2.20462)
    print(f"Weight is: {converted:.2f}")
