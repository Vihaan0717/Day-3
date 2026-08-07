weight = input("weight: ")
unit = input("(K)g or (L)g ?")
if unit.upper == "L":
    converted = weight * int(0.4)
    print(f"your rate = {converted}")
else:
    converted = weight * int (2.3)
    print(f"your rate = {converted}")

