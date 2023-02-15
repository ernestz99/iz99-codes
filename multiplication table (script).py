#Multiplication table (from 1 to 20)

num = int (input ("Display multiplication table of >>>>> "))

print ("----------------------------------------")

#iterate 20 times from a = 1 to 20
for a in range (1, 21):
    print (num, 'X', a, '=', num * a)
    
print ("----------Program completed-------------")
