temperature = 85

# different operators: >, >=, <, <=, ==, !=
if temperature > 80:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = "Fred"
print(len(name))

if len(name) < 3:
    print("Name must be at least 3 characters long!")
elif len(name) > 50:
    print("Name can only be a maximum of 50 characters!")
else:
    print("Name looks good!")