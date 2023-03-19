#PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.

#Input Format

#A SINGLE INTEGER DENOTING N VALUE

#Constraints

#1<=N<=100

#Output Format

#PATTERN AS SHOWN IN SAMPLE TEST CASE
#solution:-
n=int(input())
j=""
for i in range(1,n+1):
    j=j+str(i)
    print(" "*(n-i)+j,end="")
    print()
