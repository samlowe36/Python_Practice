for item in "Python":
    print(item)
#goes through all letters

for thing in ["Sam", "Maribel", "Dominic"]:
    print(thing)
#goes through all names

for num in [1, 2, 3, 4, 5]:
    print(num)
#goes through all numbers

for number in range(10):
    print(number)
# from 0 to 9

for num2 in range(3, 10):
    print(num2)
#from 3 to 9

for num3 in range(3, 10, 2):
    print(num3)
#from 3 to 9, count by 2


prices = [10, 20, 30]
total = 0

for amount in prices:
    total += amount

print(f"Total: ${total}")
