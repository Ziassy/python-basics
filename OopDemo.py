#classes are user defined blueprint or prototype
#sum, multipication, addition, constant
#in class we have methods, variabel, instance variables, constructor etc
# Objects for your class

# self keyword is mandatory for calling variables names into method
#intance and class variabel have whole different purpose
# constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 #class variabel

    # init is keyword to declare constructor
    def __init__(self, a, b):
        # create instance variabel
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I'm now executing as method in class")

    def Summation(self):
        sum = self.firstNumber + self.secondNumber + self.num
        return sum

# create object
# adding parameters constructor using instance variable
obj = Calculator(2, 5) #syntax to create objects in python
obj.getData() #call method in class
print(obj.num)
print(obj.Summation())