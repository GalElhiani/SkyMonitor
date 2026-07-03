import linked_list

test_list1 = linked_list.LinkedList()
num = [1, 2, 3, 4, 5 ,6]


for i in num:
    test_list1.push(i)

print("after push: \n")
print(test_list1)

test_list1.pop()
print("after one pop: \n")
print(test_list1)

print("test for get_head(): ")
print(test_list1.get_head())

print("test for is empty: ")
print(test_list1.is_empty())

print("test for get_len: ")
print(test_list1.get_len())

print("emptying the list using while loop and testing is_empty() again: ")
while not test_list1.is_empty():
    test_list1.pop()

print(test_list1.is_empty())


