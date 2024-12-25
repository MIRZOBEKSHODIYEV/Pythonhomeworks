list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
list1_filter= [iteam for iteam in list1 if iteam not in list2 ]
list2_filter= [iteam for iteam in list2 if iteam not in list1 ]
output= list1_filter+list2_filter
print(output)