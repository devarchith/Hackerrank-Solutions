#PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.

#Input Format

#A SINGLE INTEGER DENOTING N VALUE

#Constraints

#1<=N<=100

#Output Format

#PATTERN AS SHOWN IN SAMPLE TEST CASE
#solution:-
y=int(input())
for i in range(1, y + 1):
    for j in range(1, i + 1):
        print(j, end = "")
    print()
