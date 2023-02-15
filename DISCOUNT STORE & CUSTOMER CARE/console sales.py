print ('           ================================================================')
print ('           |                   15% Discount on our Sales                  |')
print ('           ================================================================')

print ('\n')
print ('1. SODA ($1500)')
print ('2. MILK ($900)')
print ('3. CHIPS ($1000)')
print ('4. BREAD ($2500)')
print ('5. VEGETABLE ($500)')

print ("\nWhat do you want to buy? (You will be given 15% discount)")
a = int (input ("Choose from 1-5:   "))

if a > 5 or a < 1:
    print ("Choose between 1-5")

elif a == 1:
    b = 1500 * 0.15
    print ('\n')
    print (f" The 15% discount price is ${b}")
elif a == 2:
    b = 900 * 0.15
    print ('\n')
    print (f" The 15% discount price is ${b}")
elif a == 3:
    b = 1000 * 0.15
    print ('\n')
    print (f" The 15% discount price is ${b}")
elif a == 4:
    b = 2500 * 0.15
    print ('\n')
    print (f" The 15% discount price is ${b}")
else:
    b = 500 * 0.15
    print ('\n')
    print (f" The 15% discount price is ${b}")

