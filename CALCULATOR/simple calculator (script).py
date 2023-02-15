a = int (input ("Enter a number:   "))
b = int (input ("Ente another number: "))
c = input ("Which operation do you want to perform (+, -, *, /) ")
if c == '+' :
           print (a,'+', b, '=', a + b)
elif c == '-' :
    print (a, '-', b, '=', a - b)
elif c == '*' :
    print (a, '*', b, '=', a * b)
elif c == '/' :
    print (a, '/', b, '=', a / b)
else :
    print ("You did not enter any operation")
        
 
