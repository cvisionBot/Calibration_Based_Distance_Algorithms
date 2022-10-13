import cv2
import numpy as np


R = np.array([
    [0.94572609, -0.00128113, -0.32496234],
    [0.0938913,  -0.95626629, 0.27701843],
    [-0.31110543, -0.2924947,  -0.90424569]
])

t = np.array([[-23.42784994, -3.89708294, 53.57954617]]).T


def calculate_distance(R, t, target_point):
    u = (target_point[0] - 960) / 1423.10029
    v = (target_point[1] - 540) / 1423.10029

    Pc = np.array([[u, v, 1]]).T
    
    a = R
    b = (Pc - t)
    c = (-t)

    t = t.T

    Pw = np.dot(a, b)
    Cw = np.dot(a, c)
    k = Cw[-1] / (Pw[-1] - Cw[-1])
    P = Cw + k * (Pw-Cw)
    print('distance : ', P[-1])


if __name__ == "__main__":
    calculate_distance(R, t, [391, 454])