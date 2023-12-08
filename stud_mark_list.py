marklist = [46,47,38,48,20,20,57,37,85,94,39,20,40,20,20,None]
# calculating average
total = 0
# calculat max and min
max_val =marklist[0]
min_val = marklist[0]
# counting absent student
absent_student = 0
# claculating  frequency
freq = {}

for mark in marklist:
    if mark == None :
        absent_student += 1
    else:
        total += mark

        if mark < min_val:
            min_val = mark
        if max_val < mark:
            max_val = mark

        if freq.get(mark) == None:
            freq[mark] = 1
        else:
            freq[mark] += 1
print(f"a. average score of the class = { total /len(marklist)}")
print(f"b. Highest score = {max_val}")
print(f"c. lowest score = {min_val}")
print(f"c. number of absent student = {absent_student}")
highest_freq = 0
highest_freq_mark = 0
for mark in freq:
    if freq[mark] > highest_freq:
        highest_freq = freq[mark]
        highest_freq_mark = mark
print(f"d. Mark with highestfrequency  = {highest_freq_mark}")