#check if number is even or odd.

print("Enter a number")
try:
    num = int(input())
except:
    print("Invlaid input")
else:
    if(num%2==0):
        print("Even")
    else:
        print("Odd")
