customer = {
    "Name": "John Smith",
    "Age": 30,
    "is_verified": True
}
print(customer.get("Name"))

customer["Name"] = "Jack Smith"
customer["Birthdate"] = "Jan 1 1980"
print(customer)


phone_numbers = { #define dictionary
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine ",
    "0": "Zero "
}
phone = input("Phone: ") #define input
output = "" #define output

for digit in phone: #loop through our input string
    output += phone_numbers.get(digit, "!") #get the numbers corresponding to digit and add them to the output + "!" for invalid entries
print(output)