import cv2
import numpy as np

# Camera Matrix [[fx, skew_c, cx], [0, fy, cy], [0, 0, 1]]
CAMERA_MATRIX = np.array([[693.648267, 0, 480.00], [0, 693.648267, 270.00], [0, 0, 1]])

# Dist Coeffs [[k1, k2, p1, p2]]
DIST_COEFFS  = np.array([[-0.415024, 0.141914, -0.007311, 0.001264]])

# 2D Point Array (Extract Image Coordinate system)
POINT_2D_LIST = []
# 3D Point Array (World Coordinate system)
POINT_3D_LIST = np.array([(9, 239, 0), (0, 239, 0), (0, 230, 0), (9, 230, 0)])

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global POINT_2D_LIST
        POINT_2D_LIST.append([x, y])


def calculate_distance(R_Matrix, t_vector, target_point):
    # Homogeneous Domain
    u = (target_point[0] - 480) / 693.648267
    v = (target_point[1] - 270) / 693.648267

    Pc = np.array([[u, v, 1]]).T

    a = R_Matrix.T
    b = (Pc - t_vector)
    c = (-t_vector)
    t = t.T

    Pw = np.dot(a, b)
    Cw = np.dot(a, c)
    k = Cw[-1] / (Cw[-1] - Pw[-1])
    Point_3D = Cw + k * (Pw -Cw)
    print('Point 3D : ', Point_3D)
    return int(Point_3D[1])


def SolvePnP_Pc_version():
    capture = cv2.VideoCapture(0) # using inner cam

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

    global CAMERA_MATRIX, DIST_COEFFS, POINT_2D_LIST, POINT_3D_LIST

    while True:
        ret, frame = capture.read()
                                                            # 0 - - - - 1
        cv2.imshow("video", frame)                          # |         | 
        cv2.setMouseCallback("video", mouse_event, frame)   # 3 - - - - 2
        
        if (len(POINT_2D_LIST) == 4): break
        
        if cv2.waitKey(1) == ord('q'): break

    capture.release()
    cv2.destroyAllWindows()

    print("check extract 2D point : ", POINT_2D_LIST)

    retval, rvec, tvec = cv2.solvePnP(POINT_3D_LIST, np.array(POINT_2D_LIST), CAMERA_MATRIX, DIST_COEFFS, rvec=None, tvec=None, useExtrinsicGuess=None, flags=None)
    # Reference Site : https://github.com/Yangxiu123321/solvePNP/blob/master/solvePNP/solvePNP/PNPsolver.cpp

    R_Matrix = cv2.Rodrigues(rvec)
    t_vector = tvec

    distance = calculate_distance(R_Matrix=R_Matrix, t_vector=t_vector, target_point=POINT_2D_LIST[1])
    print('distance : ', distance)


if __name__ == "__main__":
    SolvePnP_Pc_version()