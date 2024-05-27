#!/usr/bin/env python
# coding: utf-8

# # PART I: LISTS, DICTIONARIES, TUPLES, SET AND BOOLEANS 

# In[ ]:


#LIST

#a list is mutable, means they can be changed/modified/updated
list1=[1,2,3,4,5]  or list2 = [(2,4),(6,8),(10,12)]
#a list can hold differents types of items like string, integer, charactere etc...
list2[1:] ---> [(6,8),(10,12)]
list2[:2] ---> [(2, 4), (6, 8)]

#nesting list
final_list= [list1,list2] ---> [[1, 2, 3, 4, 5], [(2, 4), (6, 8), (10, 12)]]

#added an item from the list
final_list.append('Hi my name is yoan') ---> [[1, 2, 3, 4, 5], [(2, 4), (6, 8), (10, 12)], 'Hi my name is yoan']
#remove an item from the list. By default pop takes off the last index in the list.
final_list.pop(1) ---> [[1, 2, 3, 4, 5], 'Hi my name is yoan']

#reverse
final_list.reverse()
#sort
list1.sort() #only with integer, for exemple list2 = [(2,4),(25,3),(3,12)], list2.sort --->[(2, 4), (3, 12), (25, 3)]


# In[ ]:


#DICTIONARIES

#dictionaries are very flexible in the data types they can hold (string, integer, float). For example:
my_dict = {'banana': 12.3, 'melon': 5.2, 'fruits': ['banana', 'melon', 'orange']}

# Can call an index on that value
my_dict['key3'][0] --->'item0'

# nesting in a dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
# Keep calling the keys
d['key1']['nestkey']['subnestkey']---> 'value'

#return a list of all the keys:
d.keys() ---> dict_keys(['banana', 'melon', 'fruits'])

# Method to grab all values, means return the value of the key only.
d.values() ---> dict_values([12.3, 5.2, ['banana', 'melon', 'orange']])


# In[ ]:


#TUPLES

#They are immutables, means they can't be changed such are days of week, or dates on calendar.
#they can hold differents data types like string, integer etc... like in a list
tuple1=(1,2,3) tuple2=('one', 'hello', 3)
#we can indexing 
tuples[1:] ---> ('hello', 3)

#tuples are not used as often as lists in programming, but are used when immutability is necessary.
#If in your program you are passing around an object and need to make sure it does not get changed,
#then a tuple becomes your solution. It provides a convenient source of data integrity.


# In[ ]:


#SET

Sets are an unordered collection of unique elements.
list=[1,2,45,1,45,4,5,28,98,35,28]---> {1, 2, 4, 5, 28, 35, 45, 98}


# In[ ]:


#BOOLEANS

1 > 2 ---> FALSE
1 < 2 ---> TRUE


# # PART II: IF, FOR STATEMENTS

# In[ ]:


# Python Statements example:

#IF STATEMENTS#

loc = 'Bank' #il faut ici définir ta variable 

if loc == 'Auto Shop': # SI ta variable est égale (==) à ce que tu à écris plus haut alors print('')a. 
    print('Welcome to the Auto Shop!') 
elif loc == 'Bank': #si la première condition n'est pas respectée alors on utilise l'expression "elif"
                    #qui doit être au même au même niveau que "if". Si elif est respectée alors print('').
    print('Welcome to the bank!')
else: #si aucune des conditions n'est respectée alors print('')
    print('Where are you?')


# In[ ]:


#FOR STATEMENTS#

# basic example:
list1=[1,2,3,4,5] # il faut ici définir ta liste/tuples/dictionaries
for num in list1: # tu définis ici un argument qui doit être verifié dans la variable défini plus haut.
    if num % 2 == 0: #tu rajoute un IF, ici qui dit, si l'argument est un chiffre paire, alors imprime l'argument.
        print(num)
--->
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]   


# Start sum at zero
list_sum = 0 
for num in list1:
    list_sum = list_sum + num #te permet de faire une somme. tu rajoutes "num" à la liste déjà existante.
print(list_sum)

#impression de lettres
for letter in 'This is a string.':         t=(1,2,3)                    list2 = [(2,4),(6,8),(10,12)]
    print(letter)                            for t in tup:                 for tup in list2:
                                              print(t)                         print(tup)
                                                                                    (2, 4)
                                                                                    (6, 8)
                                                                                    (10, 12)
t
h
i
s
.
.
.


dict_items([('k1', 1), ('k2', 2), ('k3', 3)])
for k,v in d.items():
    print(k)
    print(v) 
k1
1
k2
2
k3
3


# # PART III :  USEFUL OPERATOR

# In[ ]:


#Useful Operators

#enumerate
index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

#range   
list(range(0,101,10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#zip
list(enumerate('abcde'))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

#random
from random import shuffle
mylist
[40, 10, 100, 30, 20]

#input
input('Enter Something into this box: ')


# In[ ]:


#list comprehension:

# Grab every letter in string
lst = [x for x in 'word']

# Square numbers in range and turn into list
lst = [x**2 for x in range(0,11)]
lst [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
fahrenheit


# # PART IV : *ARGS and *KWARGS

# In[2]:


def my_func(*args):
    return sum(args)
my_func(1,2,3,4)
10


# # PART V : FUNCTIONS

# In[ ]:


#MAKES TWENTY ONE: Given two integers, return True if the sum of the integers is 21 or if one of the integers is 21.
#If not, return False


#option1:

def black_jack(a,b):

    numbers=[a,b] #List, entre crochet qui sera utilisée lors du lancement de la fonction plus bas
    if sum(numbers)==21 or a==21 or b == 21:
        return True
    else :
        return False
    
#option2:
def black_jack(a,b):

    numbers=[a,b] 
    if sum(numbers)==21 or 21 in numbers:
        return True
    else :
        return False

#option3:
def black_jack(a, b):
    return sum([a, b]) == 21 or 21 in [a, b] #using a boolean expression instead of an if-else statement


# In[13]:


#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


#option1

def old_macdonald1(name):
    
    first_letter= name[0]
    between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    
    return first_letter.upper() + between + fourth_letter.upper() + rest

#option2
def old_macdonald2(name):
    first_half= name[:3]
    second_half= name[3:]
    return first_half.capitalize() + second_half.capitalize()


# In[14]:


old_macdonald2('macdonald')


# In[57]:


def master_yoda(sentence):
    sentence= sentence.split()
    reverse_sentence = sentence[::-1]
    return ' '.join(reverse_sentence)


# In[58]:


master_yoda('I am home')


# In[ ]:





# In[ ]:




