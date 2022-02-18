user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space

userfloat = float(input('Enter float:\n')) 

userchar = input('Enter character:\n') 

userstring = input('Enter string:\n') 

chartoint = chr(user_int) 
print(user_int, userfloat, userchar, userstring)
# FIXME (2): Output the four values in reverse
print(userstring, userchar, userfloat, user_int) 
# FIXME (3): Convert the integer to a characer, and output that character
print(user_int, "converted to a character is", chartoint)