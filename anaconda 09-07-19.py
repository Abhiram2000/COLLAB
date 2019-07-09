#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst = [1,2,3,4,5,6,7,8,9]
print(len(lst))
print(lst * 2)
print(3 in lst)
for x in range(len(lst)):
    print(lst[x],end=" ")


# In[2]:


lst =[1,2,3,4,5,6]
print(lst)
print(lst[1])
print(lst[0])
print(lst[-1])
print(lst[-2])
print(lst[1:])
print(lst[1:4])
print(lst[0:])
print(lst[-1:])


# In[4]:


lst
print(min(lst))
print(max(lst))
print(sum(lst))
print(sum(lst)/len(lst))
print(sum(lst[::4]))
print(sum(lst[1::2])/len(lst[1::2]))


# In[5]:


lst=[1,2,3,4]
print(lst)
lst.append(83) # Adding a new element at the end of list
print(lst)
lst.insert(4,24) # Adding an element at particular index
print(lst)
lst.count(18) # Return the value how many times element repeated
print(lst.count(3))
lst.sort() # Sort the elements in ascending order
lst.pop # Remove the last element from list
print(lst)
lst.pop(1) # Remove an element from a particular index
print(lst)
lst1=[9,8,0]
lst.extend(lst1) # Merge the list2 with list1
lst
  


# In[6]:


def secondlarge(li):
    li.sort()
    return li[-2]
li = [1,19,6,2,8,18,3]
secondlarge(li)


# In[7]:


def secondlarge(li):
    li.sort()
    return li[1]
def genericleast(li,n):
    li.sort()
    return li[n-1]
li = [1,19,6,2,8,18,3]
genericleast(li,4)


# In[ ]:


### Searching Algorithm
#### Linear Search
#### Binary Search

### Linear Search
* Linear search algorithm can be applied on Duplicate and Unique List
   - Unique list: All items of the list is appeared only once
   - Duplicate List: The items of the list can be appeared more than once
* Linear search algorithm can be applied on Sorted and unsorted data


# In[8]:


# Function to search the data in a list
# Search is found then return the index <if not return -1
def linearsearch(x,target):
   for i in range(len(x)):
       if x[i]==target:
           return i
   return -1
x=[5,8,3,4,8]
linearsearch(x,9)


# In[9]:


#Function
# Input : List
# Output : Formated Output
# Test Case:
# [1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
def plot(x):
    for i in range(len(x)):
        if i==0 or i==len(x)-1:
            print(x[i],end=" ")
        else:
            print(x[i-1] * x[i+1],end=" ")
    return
x=[1,2,3,4,5]
plot(x)     


# In[10]:





# In[11]:


#*** Function to count the occurances of a character in a string
def repeat(x,target):
    c=0
    for i in x:
        if i==target:
            c+=1
    return c
# (OR)
#def repeat1(x,target):
#    return x.count(target)
n=str(input("enter a string-"))
m=str(input("enter target element-"))
repeat(n,m) 


# In[ ]:




