# Class 변수
class Variable:
    def __init__(self, data=0.0):
        self.data = data

# Function 클래스
class Function:
    def __call__(self, input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output