# Write a program to print numbers from 1 to n. 
# for i in range(1,6):
#     print(i)
# Write a program to print numbers from m to n. Explanation
# for i in range(3,8):
#     print(i)
#Write a program to print numbers in reverse from n to

# for i in range(5, 0, -1):
#     print(i, end=" ")
#Write a program to print numbers from n to m in reverse
# for i in range(11,5,-1):
#     print(i)
#Write a program to calculate the sum of first n natural numbers
# sum=0
# for i in range(1,6):
#     sum+=i
#     print(sum)
# Write a program to find the factorial of a number. 

# sum=0
# for i in range(3,7):
#     sum+=i
#     print(sum)
#Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values
# m=2
# n=4
# sum=1
# for i in range(m,n+1):
#     sum*=i
#     print(sum)
#Write a program to print all factors of a given number
#Write a program to count how many factors a number has
#Check if a number is prime. 
# n=7
# isprime=True
# for i in range(2,n):
#     if(n%i==0):
#         isprime=False
#         break
# if(isprime):
#     print('it is a prime no')
# else:
#     print('it is not prime  no')
#Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. 
# for i in range(3,11):
#     if (i%2==0):
#         print(i) 
#Print all odd numbers between m and n. 
# for i in range(3,11):
#     if (i%2!=0):
#         print(i)
#Count how many even and odd numbers are in the range m to n.
# count1=0
# count2=0
# for i in range(3,8):
#     if (i%2==0):
#         count1+=1
        
#     else:
#         count2+=1
# print('no of even no are:',count1)
# print('no of odd no are:',count2)    
#Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”
# str='hello'
# op=''
# for i in str:
#     op=i+op
# print(op)
#Check if a string is a palindrome. Explanation: Compare 
# x='madam'
# op=''
# for char in range(len(x)-1,-1,-1):
#     op+=x[char]
# print(op)
# if(op==x):
#     print('it is a palidrome')
# else:
#     ('it is not a palidrome')
#Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6
num=123
sum=0
while(num>0):
    ld=num%10
    sum+=ld
    num=num//10
    print(sum)
#Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6
num=123
sum=1
for i in str(num):
    sum*=int(i)
print(sum)




