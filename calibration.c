#include "memory.h"
#include "calibration.h"


HD_RESULT calibration_init(Cam_Matrix* cam_mat, Dis_Coeffs* dis_coe, double fx, double fy, double cx, double cy, double k1, double k2, double p1, double p2)
{
    HD_RESULT ret = HD_OK;

    cam_mat->in_param.fx = fx;
    cam_mat->in_param.fy = fy;
    cam_mat->in_param.cx = cx;
    cam_mat->in_param.cy = cy;

    Dis_Coeffs dis_coe;
    dis_coe->d_param.k1 = k1;
    dis_coe->d_param.k2 = k2;
    dis_coe->d_param.p1 = p1;
    dis_coe->d_param.p2 = p2;

    if (ret != HD_OK)
    {
        printf("check your camera inner parameters!! \n");
    }
    return ret
}

HD_RESULT calibration_uninit(unsigned char* calib_source);
{
    HD_RESULT ret = HD_OK;

    free(calib_source)

    if (ret != HD_OK)
    {
        printf("cant deinit calibration parameters!!\n");
    }
}

HD_RESULT calibration(unsigned char* source, int width, int height)
{
    HD_RESULT ret = HD_OK;

    // # define parameter
    double resolution_w, resolution_h, focal_len, fov;
    double fx, fy, cx, cy, k1, k2, p1, p2;

    int x, y;
    double y_nu, x_nu, ru2, radial_d, x_nd, y_nd, x_pd, y_pd; 
    unsigned char* calib_source;
    calib_source = (unsigned char*)malloc(width, height);
    memcpy(calib_source, source, width * height);

    Cam_Matrix cam_mat;
    Dis_Coeffs dis_coe;

    calibration_init(&cam_mat, &dis_coe, fx, fy, cx, cy, k1, k2, p1, p2);
    // #define value

    for (y = 0; y < height; y++){
        for (x = 0; x < width; x++){
            y_nu = (y - cam_mat.in_param.cy) / cam_mat.in_param.fy;
            x_nu = (x - cam_mat.in_param.cx) / cam_mat.in_param.fx;

            ru2 = x_nu * x_nu + y_nu * y_nu;
            radial_d = 1 + dis_coe.d_param.k1 * ru2 + dis_coe.d_param.k2 * ru2 * ru2;

            x_nd = radial_d * x_nu + 2 * dis_coe.d_param.p1 * x_nu * y_nu + dis_coe.d_param.p2 * (ru2 + 2 * x_nu * x_nu);
            y_nd = radial_d * y_nu + dis_coe.d_param.p1 * (ru2 + 2 * y_nu * y_nu) + 2 * dis_coe.d_param.p2 * x_nu * y_nu;

            x_pd = cam_mat.in_param.fx * x_nd + cam_mat.in_param.cx;
            y_pd = cam_mat.in_param.fy * y_nd + cam_mat.in_param.cy;

            //calib_image 처리하기 index 접근
        };
    };

    calcurate_center_distance(&calib_source, );
    

    calibration_uninit(&calib_source);

    if (ret != HD_OK)
    {
        printf("failed calibration process!! \n");
    }
    return ret
}