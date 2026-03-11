import numpy as np
#import CDeZero2 as dz
from CDeZero2 import * # CDeZero2의 모든 클래스를 가져옴, 클래스 사용에 dz를 안붙여도 됨.

print("hello")

data = np.array(2.0)
#x = dz.Variable(data)
x = Variable(data)

# 2.3 Function 클래스 이용
#f = dz.Square()
f = Square()
y = f(x)

print('y=', y.data)