numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()

numbers.append(20)
print(numbers)


numbers.insert(0,13)
print(numbers)


numbers.remove(1)
print(numbers)


numbers.pop()
print(numbers)


numbers.index(2)
print(numbers)


print(50 in numbers)

print(numbers.count(7))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


numbers.clear()
print(numbers)
print(numbers2)


list1 = [7, 1, 2, 3, 5, 5, 9, 9, 100, 125, 125, 7, 3]
uniques = []

for num in list1:
    if num not in uniques:
        uniques.append(num)
print(uniques)
#removes duplicates from a list