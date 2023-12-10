def ternarySearch(arr, l, r, x):
    # Check if the student is present at mid
    if (r >= l):

        mid1 = l + (r - l) // 3
        mid2 = mid1 + (r - l) // 3

        # If student is present at mid1
        if (arr[mid1] == x):
            return mid1

            # If student is present at mid2
        if (arr[mid2] == x):
            return mid2

            # If student is present in left one-third
        if (arr[mid1] > x):
            return ternarySearch(arr, l, mid1 - 1, x)

            # If student is present in right one-third
        if (arr[mid2] < x):
            return ternarySearch(arr, mid2 + 1, r, x)

            # If student is present in middle one-third
        return ternarySearch(arr, mid1 + 1, mid2 - 1, x)

    return -1


def get_input(arr):
    size = int(input("enter the number of students : "))
    for i in range(0, size):
        element = int(input(f"enter the roll number of {i + 1} Student : "))
        arr.append(element)


def sort(arr):
    length = len(arr)
    for i in range(length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    print(arr)


arr = []

flag = 1

while (flag == 1):
    print("<----------------Menu----------------->")
    print("1.accept roll numbers of Students")
    print("2.display list of Students in list")
    print("3.Ternary Search")
    print("4.Sort the list")
    print("5.exit")
    print("<------------------------------------->")

    choice = int(input("enter your choice : "))

    if (choice == 1):
        get_input(arr)
        n = len(arr)
        print()
    elif (choice == 2):
        print(f"roll number in list are {arr}")
        print()
    elif (choice == 3):
        x = int(input("enter the roll number to search : "))
        result = ternarySearch(arr, 0, n - 1, x)
        if (result == -1):
            print("Student is not a member of the club")
            print()
        else:
            print("Student is a member of the club")
            print()
    elif (choice == 4):
        sort(arr)
        print()
    elif (choice == 5):
        flag = 0
    else:
        flag = 0