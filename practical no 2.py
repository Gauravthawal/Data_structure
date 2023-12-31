# The average score of class
def average(l):
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i] != -999:
            sum += l[i]
            cnt += 1
    avg = sum / cnt
    print("Total Marks are : ", sum)
    print("Average Marks are : {:.2f}".format(avg))


# Highest score in the class

def Maximum(l):
    Max = l[0]
    for i in range(len(l)):
        if l[i] > Max:
            Max = l[i]
    return (Max)


# Lowest score in the class

def Minimum(l):
    Min = l[0]
    for i in range(len(l)):
        if l[i] != -999:
            if l[i] < Min:
                Min = l[i]
    return (Min)


# Count of students who were absent for the test

def absentCnt(l):
    cnt = 0
    for i in range(len(l)):
        if l[i] == -999:
            cnt += 1
    return (cnt)


# Display mark with highest frequency

def maxFrequency(l):
    i = 0
    Max = 0
    print(" Marks ----> frequency count ")
    for ele in l:
        if l.index(ele) == i:
            print(ele, "---->", l.count(ele))
            if l.count(ele) > Max:
                Max = l.count(ele)
                mark = ele
                i += 1
    return (mark, Max)


# Input the number of students and their corresponding marks in FDS

marksInFDS = []
noStudents = int(input("Enter total number of students : "))
for i in range(noStudents):
    marks = int(input("Enter marks of Student " + str(i + 1) + " : "))
    marksInFDS.append(marks)
flag = 1

while flag == 1:
    print("/************MENU*************/")
    print("1. The average score of class ")
    print("2. Highest score and lowest score of class ")
    print("3. Count of students who were absent for the test ")
    print("4. Display mark with highest frequency ")
    print("5. Exit ")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        average(marksInFDS)
        print("\n")
    elif choice == 2:
        print("Highest score in the class is : ", Maximum(marksInFDS))
        print("Lowest score in the class is : ", Minimum(marksInFDS))
        print("\n")
    elif choice == 3:
        print("Count of students who were absent for the test is : ", absentCnt(marksInFDS))
        print("\n")
    elif choice == 4:
        mark, count = maxFrequency(marksInFDS)
        print("Highest frequency of marks {0} is {1} ".format(mark, count))
    else:
        print("Wrong choice")
        flag = 0