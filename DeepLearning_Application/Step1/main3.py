import numpy as np
from CDeZero3 import *

print("hello")

data = np.array(2.0)
x = Variable(data)

# 2.3 Square Function 클래스
f = Square()
y = f(x)

print('y=', y.data)

# 3.2 함수 연결
A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b) # y = (exp(x^2))^2을 계산

print(y.data)

# 4.2 수치 미분
f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f, x) # y = x^2의 미분값을 계산

print('dy=', dy)

y.grad = np.array(1.0) # y에 대한 미분값을 1로 설정
b.grad = C.backward(y.grad) # C의 backward 메서드를 호출하여 b에 대한 미분값 계산
a.grad = B.backward(b.grad) # B의 backward 메서드를 호출하여 a에 대한 미분값 계산
x.grad = A.backward(a.grad) # A의 backward 메서드를 호출하여 x에 대한 미분값 계산

print('dy/dx = x.grad=', x.grad)