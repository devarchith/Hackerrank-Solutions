#HackerLand University has the following grading policy:

#Every student receives a grade  in the inclusive range 0 from  to 100  .
#Any  less than 40 is a failing grade.
#Sam is a professor at the university and likes to round each student's  according to these rules:

#If the difference between the  and the next multiple of  is 5 less than 3 , round  up to the next multiple of 5 .
#If the value of  is less than 38 , no rounding occurs as the result will still be a failing grade
#solution:-
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for i in range(0,len(grades)):
        
        if grades[i] < 38:
            continue
        else:
            temp = grades[i]
            te = temp % 5
            if te == 3:
                temp = temp + 2
                grades[i] = temp
            elif te == 4:
                temp = temp + 1
                grades[i] = temp
            else:
                continue
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
