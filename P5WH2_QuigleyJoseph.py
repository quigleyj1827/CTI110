
#Math Quiz - Asks user whether they want to add or subtrack two randomly given integers.
#04/06/2022
#CTI-110 P5HW2 - Math Quiz
#Joseph Quigley
#

import random


print('Welcome to Math Quiz')
print()
print('MAIN MENU')
print('------------------------------------')
def menu_option(): 
    menu_option = ["1. Adding Random Numbers" , "2. Subtracting Random Numbers" , "3. Exit"] 
    print(menu_option[0])
    print(menu_option[1])
    print(menu_option[2])
    menu_choice() 


def random_addition(): 
    proceed = 'y'
    guesses = 1
    integer_one = random.randint(10, 999)
    integer_two = random.randint(10, 999)
    equation_answer = (integer_one + integer_two)
    print(f'{integer_one} + {integer_two}')
    while proceed == 'y':
        student_answer = int(input('Enter answer: '))
        if student_answer == equation_answer:
            print('Congratualtions!!!! Your answer is correct...')
            print('Number of guesses: ',(guesses))
            proceed = 'n'
            menu_choice()
        elif student_answer > equation_answer:
            print('Sorry, guess is too high')
        elif student_answer < equation_answer:
            print('Sorry, guess is too low')
        guesses+=1
         
        
                         

def random_subtraction():
    proceed = 'y'
    guesses = 1
    integer_one = random.randint(10, 999)
    integer_two = random.randint(10, 999)
    equation_answer = (integer_one - integer_two)
    print(f'{integer_one} - {integer_two}')
    while proceed == 'y':
        student_answer = int(input('Enter answer: '))
        if student_answer == equation_answer:
            print('Congratualtions!!!! Your answer is correct...')
            print('Number of guesses: ',(guesses))
            proceed = 'n'
            menu_choice()
        elif student_answer > equation_answer:
            print('Your answer is too high')
        elif student_answer < equation_answer:
            print('Your anser is too low')
        guesses+=1
        
def exit_test():
    print('Thank you for playing...')
    print('Bye!!')


def menu_choice():
    proceed = 'y'
    print()
    while proceed == 'y': 
        user_choice = int(input('Please choose one of the menu options: '))
        if user_choice == 1:
            random_addition()
            proceed = 'n'
        elif user_choice == 2: 
            random_subtraction()
            proceed = 'n'
        elif user_choice == 3: 
            exit_test()
            proceed = 'n'
        else:
            print('Not a valid choice!') 




menu_option()

