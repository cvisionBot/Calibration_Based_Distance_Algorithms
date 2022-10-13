import cv2
import numpy as np

MOUSE_POINT = []

camera_matrix = np.array([[1423.100291, 0, 960.00], [0, 1423.100291, 540.00], [0, 0, 1]])
dist_coeffs = np.array([-0.460567, 0.233740, 0.010677, 0.001339])

points_2D = np.array([
    (391, 454),
    (581, 457),
    (381, 205),
    (571, 199)
], dtype='double')

points_3D = np.array([
    (0.0, 0.0, 0.0),
    (10, 0.0, 0.0),
    (0.0, 10, 0.0),
    (10, 10, 0.0)
], dtype='double')

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global MOUSE_POINT
        MOUSE_POINT.append([x, y])

def main():
    capture = cv2.VideoCapture(0)

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

    while True:
        ret, frame = capture.read()

        cv2.imshow("video frame", frame)
        cv2.setMouseCallback("video frame", mouse_event, frame)

        global MOUSE_POINT, camera_matrix, dist_coeffs, points_2D, points_3D
        print('MOUSE : ', MOUSE_POINT)

        if len(MOUSE_POINT) == 4:
            retval, rvec, tvec = cv2.solvePnP(points_3D, points_2D, camera_matrix, dist_coeffs, rvec=None, tvec=None, useExtrinsicGuess=None, flags=None)

            R = cv2.Rodrigues(rvec)
            t = tvec

            print('R : ', R)
            print('t : ', t)

        if cv2.waitKey(1) == ord('q'): break
    
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()