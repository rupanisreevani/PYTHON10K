user_known="frontend"
if(user_known=="frontend"):
    print("user is a frontend developer")
elif(user_known=="bankend" ):
    print ("user is a bankend developer")
elif(user_known=="frontend and bankend"): 
    print("user is a full stack developer")
else:
    print("please go and join 10000 coders")  

ip="123" 
print(type(ip)) #to conver string to integer
op=int(ip)
print(type(op)) 
op=float(ip)  # to conver string to float
num=125
op=str(num)  
print(type(op))
 
seq=[0,2,4,6,8] 
ip=12504
cnvrt=str(ip) 
if(int(cnvrt[-1])in seq ):
    print("even")
else:
    print("odd")   

color="red"  
if(color=="red"):
    print("please stop")
elif(color=="orange"):
    print("ready to go stop")
elif(color=="green"):
    print("please go")
else:
    print("invalid colour input")    
#nested if
is_login=True
user="admin"
if(is_login):
    if(user=="admin"):
        print("welcome to admin")
    elif(user=="clie"):
        print("wellcome to client")    
    else:
        print("unauthorized user")   
else:
     print("go and login") 

seq="02468"   
ip=1257
convrt=str(ip) 
if(cnvrt[-1] in seq):
    print("even")    
else:
    print("odd")


if(num&1==0):
    print("even")
else:
    print("odd")