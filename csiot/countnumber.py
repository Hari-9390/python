'''n=int(input("Enter n value: "))
num=1
for i in range(n):
    for j in range(i):
        print(num,end=' ')
        num=num+1
    print()


n=int(input("Enter n value: "))
i=1
while i<=n:
    print(i)
    i=i+1

n=int(input("Enter n value: "))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)


base=int(input("Enter base value: "))
exponent=int(input("Enter exponent value: "))
k=1
p=1
while k<=exponent:
    p=p*base
    k=k+1
print(p)

n=int(input("Enter n value: "))'''

n=int(input("Enter n value: "))
count=0
while n>0:
    count=count+1
    n=n//10
print(count)



    
    
