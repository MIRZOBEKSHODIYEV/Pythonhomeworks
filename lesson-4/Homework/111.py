list1 = [1, 1, 2]
list2 = [2, 3, 4]
list1_filter = [item for item in list1 if item not in list2]
list2_filter = [item for item in list2 if item not in list1]
output = list1_filter + list2_filter

print(output) 