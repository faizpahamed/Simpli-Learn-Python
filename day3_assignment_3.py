#print factorial of a give number

print("Enter a number")
try:
    num = int(input())
except:
    print("Invlaid input")
else:
    fact=num
    while num >1:
        num=num-1
        fact = fact * (num)
        
    print("factorial :",fact)
