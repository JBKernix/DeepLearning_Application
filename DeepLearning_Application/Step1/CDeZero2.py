# Class 변수
class Variable:
    def __init__(self, data=0.0):
        self.data = data

# Step2: Square Function 클래스
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()
        # 함수의 확장성을 위해 자식에게 선언 되어 있는 forward 매서드를 사용하여 상속되게 함.

class Square(Function):
    def forward(self, x):
        output = x ** 2
        return output