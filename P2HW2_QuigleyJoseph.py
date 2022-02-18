#CTI-110
#P2HW2 - Score Avg
#Joseph Quigley
#02/18/2022
#average score is score list sum / by 7
#program takes input of scores and finds the minimum score from the list and the average of scores inputted


score_one = float(input('Enter score #1: '))
score_two = float(input('Enter score #2: '))
score_three = float(input('Enter score #3: '))
score_four = float(input('Enter score #4: '))
score_five = float(input('Enter score #5: '))
score_six = float(input('Enter score #6: '))
score_seven = float(input('Enter score #7: '))
 
score_list = [score_one, score_two, score_three, score_four, score_five, score_six, score_seven]
lowest_score = min(score_list)
score_average = float((score_one + score_two + score_three + score_four + score_five + score_six + score_seven) / 7)
print('----------Results---------')
print('Lowest Score  :', lowest_score)
print('Modified List :', score_list)
print('Scores Average :', (f'{score_average:.2f}'))

