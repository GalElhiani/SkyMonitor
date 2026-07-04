#Author: Gal Elhiani
#Tester: Noam Kux

def read_n_lines(file_path, n):
    '''a function that reads the first n lines in a given file'''
    with open(file_path, encoding="utf-8") as file:
        for _ in range(n):
            line = file.readline()
            if not line:
                break
            print(line)
        

#creating a test file to check if the function works
with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")

output = read_n_lines("test_file.txt", 2)

print(output)