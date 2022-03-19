print("Enter a number:")
try:
    num = int(input())
except:
    print("invalid input")
else:    
    if(num==1):
        print("ONE")
    elif(num==2):
        print("TWO")
    elif(num==3):
        print("THREE")
    else:
        print("invalid number")
