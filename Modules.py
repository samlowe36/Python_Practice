import converters               #imports whole module
# from converters import kg_to_lbs     #this is how to call a specific function instead of the whole module

print(converters.kg_to_lbs(70))


from utils import find_max

numbers = [3, 4, 6, 8, 12, 1, 50, 55, 21]
print(find_max(numbers))
