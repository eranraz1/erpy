first_name = 'Eran'
last_name = 'Raz'
welcome_message = f'Welcome {first_name} & {last_name}'
print(welcome_message) 
e =  first_name[1:3]
#first_name[1] = "w"   #string isImmutability
print(e)
print(10 < 9) 
list1 = ['pen','toothbrush', 'sanitizer','eraser']
print(list1[1])
list1[1] = 'koko'
print(list1)
# rev_ord = list1[:-2] # cut from the other side
rev_ord = list1[::-1] #        REORDER  LIST !!!!!!!
print(rev_ord)

matrix_2 = [[1,3,9], [1,4,2], [2,4,4], [2,3,5]]
print (matrix_2[2][2])
matrix_2.append([1,2,4,4]) 
print (matrix_2)
matrix_2.insert(2,9)
matrix_2.extend('10Z123')  # Extend takes an iterable (loopable items) and adds to end of list
print (matrix_2)
matrix_2.pop()
matrix_2.remove('Z') 
print (matrix_2)
#matrix_2.clear()
print (matrix_2.count('1')) # get location of value
print (matrix_2.index([2, 3, 5])) # get location of value

#Some common list patterns
cloned_mat = matrix_2[::1] # Clone> duplicate
print(cloned_mat)
make_str = ''.join(rev_ord) # turn to string 
print (make_str)
new_list =  (list(range(2,11,2))) # generate list 
print(new_list)
a,b,c,d,e = new_list # unpack a list 
f,*other = new_list # unpack a list- till the end
print ('other: {}'.format(other))
# None= Null

# Dictionaries - have no order
user = {
    'name': 'Maxim',
    'age': 40,
    'married': True, 
    'kids': 4
    }
print(user.get('age1','default')) # get function to avoid error : None or default
print('name' in user.keys()) # check key
print( 4 in user.values())  # check value
user_copy = user.copy()
print (user_copy)
user_copy.pop('age') #user_copy.clear()
user_copy.update({'pet':'Dog'})
user_copy.update({'age':45})
print (user_copy)

#  Tuples - same function as list

colors = ('red', 'orange', 'blue', 'yellow')
print (colors[2])
print(colors.count('orange'))

#   Sets
new_set = {1,2,3,4,5,5,5,6,6} # only unique
list2 = [1,2,3,4,5,5,5,6,6]
print(list2)
list2 = set(list2)    #         remove duplicates
print(list2)

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
print(set_a.union(set_b))
print(set_a | set_b) # same as above just a compact syntax
print(set_a.intersection(set_b))
set_a.discard(3)
print(set_a)

############################################################
#   LOGIC
############################################################
# www = input('Please enter your age: ')
# if(int(www  ) <= 18):
#     age_d =  'too young'
# elif (int(www) > 18 and int(www) < 50):
#     age_d = 'perfect age'
# else:
#     age_d = 'too old'
#     print (age_d)

username = '' # bool('santa') => True
password = 'superSecretPassword' # bool('superSecretPassword') => True
if username and password:
  print('Details found')
else:
  print('Not found')

is_single = 1
msg = 'you are OK' if is_single else 'you are NOT OK'
print(msg)

#   == convert types
print(10 == 10.0) # True
print(10 is 10.0) # False -  checks for the value as well as their memory locations

for i in 'Python':
    print(i)
for item in {1,2,3,4,5}: # Set is iterable
    print(item)
#                    loop DICT
for i in user:
    print (i)
for i in user.keys():
    print (i)
for i in user.values():
    print (i)
for i in user.items():
    print (i)

for x,y in user.items():
    print (y,x)
for i in range(10,0,-2):
    print(i)
print(list(range(40,10,-5)))

#   enumerate - create range with keys
for x, y in enumerate(range(5,50,4)):
    print(f'key x is {x} and value {y}')
i=0
while i<10:
   print (i)
   i +=2
else:
    print('end')
'''
while 1==1:
    text = input('set input: ')
    if text == 'x':
        break
''' 

print('-----------------------')
for elm in set_b:
    if elm <= 5:
        pass
    else:
        print(elm)
print('-----------------------')
for elm in set_b:
    if elm <= 5:
        continue
    print('1')

###  print duplicates
email_list = ['roger@hey.com','michael@hey.com','roger@hey.com','prince@gmail.com']
email_list.sort()

for i in range(1,len(email_list)):
    if email_list[i] !=  email_list[i-1]: 
        pass
    else:
        print (email_list[i])

#  functions
def blower(name, emoji): # parameters
  print(f'{name} {emoji} {emoji} {emoji}')

blower('fire', '🔥') # arguments
blower('water', '🌊')        

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)
print (times5(2))

def prirnto(*args):
    print (args)
prirnto(1,2,3,4,5,'aBA')                    # --> Returns a tuple

def superfunc (**kwargs):
    print (kwargs)
print(superfunc(f='sami',l='susu',c='daa'))  #  --> Returns a dict

# OOP
class Hero:
    def __init__ (self,name, weapon,age):
        if age >=18:
            self.name = name
            self.weapon = weapon
            self.age= age

    def fight (self):
        return self.weapon

spider = Hero('spiderman','gun',18)
print(spider.fight())

#Coding Exercise - soccer
class SoccerPlayer:
    def __init__(self, name, goals):
        self.name = name
        self.goals = goals
    def calc2 (self):
        print(f'No of goals is: {self.goals}')
      
    @classmethod                        #decorator @classmethod on top of the method name
    def calc_goals(cls,num1,num2):
        return num1*num2

    @staticmethod                      ##decorator @classmethod on top of the method name, doesnt return anything - cls
    def multiply(num1, num2): 
                return num1 * num2
            # cls is just like self which needs to passed as 1st parameter

print(SoccerPlayer.calc_goals(2,3))  # class method
print(SoccerPlayer.multiply(3,5)) # 15


def calc_max_goals(*args):
    print (max(args))
    return max(args)



Players=['Eran','Adi','Daniel']
Players[0] = SoccerPlayer('Eran',30)
Players[1] = SoccerPlayer('Adi',56)
Players[2] = SoccerPlayer('Daniel', 57)

Players[2].calc2()

calc_max_goals(Players[0].goals,Players[1].goals,Players[2].goals)

#  Inheritance

class PlayerQ:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight

  def a_w (self):
        return self.age * self.weight
playerq1 = PlayerQ('Momi',18,70)
print(f'The result is: {playerq1.a_w()}')

class duplicateClass(PlayerQ):
    def shot(self):
        print (f'Shot {self.name}')
playerq2= duplicateClass('Sami',15,72)
print(playerq2.shot())
print(isinstance(playerq2,duplicateClass))   # check is instance
#playerq2.duplicateClass.shot()

##############  Polymorphism - Poly means many and morphism means form
class condi:
    def __init__ (self,numb):
       self.numb = numb 
    def cond(self):
       return self.numb*2
x= condi(3)
print(x.cond())

class Employee:
  def __init__(self, name):
    self.name = name
    print(f'{self.name} is an employee')
class Manager(Employee):
  def __init__(self, department, name):
    self.department = department
    self.name = name
    super().__init__(name)
    print(f'{self.name} is the Manager, {self.department} department')
man1 = Employee('jole')
man2 = Manager('IT','Dambo')
print(dir(man2))

#             MAP
numbers = [1,2,3,4,5]
def multi_by5(num):
    return num*5

result1= map(multi_by5,numbers)
print (list(result1))

#     filter

colors = ['blue', 'green', 'black', 'red']

def remove_color(i):
    return i != 'red'

left_color = filter(remove_color,colors)
print (list(left_color))

#            ZIP
emails = ['alan@gmail.com', 'ross@gmail.com']
usernames = ['alan', 'ross']
users= dict(zip(usernames, emails))
print (users)

#           reduce()
from functools import reduce
numbers = [12,2,3,4]
def sum_(x,y):
    return y+x
reduce_ = reduce(sum_, numbers,0)
print  (reduce_)

# Lambda   ********* more exesice !!!
names = ['John', 'Peter', 'Elon', 'Joseph']
# make all names upper cased
upper_cased = list(map(lambda name: str.upper(name)+'_A', names))

print(upper_cased)

multiply = lambda x,y : x*y
print(multiply(4,3))

dividxy = lambda x,y: x/y
print (dividxy(3,2))

numbers =[[34, 63, 88, 71, 29],
[90, 78, 51, 27, 45],
[63, 37, 85, 46, 22],
[51, 22, 34, 11, 18]] 

mean = lambda x: sum(x)/len(x ) 
average = list(map(mean, numbers)) 
print(average)

users = [('Mary', 23), ('Emilie', 10), ('Katie', 30)]
print(sorted(users))  # sorted by users
sort_by_age = sorted(users,key =lambda item: item[1] )
print(sort_by_age)

scores = [23, 55, 20, 90, 34, 53]
score_under_50 = list(filter(lambda x: x<50, scores))
print(score_under_50)

#                Comprehensions
#List Comprehension

print([i*2 for i in range(10)])
print([i-1 for i in range(2,10,2)])

numbers = [2,34,23,53,34,12,22,89]
even_numbers = [i for i in numbers if i%2 ==0]
print(even_numbers)

# dict  Comprehension
attendance = {
    'John': True,
    'David': False,
    'Nick': True,
    'Tom': False,
    'Marie': False,
    'Nancy': True
}
student_present = [key for key, value in attendance.items() if value == True]
print(student_present)

names = [
    'Harry', 'Johnny', 'Lewis', 'Harry', 'Buck', 'Nick', 'David', 'Harry',
    'Lewis', 'Michael']
names = set(names)
names= list(names)
print(names)
print(len(names))


def sum(num1, num2):
    return num1 + num2
def logger (func,args):
    return func(*args)*1.1
log_=logger(sum, (1, 5))

print (f' the func result is: {log_}')



def random(): # Higher order function
  def special():
    print('I am something special')
  return special
  random()() # I am something special
#-------------------------------------------------------------------

def starmaker(func):
    def wrapper():
        func()
        print('You are a star now!')
        print('*********') 
    return wrapper

@starmaker #decorator
def layman():
  print('I am just a layman')

#starmaker(layman)() # This is the underlying decorator magic!
layman()

# Genetators

def my_infinite_generator(max):
  num = 0
  f=1
  while num < max:
    yield num
    num +=1


result = my_infinite_generator(6)
print(next(result)) # 0
print(next(result)) # 1
print(next(result)) # 2
print(next(result)) # 3
print(next(result)) # 4
print(next(result))
# print(next(result))

def fibonacci_generator(num):
  a,b = 0,1
  for item in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

for num in fibonacci_generator(20):
  print(num)

# Fibonacci sequence squared
def fibonacci_generator(num):
  a,b = 0,1
  for item in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

def square(nums):
  for num in nums:
    yield num**2

result = square(fibonacci_generator(5))

for num in result:
  print(num) # 0 1 1 4 9

#                                        Request module
# import requests
# from bs4 import BeautifulSoup
 
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text)
 
# for story_heading in soup.find_all(class_="story-heading"): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())


''' links:
https://realpython.com/primer-on-python-decorators/#returning-functions-from-functions
https://www.programiz.com/python-programming/decorator
'''
#https://dev.to/arindamdawn/30-days-of-python-day-18-file-i-o-3jmb