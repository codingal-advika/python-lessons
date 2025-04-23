'''Write a program to create a parent class Person (attributes - name, id number)
 with a method display to display the attributes. Next, create a child class Employee
(attributes - name, id number, salary, post). Access the attributes of parent class in child class. 
Then, create an object for child class and call the display method to display the name and id number'''

class parent :
    def __init__(self , name , id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print('The name of the employee is:' , self.name)
        print('The id number of the employee is: ' , self.id_number)
class child(parent):
    def __init__(self , name , id_number , salary , post):
        self.salary  = salary
        self.post = post
        parent.__init__(self, name  , id_number)
    def display(self):
        print('The amount of salary the child earns is' , self.salary)
        print('The post is: ' , self.post)
        parent.display(self)
ob  = child('Advika' , 5643210 , 25000 , 'Cashier')
ob.display()

    

