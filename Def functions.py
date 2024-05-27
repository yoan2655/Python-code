#!/usr/bin/env python
# coding: utf-8

# In[7]:


def lesser_even(a,b):
    if a %2==0 and b %2==0:
        if a<b:
            return max(a,b)
        
    else:

        if a<b:
            return min(a,b)


# In[9]:


lesser_even(2,10)


# In[32]:


def animal(text):

    text=text.split()
    print(text)
    return text[0][0] == text[1][0]


# In[34]:


animal('lama nion')


# In[62]:


def black_jack(a,b):
    return a+b ==21 or a==21 or b==21


# In[63]:


black_jack(10,11)


# In[91]:


def old_macdonald(name):
    
    first_letter= name[0]
    between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    
    return first_letter.upper() + between + fourth_letter.upper() + rest


# In[92]:


old_macdonald('macdonald')


# In[97]:


def almost_there(number):
    for x in number: 
        if 90<x<110 :
            return True


# In[98]:


almost_there(24)


# In[117]:


def almost_there(n):
    if 90<n<110 or 190<n<210:
        return True
    else:
        return False
    


# In[119]:


almost_there(100)


# In[ ]:




