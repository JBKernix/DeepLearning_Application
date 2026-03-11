import numpy as np

# Class 변수
class Variable:
    def __init__(self, data=0.0):
        self.data = data
        self.grad = None

# Step2: Square Function 클래스
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        self.input = input # 입력값을 저장
        return Variable(y)
        
    # 함수의 확장성을 위해 자식에게 선언 되어 있는 매서드를 사용하여 상속되게 함.
    def forward(self, x):
        raise NotImplementedError()
        # 함수 계산을 위해 자식에게 선언 되어 있는 forward 매서드를 사용하여 상속되게 함.

    def backward(self, gy):
        raise NotImplementedError()
        # 미분 계산을 위해 자식에게 선언 되어 있는 backward 매서드를 사용하여 상속되게 함.

class Square(Function):
    def forward(self, x):
        return x ** 2
    
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx
        
    
class Exp(Function):
    def forward(self, x):        
        return np.exp(x)
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
    
# Step4: numerical_diff(수치 미분)
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)

    return (y1.data - y0.data) / (2 * eps)