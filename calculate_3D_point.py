import cv2
import numpy as np

R = np.array([
    [0.81189968, -0.58378633, -0.00352633],
    [0.58376021,  0.81190152, -0.00631888],
    [0.00655191,  0.00307177,  0.99997382]
])

u = (391 - 960) / 1423.100291
v = (454 - 540) / 1423.100291

Pc = np.array([[u, v, 1]]).T
t = np.array([[1.89418832e+07, 8.22605760e+06, 2.21427044e+08]]).T

a = R
b = (Pc - t)

print('a b dot : ', np.dot(a, b))

c = (-t)

Pw = np.dot(a, b)
Cw = np.dot(a, c)
print('Pw : ', Pw)
print('Cw : ', Cw)
k = (-2.21570621e+08) / (-2.21570620e+08 - (-2.21570621e+08))
P = Cw + k * (Pw-Cw)
print('distance : ', P)