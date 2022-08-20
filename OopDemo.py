#classes are user defined blueprint or prototype
#sum, multipication, addition, constant
#in class we have methods, variabel, instance variables, constructor etc
# Objects for your class

class Calculator:
    num = 100

    # init is keyword to declare constructor
    def __init__(self):
        print("I am called automatically when object is created")

    def getData(self):
        print("I'm now executing as method in class")

# create object
obj = Calculator() #syntax to create objects in python
obj.getData() #call method in class
print(obj.num)