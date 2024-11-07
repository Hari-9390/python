"""n=int(input("Enter n value: "))
for i in range(1,n+1):
    print('*'*i)"""
    
n=int(input("Enter n value: "))
for i in range(n,0,-1):
    print('*'*i,end="\n")
