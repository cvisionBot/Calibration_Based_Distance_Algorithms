#include "calibration.h"

HD_RESULT calibration_init(double fx, double fy, double cx, double cy, double k1, double k2, double p1, double p2)
{
    HD_RESULT ret = HD_OK;

    Cam_Matrix cam_mat;
    cam_mat.in_param.fx = fx;
    cam_mat.in_param.fy = fy;
    cam_mat.in_param.cx = cx;
    cam_mat.in_param.cy = cy;

    Dis_Coeffs dis_coe;
    dis_coe.d_param.k1 = k1;
    dis_coe.d_param.k2 = k2;
    dis_coe.d_param.p1 = p1;
    dis_coe.d_param.p2 = p2;

    if (ret != HD_OK)
    {
        printf("check your camera inner parameters!! \n");
    }
    return ret
}

HD_RESULT calibration_uninit(void)
{
    HD_RESULT ret = HD_OK;

    if (ret != HD_OK)
    {
        printf("cant deinit calibration parameters!!\n");
    }
}

HD_RESULT calibration(VIDEO_LIVEVIEW *lv)
{
    HD_RESULT ret = HD_OK;

    if (ret != HD_OK)
    {
        printf("failed calibration process!! \n");
    }
    return ret
}