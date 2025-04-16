class Fruit: #This is how class is declared
    fruits = 'Grapes'  #class variable(Global variable)  - > fruit is an attribute here.
    def __init__(self , taste , size):  #__init__ means initialize and this method get executed automatically.
        self.taste = taste  #instance variable(Local variable)
        self.size = size    #With the help of self we are making it global so that it can be used outside this method.
    def display_names(self):  #This is how a method is declared.
        print('The taste of the fruit is: ' , self.taste)
        print('The size of the fruit is: ' , self.size)
        
ob = Fruit('sweet and crispy' , 'small and green')# object creation(object is an example of a class)
#In the above line (class:Fruit) we have passed two argument.Arguments depends based on parameters passed in the __init__ method
ob.display_names()  # Calling a method(object name.method)
print('The name of the fruit is: ' , ob.fruits)  #Printing the class variable outside of the class

# Self and object are same.Self acts like an object inside a class.Example:To display the class variable inside the class
# we must right it as self.fruit instead of ob.fruit
