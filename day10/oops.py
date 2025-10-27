# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def engine_start(self):
#         print(f'{self.model} of {self.brand} has started')

#     def engine_stop(self):
#         print(f'{self.model} has stopped')

# obj1 = Vehicle("KTM", "Classical 250")
# obj1.engine_start()
# obj1.engine_stop()
# encapsulatoin
# class BankAccount:
#     def _init_(self, name, balance):
#           self._name=name
#           self._balance=balance

#           def getBalance(self):
#                 print(f'your current balance is:{self.__balance}')
#                 def deposite(self, amount):
#                       if amount>0:
#                             self.__balance+=amount
#                             print(f'{amount} has been credited to your account')
#                             print(f'your new balance is:{self.__balance}')
#                       else:
#                             print('Invalid ammount')

#                 def withdraw(self, amount):
#                       if 0<amount<self.__balance:
#                             self.__balance-=amount
#                             print(f'{amount} has been debited from your account')
#                             print(f'your current balance is:{self.__balance}')
#                       else:
#                             print('Insufficient Balance')

# customer1=BankAccount('Apoorva', 50000)
# customer1.getBalance()
# customer1.deposite(150000)
# customer1.withdraw(20000)


# #polymorphism
#function with same name performing differently based on classes and objects
#1.duck typing
#if it walks like a duck and quacks like a duck then it is a duck
#ia an object has certain features then it is considered
# class Dog:
#     def speak(self):
#         print('dog barks')
#     def walk(self):
#         print("dog walks")
# class cat:
#     def speak(self):
#         print('cat meows')
#     def walk(self):
#         print("cat walks")

# class human:
#     def speak(self):
#         print('man talks')
#     def walk(self):
#         print("man walks")
# def checking(obj):
#     obj.speak()
#     obj.walk
#     print('then it is a man')
# dog1=Dog()
# cat1=cat()
# man1=human
# checking(dog1)



#2.method overriding without inheritance

# class father:
#     def work( self):
#         print('he does work to provide his family')
# class mother:
#     def work(self):
#         print('she is takes care of family')

# father1=father()
# mother1=mother()
# father1.work()
# mother1.work()
# #method overriding with inheritance
# class vehicle:
#     def start(self):
#         print('vehicle started')
# class car(vehicle):
#     def start(self):
#     print('car started')
# car1=car()
# car1.start()


#3.method overloading simulating method overloading using default arguments

class math:
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d

m1=math()
print(m1.add(3))

#4.opertor overloading
class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,otherbook):
        return self.pages+otherbook.pages

book1=book(250)
book2=book(300)
print(book1+book2)