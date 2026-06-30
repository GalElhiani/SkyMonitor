lst =["1", "3", "9", "5", "4", "10", "2"]
sorted_list = lambda target_list: sorted(map(int, target_list))     #map converts all strings in target_list to int
result = sorted_list(lst)
print(result)
