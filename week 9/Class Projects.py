#!/usr/bin/env python
# coding: utf-8

# ## Class Project 1
# One of the key issue that have threatened organizations and institutions is that of logistics. To solve it, employers now use biometric softwares and computer vision enabled tools to verify identities of their employees and take attendance. Mrs. Jane runs a delivery business with 15 employees, but she would want a way to identify if a user is one of her employees, take attendance and assign a task to the employee for the day. 
# 
# Employees = "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones" , "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima".
# 
# Tasks = "Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items"
# 
# Your mission, should you choose to accept it, is to develop python program using your knowledge in OOP (class and objects) that takes a user's name and check if he/she exists in the list of employees, take attendance for the day and assign a task to the employess … otherwise, you politely refuse access to the system.
# 
# <b>Hint:</b>
# 
# <ol><li>Build a class <b>Employee()</b> that has four methods in the class; <b>check_employee()</b>, <b>take_attendance()</b>, <b>assign_task()</b> and <b>refuse_access()</b>.</li><li>
#     You can <b>import random</b> module and use the <b>random.randint()</b> method to randomly select task from the list. </li></ol>
# 

# In[ ]:


import random
class Employee:
    Employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu", "Stella Mankinde", "Jane Akibo", "Ago James", 
                 "Michell Taiwo", "Abraham Jones" , "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"]
    Tasks = ["Loading", "Transporting", "Reveiwing Orders", "Customer Service", "Delivering Items"]
    count = 0
    
    def __init__(self,name):
        # constructors
        self.name = name
        
    def check_employee(self):
        if self.name in self.Employees:
            print ("Hello,", self.name)
    
    def take_attendance(self):
        # taking attendance by adding 1 for each employee
        if self.name in self.Employees:
            Employee.count += 1
        
    def assign_task(self):
        # picks a random task from the list of tasks
        if self.name in self.Employees:
            self.task = random.choice(self.Tasks)
            print(self.name, "your job is to", self.task)
    
    def refuse_access(self):
        if self.name not in self.Employees:
            print ("You do not have access to the system,", self.name)

def employee_checker():            
    employee = Employee(str(input("What is your name")))
    employee.check_employee()
    employee.refuse_access()
    employee.take_attendance()
    employee.assign_task()
    print('The number of employees present is:', employee.count)
    return employee_checker()

employee_checker()


# ## unused code
# #list of employees
# employee1 = Employee("Mary Evans")
# employee2 = Employee("Eyo Ishan")
# employee3 = Employee("Durojaiye Dare")
# employee4 = Employee("Adams Ali")
# employee5 = Employee("Andrew Ugwu")
# employee6 = Employee("Stella Mankinde")
# employee7 = Employee("Jane Akibo")
# employee8 = Employee("Ago James")
# employee9 = Employee("Michell Taiwo")
# employee10 = Employee("Abraham Jones")
# employee11 = Employee("Nicole Anide")
# employee12 = Employee("Kosi Korso")
# employee13 = Employee("Adele Martins")
# employee14 = Employee("Emmanuel Ojo")
# employee15 = Employee("Ajayi Fatima")
# 
# #list of tasks
# 1 = "Loading"
# 2 = "Transporting"
# 3 = "Reveiwing Orders"
# 4 = "Customer Service"
# 5 = "Delivering Items"
# 
# employee = Employee(str(input("What is your name")))

# ## Class Project 2
# You run a delivery service, and charge people based on their location and weight of their package. The following are some of the things you consider.
# 
# You charge N2000, whenever you are delivering a package with weight of 10kg and above to PAU, and N1500 when it is less.
# However, you charge N5000 whenever you deliver to Epe, a package with weight of 10kg and above, and N4000 when it is less.
# 
# Develop the python program using your knowledge in OOP, that tells a user how much to pay, based on their location, and package weight. 
# 

# In[ ]:


class service:
    
    def __init__(self,location,weight):
        self.location = location
        self.weight = weight

    def charge(self):
        if self.location == "PAU":
            if self.weight > 10:
                print ("The fee is N2000")
            elif self.weight == 10:
                print ("The fee is N2000")
            elif self.weight < 10:
                print ("The fee is N1500")
        
        elif self.location == "Epe":
            if self.weight > 10:
                print ("The fee is N5000")
            elif self.weight == 10:
                print ("The fee is N5000")
                
            elif self.weight < 10:
                print ("The fee is N4000")
        else:
            print ("We dont deliver here")

item = service(str(input("What is the delivery location?")), int(input("What is the weight?")))
item.charge()


# In[ ]:




