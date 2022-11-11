names = ["Maribel", "Aimee", "Sam", "Sara", "Dominic"]
names[0] = "Marbosso"
print(names[2:4])
print(names)


numbers = [5, 10, 15, 20, 25, 11]
print(max(numbers))
#easy way

nums = [5, 10, 15, 11, 20, 26]
max = nums[0]
for max_num in nums:
    if max_num > max:
        max = max_num
print(max)
#for loop way of finding max in a list