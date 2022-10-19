import cv2
import copy
import numpy as np

# Camera Matrix [[fx, skew_c, cx], [0, fy, cy], [0, 0, 1]]
CAMERA_MATRIX = np.array([[693.648267, 0, 480.00], [0, 693.648267, 270.00], [0, 0, 1]])

# Dist Coeffs [[k1, k2, p1, p2]]
DIST_COEFFS  = np.array([[-0.415024, 0.141914, -0.007311, 0.001264]])

def calibration(origin_image, res_w, res_h):
    global CAMERA_MATRIX, DIST_COEFFS
    calib_image = copy.deepcopy(origin_image)
    for y in range(res_h):
        for x in range(res_w):
            y_nu = (y - CAMERA_MATRIX[1][-1]) / CAMERA_MATRIX[1][1]
            x_nu = (x - CAMERA_MATRIX[0][-1]) / CAMERA_MATRIX[0][0] # - skew_c * y_nu but skew_c = 0

            ru2 = x_nu * x_nu + y_nu * y_nu
            radial_d = 1 + DIST_COEFFS[0][0] * ru2 + DIST_COEFFS[0][1] * ru2 * ru2 # + k3 * ru2 * ru2 * ru2 but k3 doesn't exist

            x_nd = radial_d * x_nu + 2 * DIST_COEFFS[0][2] * x_nu * y_nu + DIST_COEFFS[0][3] * (ru2 + 2 * x_nu * x_nu)
            y_nd = radial_d * y_nu + DIST_COEFFS[0][2] * (ru2 + 2 * y_nu * y_nu) + 2 * DIST_COEFFS[0][3] * x_nu * y_nu

            x_pd = CAMERA_MATRIX[0][0] * x_nd + CAMERA_MATRIX[0][-1]
            y_pd = CAMERA_MATRIX[1][1] * y_nd + CAMERA_MATRIX[1][-1]
            # print('x_pd : ', x_pd)
            # print('y_pd : ', y_pd)
            calib_image[y][x] = origin_image[int(y_pd)][int(x_pd)] 

    return calib_image


def main():
    resolution_h = 540
    resolution_w = 960

    origin_image = cv2.imread('C:/Project_Tracker/calibration_image/0.jpg')
    origin_image = cv2.resize(origin_image, (resolution_w, resolution_h)) #ld
    
    
    cv2.imshow("orgin_image", origin_image)
    cv2.waitKey(0)

    calib_image = calibration(origin_image, resolution_w, resolution_h)
    cv2.imshow("calibration", calib_image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()