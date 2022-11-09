weight = input("Please enter your weight: ")
lbs_or_kg = input("(L)bs or (K)g: ")

if lbs_or_kg.upper() == "L":
    print(f"You are {float(weight) * 0.45} Kilos")
elif lbs_or_kg.upper() == "K":
    print(f"You are {float(weight) / 0.45} Pounds")
else:
    print("Invalid")