def add(*numbers):#add two numbers
    print(sum(numbers))
add(1,2,3,4,5)   

def stationart(*price):#price and len
    print(len(price))
    print(sum(price))
stationart(5,5,30,50) 

def details(*details):#*keyword arguments
    print(details) 
details(name="sreevani",batch=53,couse="python") 

def details(*details,batch=53):
    print(batch)
    print(details)
details("sreevani",10,"python")