#this program demonstrates how a function takes string and a character and conuts
#how many appearences the character makes in said string
#Author: Gal Elhiani
#Tester: Ron Cohen

string = "hello"
char = 'l'
def CharCount(ch, str):
    """Counts the number of occureneces of a given character in the given string"""
    count = 0
    for i ,c in enumerate(str):
        if(str[i] == ch):
            count+=1

    return count


print(CharCount(char, string))
