#CTI-110
#P4LAB1 Count input length without spaces, periods, exlamation points, or commas
#Joseph Quigley
#3/09/2022
#Uses for loop to count length of user input
user_text = input()

count = 0
for x in user_text:
    if not(x in " .,! "):
        count += 1
print(count)
