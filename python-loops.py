'''
https://www.hackerrank.com/challenges/python-loops/problem

The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

'''

if __name__ == '__main__':
    print("Enter a number: ")
    n = int(input())
    for i in range(n):
        print(i**2)