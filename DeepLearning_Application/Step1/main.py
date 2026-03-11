import numpy as np
import CDeZero as dz

print("hello")

data = np
x = dz.Variable(data)

print('data=', data)
print('초기값 x=', x.data)

x.data = np.array(3.0)
print('변경값 x=', x.data)

y = dz.Variable()
print('초기값 y=', y.data)

y.data = np.array(10.0)
print('변경값 y=', y.data)
