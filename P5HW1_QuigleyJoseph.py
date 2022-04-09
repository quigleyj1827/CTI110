#Program takes input to collect scores and displays average, lowest score and letter grade.
#04/08/2022
#CTI-110 P5HW1 - Score List
#Joseph Quigley
#

# Menu function for user to select option

def display_menu():
    print('----------------MENU----------------')
    print(' 1) Create Score List')
    print(' 2) Display Results')
    print(' 3) Exit')
    x = int(input())
    while x != 3:    # This loop will repeat until user ends program     
        if x == 1:
            get_score()
        elif x == 2:
            eval_grade()
        elif x != ('1', '2'):
            print('Please select 1, 2, or 3')
        elif x == 3:
            print('Goodbye!!!')
           
        print('----------------MENU----------------')
        print(' 1) Create Score List')
        print(' 2) Display Results')
        print(' 3) Exit')
        x = int(input())
       
   

grades = []

def get_score(): # Function to get scores from user
    number_of_scores = int(input("How many scores to you want to enter? "))
    for i in range(1, number_of_scores+1):
        grade = float(input("Enter score # " + str(i) +" :"))
        while grade > 100 or grade < 0: #This loop ensures that correct grades are entered
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            print('Enter score #', str(i))
            grade = int(input("Enter score # " + str(i) +" again:"))
        grades.append(grade)

#get_score()
#display_menu()



def eval_grade(): # Function to convert entered grades to letter grade, get average, find lowest score and remove. 
    while len(grades) == 0:
        print('Create Score List First!!')
        display_menu()
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
     
    print('----------Results----------')
    print('Lowest Score  :', lowest_score)
    print('Modified List :', grades)
    print('Scores Average:', (f'{avg:.2f}'))
    print('Grade    :', grade)
    display_menu()
#eval_grade()
#display_menu
def main():
    display_menu()


main()




