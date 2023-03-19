#PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.

#Input Format

#A SINGLE INTEGER DENOTING N VALUE
#Constraints

#1<=N<=100

#Output Format

#PATTERN AS SHOWN IN SAMPLE TEST CASE
#solution:-
rows = int(input())
count=0
for row in range(1, rows+1):
    for column in range(1, row + 1):
        if((row+column)%2==0):
            print(1, end='')
        else:
            print(0, end='')
    print('')
