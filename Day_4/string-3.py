
import sys


def printAl(string):
    my_list_final = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if check_palindrome(string[i:j+1]):
                my_list_final.append((i, j+1))
    max_ = -sys.maxsize, -1
    for count, i in enumerate(my_list_final):
        if abs(i[0] - i[1]) > max_[0]:
            max_ = abs(i[0] - i[1]), count
    if len(my_list_final) == 0:
        return string[0]
    else:
        value = my_list_final[max_[1]]
        return string[value[0] : value[1]]


def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = str(input())
        print(printAl(string), end=" ")
        print()