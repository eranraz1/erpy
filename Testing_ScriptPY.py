import timeit
'''
Ask the user for a number. Depending on whether the number is even or odd,
 print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
 If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

# num = int(input('please set num: '))
# check = int(input('please set check: '))

# def check_even(num,check):
#     if num % 4 ==0:
#         return 'multiple of 4 - finished'
#     else:
#         if num % check ==0:
#             return 'check is even'
#         else:
#             return 'check is not even'

# print (check_even(num,check))



'''
and write a program that prints out all the elements of the list that are less than 5.
'''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]

# for i in a:
#     if i<5:
#         print(i)
# b = []
# for i in a:
#     if i<5:
#         b.append(i)
# print (b)

# #filter
# def under_5(i):
#     if i<=5 :
#         return i

# left5_list = filter(under_5,a)

# print (list(left5_list))


# tnum = int(input('please set some num: '))
# num_list=[]
# for i in range (2,tnum+1):
#     if tnum%i ==0:
#         num_list.append(i)
# print (list(num_list))

'''
List Overlap
'''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# print(set(a).union(set(b)))

# for i in b:
#     if i not in a:
#         a.append(i)
# print(a)

'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''

check_string = 'abcdeqhedcba'
print (len(check_string))
#print (int(len(check_string)/2))
str_start = check_string[0:int(len(check_string)/2)]
str_end = check_string[int(len(check_string)/2):]

if len (check_string)%2 >0:
    print ('not palindrome')
else:
    for i in range(int(len(check_string)/2)):
        if str_start[0+i] != str_end[-1-i]:
            print('not palindrome')
            break
        else:
            if (i+1 == int(len(check_string)/2)):
                print('palindrome')
            else:
                continue




str_end_rev  = str_end[::-1]  # REVERSED STRING  ***
print(str_end_rev)
str_end_rev
if  str_end_rev == str_start:
    print('palindrome')
else:
    print('not palindrome')

def palind():
    return check_string[::] == check_string[::-1]
print(palind())
  #  print(str_start[0+1])
   # print(str_end[-1-1])

'''
 new list that has only the even elements of this list in it.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [i for i in a if i%2==0]
print(even)

'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
 compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
 
input1 = 'Rock'
input2 = 'Paper'
game_dict = {'Rock':0,'Paper':1,'Scissors':2}

print(dict(game_dict))
#print(game_dict[input2])
a =  'y'
while a == 'y':
    if game_dict[input1] > game_dict[input2]:
        a= 'input1 wins'
        
    elif game_dict[input1] < game_dict[input2]:
        a= 'input2 wins'
    else:
        a= input('whant new game (y/n?')
print(a)

'''
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#allproducts = [a*b for a in x for b in y]

comm_products = [i for i in set(b) if i in set(a) ]
print(list(comm_products))



#Ask the user for a number and determine whether the number is prime or not
num_check= 55
div_list = [2,3,5,7]
#exclude from list
div_list_d = [i for i in div_list if i != num_check]
#print(list(div_list_d))
#def check_prime(num_check):
t_list = [i for i in div_list_d if num_check%int(i)==0] 
if(len(t_list)) == 0:
    print('Prime')
else:
    print('Not Prime')
     


# while 1==1:
#     p= input("Enter a number to check. Ctl-C to exit.")
   
    
    # num div% list > 1


'''
List Ends 
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''
a = [5, 10, 15, 20, 25 , 35, 22]
#b= [a[0],a[-1]]


def statend_list(l):
     return l[0],l[-1],99
    
b =  [statend_list(a)]       
print(list(b))

#-------------------------------------


def fibo1(num):
    a = 1 
    b = 1
    if num == 0:
        fibonnaci = []
        #print(list(fibonnaci))
    elif num == 1:
        fibonnaci = [1]
        #print(list(fibonnaci))
    elif num == 2:
        fibonnaci = [1,1]
        #print(list(fibonnaci))
    elif num > 2:
        fibonnaci = [1,1]
        for i in range (2,num):
            c = b + a
            print(c)
            fibonnaci.append(c)
            a = b
            b = c
        #print(list(fibonnaci))
    return fibonnaci
#go  = int(input("please set num for fibonnaci"))
go =10
print(fibo1(go))

#-------------------------------------
fib = [1,1]
for n in range(2,11):
    if n < 1:
        n=2
    fib.append(fib[n-1] + fib[n-2])
print(list(fib))

'''
Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.
'''
lista = [1, 1, 2, 3, 5, 8, 13, 21, 55, 55, 99, 99]
def no_dup(ls):
    b = []
    for num in ls:
        if num not in b:
            b.append(num)
    return b
print (no_dup(lista))

print('------------------')

def setter(ls2):
    return list(set(ls2))
a= setter(lista)
print(a)

'''                           ****
WORD location change
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string,
 except with the words in backwards order. For example, say I type the string:
'''

e_str= 'My name is Eran'
e_list = e_str.split(' ')
e_list = e_list[::-1]
e_str = ' '.join(e_list)
print(e_str)

x1= 'My name is Eran'
def revers(x):
    y= x.split(' ')
    return ' '.join(reversed(y))
print (revers(x1))


# to run only on main files
# def sqr(n):
#     return n*n
# if __name__ == "__main__":   
#     user_num= int(input('please give me a number: '))
#     print (sqr(user_num))
print ('---   Cows And Bulls   ---')
'''
'Cows And Bulls' - Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
'''
# - - - need to continue
gen_num = '0123'
test_num = '4253' #

def func(num):
    a = 1
    while a == 1:
        if  len (num) != 4:
            return 'nunber size doesnt fit'
        else:
            for i in range(len(gen_num)):
                bull_num = 0
                cow_num = 0 
                if gen_num[i] == num[i]:
                    bull_num +=1
                    cow_num +=1
                    result = f'bull: {bull_num}, cow: {cow_num}'
                    if bull_num != 4:
                        print (result)
                        print('not done yet...')
                        a = 'b' # num = input('please put 4 digit number -Again')
                    else:
                        print (result)
                        print('game finished after x tryies')
                        a = 'b'
                          
func(test_num)

#   
'''
Element Search
'''

log_file = open ('C:\\app\\PY_EXERCISE\\func_log.txt','a')
log_file.write('starting...')

lista = list(range(1,100,3))
lista.sort(reverse = True) # making sure it's sorted
print(list(lista))
check_num = 7
a= ''

def sorter_func(num,loop):
    for n in lista:
        loop +=1 
        if n > num:
            liner = '\n'*loop 
            print(f'{n} > {num}')
            log_file.write(liner +f'{n} > {num}')
            str_= liner +f'{n} > {num}'

        elif n == num : 
            print(f'{n} = {num}')
            log_file.write(liner +f'{n} > {num}')
            return True
        else:
            return False
            # if n < num:
            #     return False
        #     print(num,n)
        # if n == num:
        #     return True
        #     print(num,n)
        # else:
        #     return False
        #     print(num,n)

print(sorter_func(check_num,loop = 0))  
log_file.close()


loc_start = 0
loc_end = int(len(lista))-1 
loc_mid = int(len(lista)/2)
nmid0 = lista[loc_start]
nmid1 = lista[loc_end]
nmid2 = lista.index(loc_mid)
a= False

#print (loc_end)
while loc_end - loc_start >1 or a == True:
    loc_mid = int((loc_end - loc_start)/2) + loc_start # need to add the start as it' s in the middle of new string
    if check_num == lista[loc_mid]:
        a= True 
        break
    elif check_num < lista[loc_mid]:
        loc_start = loc_mid
        #loc_mid = int((loc_end - loc_start)/2) + loc_start # need to add the start as it' s in the middle of new string
        print(f'new range (right): {lista[loc_start]} - {lista[loc_end]}')
    else:
        loc_end = loc_mid
        #loc_mid = int((loc_end - loc_start)/2) + loc_start # need to add the start as it' s in the middle of new string
        print(f'new range (left): {lista[loc_start]} - {lista[loc_end]}')

print (f'result = {a}')
print ('--- find function ---')


###   a better for loop V V V - write as a function
def find(ordered_list, item_to_find):
    for item in ordered_list:
        if item == item_to_find:
            return True
    return False 

if __name__ == '__main__':
    list_of_items = list(range(0,20,2))
    print(find(list_of_items,8))
    print(list_of_items)

#            Write To A File 
open_file = open('C:\\app\\PY_EXERCISE\\PY_test_writing.txt','w') 
open_file.write('bla bla bla bla bla ')
open_file.close()

with open ('C:\\app\\PY_EXERCISE\\PY_test_writing.txt','a') as the_file:
    the_file.write('\nbela bela bela bela bela')
with open ('C:\\app\\PY_EXERCISE\\PY_test_writing.txt','r')  as the_file:
    q = the_file.read() 
    print(q)


with open ('C:\\app\\PY_EXERCISE\\func_log1.txt','a') as the_file2:
    for c in range (10):
        the_file2.write('\n starting another line:... ')
        the_file2.write(f'\n writing line no {c**3}')
'''
Read From File -Quotation List
'''
q_list2 =[]
with open ('C:\\app\\PY_EXERCISE\\Quotation_List.txt','r') as quote1:
    q_list = quote1.readlines()
    for txt in q_list:
        q_list2.append(txt.strip('\n'))
        #print(q_list2)
    
# new_list4 =[]
# with open ('C:\\app\\PY_EXERCISE\\Training_01.txt','r') as tr_file:
#     long_str = tr_file.readlines()
    
#     for s in long_str:
#         new_list4.append(s.split('/')[2])
# unique_list = set(new_list4)
# new_dict= {}
# for i in unique_list:
#     #print(f'{i} : {new_list4.count(i)}')
#     new_dict[i] = new_list4.count(i)
#     print (new_dict)
#     print(type(new_dict))

# copied code *****                          V V V
counter_dict = {}
with open('C:\\app\\PY_EXERCISE\\Training_01.txt') as f:
	line = f.readline()
	while line:
		line = line.split('/')[2]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)  



dups=[]
dup_dict={}
with open ('C:\\app\\PY_EXERCISE\\files\happynumbers.txt') as file1:
    file1row =  file1.readline()
    while file1row:
        #print (f'file1: {file1row}')
        with open ('C:\\app\\PY_EXERCISE\\files\primenumbers.txt') as file2:
            file2row =  file2.readline()
            while file2row:
                #print (f'file2: {file2row}')
                if file2row == file1row:
                    dups.append(file2row.strip('\n'))
                    if file2row in dup_dict:
                        dup_dict[file2row.strip('\n')] += 1
                    else:
                        dup_dict[file2row.strip('\n')] = 1
                file2row =  file2.readline()

        file1row =  file1.readline()
print(list(dups))
print(dup_dict)
# with open (C:\\app\\PY_EXERCISE\\files\happynumbers.txt) file2:
#     file2row =  file2.readline()    
'''
def mulix(x,y):
    print((x+1)*y)

def main():
    e = 2.1
    r = int(input('please set no.: '))
    mulix(e,r)

main()
'''

import random 
#Num Testing
high_limit = 100
lower_limit = 0

verify = ''
try1 = (high_limit - lower_limit)/2 
print (f'pls verigy its {try1}')
verify = input('verifing H/L/R: ')
tryies_count = 0
while verify != 'R':
    if verify == 'H' :
        lower_limit = try1 +1
        try1 = random.randint(lower_limit,high_limit)
        verify = input(f'verifing {try1} H/L/R ')
        tryies_count +=1
    elif verify == 'L' :
        high_limit = try1 -1
        try1 = random.randint(lower_limit,high_limit)
        verify = input(f'verifing {try1} H/L/R ')
        tryies_count +=1
    else:
        print(f'you got it its {try1} with {tryies_count} tryies')
        break

if verify == 'R':
    print (f'you got it its {try1} with {tryies_count} tryies')
















#     https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html