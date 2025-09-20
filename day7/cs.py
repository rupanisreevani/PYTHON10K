def is_even(a):
    if(a%2==0):
        print("even")#even or odd
    else:
        print("odd")    
def add(a,b):#add two no
    print(a+b) 
add(23,65)  
def details(name,pin):#positional arguments
    print(name)
    print(pin)
details(5000,"coders")
def details(name,pin):#keyword arguments
    print(name)
    print(pin)
details(pin=5000,name="sreevani")  
def details(name,batch=35):
    print(name) 
    print(batch)
details("sreevani")  
def items(name,quantity,pice=1000):
    print(f"name:{name},quantity:{quantity},price:{pice}")
items("iphone",1,1005)  
def leapyear (a):#leapyear
    if (a%4==0 and 100!=0 and a%400!= 0):
        print("is a leap year")
    else:
        print("is a not leap year")    
leapyear(2014)
def numbers(a,b):#greatest of two numbers
    if(a>b):
        print("a is greatest number")
    else:
        print("b is greatest number")
numbers(a=6,b=10)        
def age(a):#eligible to vote
    if(a>=18):
        print("he can vote")
    else:
        print("he can't vote")
age(25)
def number(a):
    if(a>0):
        print("The number is positive") 
        
number(34)

def num(a):#divisble by 3
    if(a%3==0):
        print("num is divisble")
num(6)

def num(a):# divisble by 3 and 5
    if(a%3==0 & a%5==0):
        print("divisble")
    else:
        print("not divisble")    
num(8)   

def num(a,b,c): # smallest od three numbers
    if(a<b&b<c):
        print("a is smallest b ")  
    else:
        print("b is smallest c")   
num(5,6,8) 

def year(a): # century year
    if(a%100==0):
        print("year is century")
year(2002)
year(2003)        

def age(age):
    if(age>=60):
        print("senior citzen")
    else:
        print("not senior citizen")    
age(68)  
age(70)