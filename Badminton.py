#Eperiment-1 input code


def cricket_and_badminton():  # Function to compute the list of students who play both cricket and badminton
    cricket_players = ['Alice', 'Bob', 'Charlie', 'David']
    badminton_players = ['Alice', 'Bob', 'Emily', 'Frank']

    both = []  # Initialize an empty list to store the names of students who play both cricket and badminton

    for student in cricket_players:
        if student in badminton_players:
            both.append(student)

    return both


def cricket_or_badminton():  # Function to compute the list of students who play either cricket or badminton but not both
    cricket_players = ['Alice', 'Bob', 'Charlie', 'David']
    badminton_players = ['Alice', 'Bob', 'Emily', 'Frank']

    either = []  # Initialize an empty list to store the names of students who play either cricket or badminton but not both

    for student in cricket_players:
        if student not in badminton_players:
            either.append(student)

    for student in badminton_players:
        if student not in cricket_players:
            either.append(student)

    return either


def neither_cricket_nor_badminton():  # Function to compute the number of students who play neither cricket nor badminton
    cricket_players = ['Alice', 'Bob', 'Charlie', 'David']
    badminton_players = ['Alice', 'Bob', 'Emily', 'Frank']

    all_students = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'George', 'Harry', 'Ian', 'Jack']

    neither = 0  # Initialize a counter to count the number of students who play neither cricket nor badminton

    for student in all_students:
        if student not in cricket_players and student not in badminton_players:
            neither += 1

    return neither


def cricket_and_football():  # Function to compute the number of students who play cricket and football but not badminton
    cricket_players = ['Alice', 'Bob', 'Charlie', 'David']
    football_players = ['Bob', 'Charlie', 'David', 'Kevin']
    badminton_players = ['Alice', 'Bob', 'Emily', 'Frank']

    cricket_and_football = []  # Initialize an empty list to store the names of students who play both cricket and football

    for student in cricket_players:
        if student in football_players and student not in badminton_players:
            cricket_and_football.append(student)

    return len(cricket_and_football)


# Print the results
print("List of students who play both cricket and badminton:", cricket_and_badminton())
print("List of students who play either cricket or badminton but not both:", cricket_or_badminton())
print("Number of students who play neither cricket nor badminton:", neither_cricket_nor_badminton())
print("Number of students who play cricket and football but not badminton:", cricket_and_football())
