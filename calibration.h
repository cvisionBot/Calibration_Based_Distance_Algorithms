#include <stdio.h>

/*-----------------------------------------------------------------------------*/
/* Type Definitions                                                            */
/*-----------------------------------------------------------------------------*/

typedef struct _Inner_Param
{
    double fx;
    double fy;
    
    int cx;
    int cy;
    // double skew_c;
} Inner_Param;

typedef struct _Disort_Param
{
    double k1;
    double k2;

    double p1;
    double p2;
} Disort_Param;

typedef struct _Camera_Matrix
{
    Inner_Param in_param;
    double matrix_info[3][3] = {in_param.fx, 0, in_param.cx, 0, in_param.fy, in_param.cy, 0, 0, 1};
} Cam_Matrix;

typedef struct _Disort_Coeffs
{
    Disort_Param d_param;
    double dis_coeffs[4] = {d_param.k1, d_param.k2, d_param.p1, d_param.p2};
} Dis_Coeffs;

#ifdef __cplusplus
extern "C"
{
#endif
    // calibration stream func
    HD_RESULT calibration_init(Cam_Matrix cam_mat, Dis_Coeffs dis_ceo, double fx, double fy, double cx, double cy, double k1, double k2, double p1, double p2);
    HD_RESULT calibration_uninit(unsigned char* calib_source);
    HD_RESULT calibration(unsigned char* source, int width, int height);

    // calcuarate center point working distance
    HD_RESULT calcurate_center_distance(unsigned char* calib_source, int res_w, int res_h, double Lens, double Focal_length, double FoV);

    // in calibration func
    HD_RESULT Normalize(double &x, double &y);
    HD_RESULT DeNormalize(double &x, double &y);
    HD_RESULT Disort(double &x, double &y);
    HD_RESULT DisortPixel(double &x, double &y);
    HD_RESULT UnDisortPixel(double &x, double &y);

#ifdef __cplusplus
}
#endif
