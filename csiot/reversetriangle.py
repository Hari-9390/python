'''n=int(input("Enter n value: "))
for i in range(1,n+1):
    if i=1:
        sum+=i+2
    print('*'*i,end="\n")


n=5
for i in range(n):
    print(' ' * (n-i-1) + '*' * (2 * i + 1))


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i== n-1 or j==0 or j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
            print()'''



n=10
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()
        
