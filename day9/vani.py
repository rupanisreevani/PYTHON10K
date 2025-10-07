#sequence of numbers

'''n=4
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end='')
        num+=1
    print()

n=5
for i in range(1,n+1):
    print(""*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print(""*(n-i)+"*"*i)

n=5
for i in range(1,n+1):
    print(" " * (n-i)+" *" * i)


n = 5   # size of diamond

# upper half
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)

# lower half
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "* " * i)'''

#whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even numbe
# a=int(input('enter the value:'))
# if (a %2==0):
#     print('it is even')
# else:
#     print('it is a odd')

#Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy
# a=int(input('enter the value:'))
# if(a%5==0 and a%10!=0):
#     print('value is divisible by 5')
# else:
#     print('not divisible by 10')

#find the biggest number among two
# a=int(input('enter the value:'))
# b=int(input('enter thr value:'))
# if (a>b):
#     print('a is biggest ')
# else:
#     print('b is biggest')
#Find the smallest number among two. Explanation: Use comparison operators (<) to 
# a=int(input('enter the value:'))
# b=int(input('ente the value:'))
# if a<b :
#     print('a is smallest')
# else:
#     print('b is smallest')

#Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: 18
# a=int(input('enter the value:'))
# if( a%2==0 and a%3==0 and a%3==0):
#     print('it is divisible by 2,3,6')
# else:
#     print('it is not divisible by 2,3,6')
#Check if a person is eligible to vote 
# age=int(input('enter the age:'))
# if (age>=18):
#     print('this eligible to vote')
# else:
#     print('not eligible for vote')
# Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Outpu:fail

# maths=int(input('enter the value:'))
# phy=int(input('enter the value:'))
# chem=int(input('enter the value:'))
# if( maths>=35 and phy>=35 and chem>=35):
#     print('pass')
# else:
#     print('fali')
#Check if the student passed at least one subject
# maths=int(input('enter the value:'))
# phy=int(input('enter the value:'))
# chem=int(input('enter the value:'))
# if( maths>=35 or phy>=35 or chem>=35):
#     print('pass')
# else:
#     print('fali')
#Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions 
# maths=int(input('enter the value:'))
# phy=int(input('enter the value:'))
# chem=int(input('enter the value:'))
# if( maths>=35 and phy>=35):
#     print('pass')
# elif(chem>=35 and maths>=35):
#     print('pass')
# else:
#     print('fail')   

#Find the biggest number among three. 
# a=int(input('enter the value:'))
# b=int(input('enter the value:'))
# c=int(input('enter the value:'))
# if(a>b and b>c):
#     print('a is biggest')
# elif(b>c and c>a):
#     print('b is biggest')
# else:
#     print('c is biggest')
#Find the smallest number among three. 

# a=int(input('enter the value:'))
# b=int(input('enter the value:'))
# c=int(input('enter the value:'))
# if(a<b and b<c):
#     print('a is smallest')
# elif(b<c and c<a):
#     print('b is smallest')
# else:
#     print('c is smallest')
#Check if a number is a perfect square. Explanation: A number is a perfect square if the 
# n=25
# isperfert=False
# for i in range(1,n):
#     if(i**2==n):
#         isperfert=True
#         break
# if (isperfert):
#     print('is a perfect no ')
# else:
#     print('is not perfert no')
#Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4
# m=30
# if (m%5==0):
#     print('m//5')
# else:
#     print('m//5+1')
#Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - 
# a=int(input('entre the value:'))
# b=int(input('enter the value:'))
# c=int(input('enter the value:'))
# if(a<=b and c<=a and a<=c and a>=b):
#     print(f'{a}is second biggest no')
# elif(b<=c and b>=a and b<=a and b>=c):
#     print(f'{b}is second biggest no')
# else:
#     print(f'{c}is second biggest no')


#Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
# a=int(input('enter the value:'))
# if(a%4==0 and 100!=0 and a%400!=0):
#     print('is leap year')
# else:
#     print('is not leap year')




