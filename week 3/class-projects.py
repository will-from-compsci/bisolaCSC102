#!/usr/bin/env python
# coding: utf-8

# ## Name: Akinkugbe Bisola
# ## Matriculation number: 21120612556
# ## E-mail: bisola.akinkugbe@pau.edu.ng

# ## Project 1 Algorithm
# ![Project 1](project1.png) 
# <br>BEGIN
# <br>INPUT number
# <br>IF number < 17:
#     <br>DECLARE ans = 17 - number
#     <br>COMPUTE ans
#     <br>DISPLAY "The answer is ans"
#     <br>ENDIF
# <br>IF number > 17:
#     <br>DECLARE ans = 2 * (number - 17)
#     <br>COMPUTE ans
#     <br>DISPLAY "The answer is ans"
#     <br>ENDIF
# <br>END

# In[10]:


# Project 1
# Program to get the difference between a given number and 17, and if the number is greater than 17, return double the absolute difference
number = int(input("What is the number?"))
if number < 17:
    print ("The answer is", 17 - number)
elif number > 17:
    print ("The answer is", ((number - 17) * 2))


# ## Project 2 Algorithm
# ![Project 2](project2.png)
# <br>BEGIN
# <br>INPUT num1, num2, num3
# <br>IF num1 == num2 == num3:
#     <br>COMPUTER answer = (num1 + num2 + num3) * 3
#     <br>DISPLAY "The answer is answer"
#     <br>ENDIF
# <br>ELSE:
#     <br>answer = num1 + num2 + num3
#     <br>DISPLAY "The answer is answer"
# <br>END
#     

# In[13]:


# Project 2
# Program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum 
num1 = int(input("What is the 1st number?"))
num2 = int(input("What is the 2nd number?"))
num3 = int(input("What is the 3rd number?"))
if num1 == num2 == num3:
    answer = (num1 + num2 + num3) * 3
else:
    answer = num1 + num2 + num3
print ("The answer is", answer)


# ## Project 3 Algorithm
# ![Project 3](project3.png)
# <br>BEGIN
# <br>INPUT num1, num2
# <br>IF num1 = num2:
#     <br>DISPLAY "True"
#     <br>ELSE IF num1 - num2 = 5:
#         <br>DISPLAY "True"
#         <br>ELSE IF num1 + num2 = 5:
#             <br>DISPLAY "True"
#             <br>ELSE:
#                 <br>DISPLAY "False"
# <br>END
#             

# In[34]:


# Project 3
# Program which will return true if the two given integer values are equal or their sum or difference is 5
num1 = int(input("What is the 1st number?"))
num2 = int(input("What is the 2nd number?"))
if num1 == num2:
    print ("True")
else:
    if num1 - num2 == 5:
        print ("True")
    else:
        if num1 + num2 == 5:
            print ("True")
        else:
            print ("False")


# ## Project 4 Algorithm
# ![Project 4](project4.png)
# <br>BEGIN
# <br>INPUT num1, num2, num3
# <br>DETERMINE biggest
# <br>DETERMINE smallest
# <br>DECLARE middle = num1 + num2 + num3 - biggest - smallest
# <br>DISPLAY "The order is smallest, middle, biggest" 
# <br>END

# In[39]:


# Project 4
# Program to sort three integers without using conditional statements and loops
num1 = int(input("What is the 1st number?"))
num2 = int(input("What is the 2nd number?"))
num3 = int(input("What is the 3rd number?"))
biggest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
middle = num1 + num2 + num3 - biggest - smallest
print ("The order is", smallest, middle, biggest)


# ## Project 5 Algorithm
# ![Project 5](project5.png)
# <br>BEGIN
# <br>DECLARE sumlist = []
# <br>INPUT number
# <br>IF number > 1:
#     <br>REPEAT number - 1
#     <br>UNTIL number = 1
# <br>COMPUTE cube = number^3
# <br>DISPLAY cube
# <br>APPEND cube into a list or set
# <br>DISPLAY the sum of the cubes
# <br>END

# In[4]:


# Project 5
# Program that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
sumlist = [] 
number = int(input("What is the number?"))
while number > 1:
    number -= 1
    cube = (number**3)
    print (cube)
    sumlist.append(cube)
    print (sum(sumlist))




