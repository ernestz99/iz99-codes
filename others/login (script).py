print ("\t\t\tMEMBER LOGIN")
a = ['zeal' , 'ernest', 'tel', 'musiala']
b = ['zea123' , 'ern123', 'tel123', 'mus123']
d = input ("Enter your username: ")
e = input ("Enter your password: ")
print ('\n')
if d in a and e in b:
    print ('login successful')
elif d not in a and e not in b :
    print ('lol. access denied')
elif d not in a :
    print ('invalid username')
else :
    print ('invalid password')



