#Write a program to calculate the no.of digits in a given number.

#Input Format

#A single integer denoting the number

#Constraints

#1<=num<=10000

#Output Format

#Print the count of the digits
#solution:-
#!/bin/python3

import sys

if __name__ == "__main__":
    num = int(input().strip())
    print(len(str(num)))
