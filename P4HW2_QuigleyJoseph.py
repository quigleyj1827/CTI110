#Pizza Quantity Calculator
#3/21/2022
#CTI-110 P4HW2 – Pizza Order
#Joseph Quigley
#Program calculates the amount of pizzas to order for inputted amt of students if students get 3 slices each and each pizza has 6 slices
# pizzas_needed will be students / (1.5, 2, or 3)
#Price of pizzas is $5 with 6% tax

def main():
    
    print('How many students do you want to order pizza for?', end=' ')
    students = int(input())
    print('Enter number of people per pizza ( 1.5, 2 or 3) :', end=' ')
    people_per_pizza = float(input())

    sharer = [1.5, 2, 3]
# while loop executes if user input is not with in list    
    while people_per_pizza not in [1.5, 2, 3]:
        print('Invalid Entry !')
        print('Should have entered 1.5, 2 or 3') 
        print('Enter number of people per pizza again ( 1.5, 2 or 3) :', end=' ')
        people_per_pizza = float(input())         
       
# calculate amount of pizzas needed based on inputted number of students and per pizza      
    if people_per_pizza == 1.5:
        pizzas_needed = students / people_per_pizza
    elif people_per_pizza == 2:
        pizzas_needed = students / people_per_pizza
    elif people_per_pizza == 3:
        pizzas_needed = students / people_per_pizza    
  
    cost_per_pizza = 5.00
    sub_total = float(cost_per_pizza * pizzas_needed)
    taxed_total = float(sub_total * 0.06)
    total = sub_total + taxed_total

    print('----Pizza Order--------')
    print('Number of Students :', students)
    print(f'Pizzas Needed :', round(pizzas_needed))
    print(f'Price $, {total:.2f}')

    restart = input('Would you like to run program again (y for yes): ')
    if restart == 'y':
        main()
    else:
        exit()
main()
