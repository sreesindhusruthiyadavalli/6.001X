# Paste your code into this box
num = int(raw_input("Please think number between 0 and 100!"))
low = 0
high = 100
ans = ((low + high)/2)
print ("Is your secret number" + str(ans)+ "?")
user_input = raw_input("Enter h for high ,l for low and c for correct")
if (user_input != 'h' or user_input != 'l' or user_input != 'c'):
    print ("Enter the valid input for the computer guess")
elif(user_input == 'h'):
    high = ans
    ans = (low + high)/2
