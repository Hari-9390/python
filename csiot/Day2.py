x=int(input("Enter the units used: "))
Amount= 120
if 50<x<100:
    Amount+=(x-50)*2.89
elif 100<=x<150:
    Amount+=289+(x-100)*3.83
elif 150<=x<200:
    Amount+=289+383+(x-150)*4.89
elif 200<=x<300:
    Amount+=289+383+489+(x-200)*5.34
elif 300<=x<400:
    Amount+=289+383+489+534+(x-300)*4.99
elif 400<=x<500:
    Amount+=289+383+489+534+499+(x-400)*6.89
elif 500<=x<750:
    Amount+=289+383+489+534+499+689+(x-500)*7.56
elif 750<=x:
    Amount+=289+383+489+534+499+689+756+(x-750)*8.73
print(Amount)



a=int(input())
b=int(input())
c=int(input())
if a==b!=c or a!=b==c or c!=a==b:
    print("it is a isoceles triangle")
elif a==b==c:
    print("it is a equilateral")
elif a!=b!=c:
    print("it is a scalar ")
else:
    print("bye")






n=int(input("enter marks"))
if 0 <= marks <= 100:
    if marks >= 90:
        grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    print("Invalid marks. Please enter a value between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")




acc_bal = 100000000000
operation = input("Enter w for withdraw , d for deposit")

if operation == "w" or "W":
    amount = int(input("Enter the amount"))
    if acc_bal<amount:
        print("Insufficient funds")
    else:
        acc_bal-=amount
elif operation == "d" or "D":
    amount = int(input())
    acc_bal+=amount
else:
    print("Enter valid operation")
print(acc_bal)
