Exp-1:

x=int(input("Enter a positive number"))
sum=0
tmp=x
if(x>0):
    for i in range(len(str(x))):
        z=tmp%10
        y=pow(z,len(str(x)))
        tmp//=10
        sum+=y
    if(sum==x):
        print("x is a armstrong number")
    else:
        print("x is not a armstrong number")
else:
    print("Number is invalid")

Exp-2:

x=int(input("Enter a number"))
sum=0
n=x
while x>0:
    z=n%10
    sum=sum+10*z
    n//=10
if sum==x:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")

Exp-3:

x=int(input("Enter number"))
n=x
sum=0
for i in range(len(str(x))):
    z=n%10
    sum+=z
    n//=10
print(sum)



