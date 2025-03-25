# List Manipulation
# 1. Create an empty list called my_list
my_list = []

# 2. Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# Alternatively: my_list = [10, 20, 30, 40]

# 3. Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("After insert:", my_list)  # Should print: [10, 15, 20, 30, 40]

# 4. Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extend:", my_list)  # Should print: [10, 15, 20, 30, 40, 50, 60, 70]

# 5. Remove the last element from my_list
my_list.pop()
print("After pop:", my_list)  # Should print: [10, 15, 20, 30, 40, 50, 60]

# 6. Sort my_list in ascending order
my_list.sort()
print("After sort:", my_list)  # Should print: [10, 15, 20, 30, 40, 50, 60]

# 7. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)  # Should print: 3