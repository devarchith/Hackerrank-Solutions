#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
 #nput Format

#The first line contains an integer, , the number of students.
#The  subsequent lines describe each student over  lines.
#- The first line contains a student's name.
#- The second line contains their grade.

#Constraints

#There will always be one or more students having the second lowest grade.
#Output Format

#Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
#solution:-
Result =[]
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 

    for a,c in sorted(Result):
        if c==b:
            print(a)
