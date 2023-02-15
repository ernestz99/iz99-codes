print ('           ================================================================')
print ('           |                      CUSTOMER CARE SERVICE                   |')
print ('           ================================================================')


def all():
    print ('\n')
    print ('1. Call Us')
    print ('2. Chat US')
    print ('3. Send An Email')
    print ('4. FAQs')

    print ("\n")
    a = int (input ("Choose from 1-4:   "))

    if a > 4 or a < 1:
        print ('================================================================')
        print ("\nChoose between 1-4")
        all()
    elif a == 1:
        print ('\n')
        print ('''Hi, Let's help you today.
Phones lines are available between 8:00 AM and 5:00 PM on weekdays.
CALL 091000C247MiNiSTORE''')
        print ('\n')
    elif a == 2:
        print ('\n')
        print ('''ZEE: Hi there!
Thanks for getting in touch.
How can i help you?''')
        b = input("YOU: ")
        print(f'''\nYOUR COMPLAINT: ( {b}.........) is received
We will get back to you
Ciao!!!''')
        print ('\n')
    elif a == 3:
        print ('\n')
        print ('''Hi, Let's help you today.
Send us a mail through the Store mail below 
\nministores247@gmail.com''')
        print ('\n')
    else:
        print ('\n')
        print ("Loading...........")
        print ('\n')

all()