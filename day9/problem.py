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
# num=123
# sum=0
# while(num>0):
#     ld=num%10
#     sum+=ld
#     num=num//10
#     print(sum)
#Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6
# num=123
# sum=1
# for i in str(num):
#     sum*=int(i)
# print(sum)

#Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number
# num=int(input('enter a nunber'))
# sum=0
# temp=num
# n=len(str(num))
# for i in range(n):
#     ld=temp%10
#     sum+=ld**n
#     temp=temp//10
# if(sum==num):
#     print('is Armstrong number')
# else:
#     ('is not Armstrong number')
#Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321
# num=123
# rev=0
# while(num>0):
#     ld=num%10
#     print(ld)
#     num=num//10

# num=123
# con=str(num)
# for i in range(len(con)-1,-1,-1):
#     print(con[i],end="")


# num=123
# rev=0
# for i in range(len(str(num))):
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print(rev)
#Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome
# num=121
# rev=0
# while(num>0):
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# if(rev==num):
#     print('it is palindrome number')    
# else:
#     print('it is  not palindrome number')
# : Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. 
# w = 'apple'
# vowels = 'aeiou'
# count = 0

# for chr in w:
#     if chr in vowels:
#         count += 1

# print('number of vowels:', count) 
#Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 

# w = 'apple'
# vowels = 'aeiou'
# count = 0

# for chr in w:
#     if chr not in vowels:
#         count += 1

# print('number of vowels:', count) 
#Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Outpu

# w='apple'
# vowels='aeiou'
# count_v=0
# count_c=0
# for chr in w:
#     if chr in vowels:
#         count_v +=1
#     else:
#         count_c +=1
# print("Number of vowels:", count_v)
# print("Number of consonants:", count_c)
# Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number
# num=28
# sum=0
# for i in range (1,num):
#     if(num%i==0):
#         sum+=i
# if(sum==num):
#     print('it is a perfect number')
# else:
#     print('it is not perfect number')

#Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - Input: 9 - Output: Neon number









