#in inheritance we cal acceess all method, properties and variabel form parent class Calculator
from OopDemo import Calculator

class ChildImplementation(Calculator):
    num2 = 100

    def __init__(self):
        # rules of inheritance when parent class have parameters that should not empty
        #if we didn't add parameter we get an error __init__() missing 2 required positional arguments: 'a' and 'b'
        Calculator.__init__(self, 3, 6)

    def getCompleteData(self):
        sum = self.num2 + self.num + self.Summation()
        return sum

obj = ChildImplementation()
print(obj.getCompleteData())