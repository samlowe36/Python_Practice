for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")
#inner loop iterates for its whole range each time the outer loop iterates once

numbers = [5, 2, 5, 2, 2]
numbers2 = [2, 2, 2, 2, 5]
letters = "x"

for x_count in numbers:
    print(x_count * letters)
  #easy way

print("________________________________________________")

for x_count2 in numbers2:
    output = ""
    for count in range(x_count2):
        output += 'x'
    print(output)
#nested loops way