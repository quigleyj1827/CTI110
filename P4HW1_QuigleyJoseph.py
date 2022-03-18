#CTI-110
#P4HW1 - Score List
#Joseph Quigley
#02/18/2022

grades = []
#Loop to get number of scores
number_of_scores = int(input("How many scores to you want to enter? "))
for i in range(1, number_of_scores+1):
    grade = float(input("Enter score # " + str(i) +" :"))
    while grade > 100 or grade < 0:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        print('Enter score #', str(i))
        grade = int(input("Enter score # " + str(i) +" again:"))
    grades.append(grade)
#calculate average and lowest score
avg = sum(grades)/len(grades)
lowest_score = min(grades)
grades.remove(lowest_score)

#Grade scale

letter =""
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >=70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"


#Calculate final letter grade
print('----------Results----------')
print('Lowest Score  :', lowest_score)
print('Modified List :', grades)
print('Scores Average:', (f'{avg:.2f}'))
print('Grade    :', grade)
