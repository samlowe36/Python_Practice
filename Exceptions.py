try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(f"{age} years old")
except ValueError:
    print("Invalid Value. Enter a whole number.")
except ZeroDivisionError:
    print('Age cannot be zero')
