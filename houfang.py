import numpy as np
import math as m

# 定义函数 r_mat，用于计算旋转矩阵 R
def r_mat(f, w, k):
    """
    计算旋转矩阵 R

    参数:
        f: 绕 X 轴的旋转角度 (弧度)
        w: 绕 Y 轴的旋转角度 (弧度)
        k: 绕 Z 轴的旋转角度 (弧度)

    返回:
        R: 旋转矩阵
    """
    # 绕 X 轴旋转矩阵
    Rf = np.mat([[m.cos(f), 0, -m.sin(f)],
                 [0, 1, 0],
                 [m.sin(f), 0, m.cos(f)]])
    # 绕 Y 轴旋转矩阵
    Rw = np.mat([[1, 0, 0],
                 [0, m.cos(w), -m.sin(w)],
                 [0, m.sin(w), m.cos(w)]])
    # 绕 Z 轴旋转矩阵
    Rk = np.mat([[m.cos(k), -m.sin(k), 0],
                 [m.sin(k), m.cos(k), 0],
                 [0, 0, 1]])
    # 旋转矩阵 R = Rf * Rw * Rk
    R = Rf * Rw * Rk

    return R

# 定义函数 xy_approximate，用于近似计算像点坐标 x、y
def xy_approximate(X, Y, Z, x, y, Xs, Ys, Zs, R,f,xo,yo):
    """
    近似计算像点坐标 x、y

    参数:
        X: 物方点 X 坐标数组
        Y: 物方点 Y 坐标数组
        Z: 物方点 Z 坐标数组
        x: 像点 x 坐标数组
        y: 像点 y 坐标数组
        Xs: 相机投影中心 X 坐标
        Ys: 相机投影中心 Y 坐标
        Zs: 相机投影中心 Z 坐标
        R: 旋转矩阵

    返回:
        x_apxm: 近似计算的像点 x 坐标数组
        y_apxm: 近似计算的像点 y 坐标数组
    """
    x_apxm = [0, 0, 0, 0]
    y_apxm = [0, 0, 0, 0]

    # 遍历四个像点
    for i in [0, 1, 2, 3]:
        # 近似计算像点 x 坐标
        x_apxm[i] = x[i] - (xo - f * ((R[0, 0] * (X[i] - Xs) + R[1, 0] * (Y[i] - Ys) + R[2, 0] * (Z[i] - Zs))
                                      / (R[0, 2] * (X[i] - Xs) + R[1, 2] * (Y[i] - Ys) + R[2, 2] * (Z[i] - Zs))))
        # 近似计算像点 y 坐标
        y_apxm[i] = y[i] - (yo - f * ((R[0, 1] * (X[i] - Xs) + R[1, 1] * (Y[i] - Ys) + R[2, 1] * (Z[i] - Zs))
                                      / (R[0, 2] * (X[i] - Xs) + R[1, 2] * (Y[i] - Ys) + R[2, 2] * (Z[i] - Zs))))

    return x_apxm, y_apxm

# 定义函数 a_parameter，用于计算 A 矩阵参数
def a_parameter(X, Y, Z, Xs, Ys, Zs, x, y, w, k, R,f,xo,yo):
    """
    计算 A 矩阵参数

    参数:
        X: 物方点 X 坐标
        Y: 物方点 Y 坐标
        Z: 物方点 Z 坐标
        Xs: 相机投影中心 X 坐标
        Ys: 相机投影中心 Y 坐标
        Zs: 相机投影中心 Z 坐标
        x: 像点 x 坐标
        y: 像点 y 坐标
        w: 绕 Y 轴的旋转角度 (弧度)
        k: 绕 Z 轴的旋转角度 (弧度)
        R: 旋转矩阵

    返回:
        parameter: A 矩阵参数
    """
    parameter = np.zeros((2, 6))
    mean = np.zeros((3, 1))
    minus = np.zeros((3, 1))

    minus = np.array([[X - Xs],
                      [Y - Ys],
                      [Z - Zs]])
    mean = R.T * np.mat(minus)

    parameter[0][0] = (R[0, 0] * f + R[0, 2] * (x - xo)) / mean[2].item()
    parameter[0][1] = (R[1, 0] * f + R[1, 2] * (x - xo)) / mean[2].item()
    parameter[0][2] = (R[2, 0] * f + R[2, 2] * (x - xo)) / mean[2].item()
    parameter[1][0] = (R[0, 1] * f + R[0, 2] * (y - yo)) / mean[2].item()
    parameter[1][1] = (R[1, 1] * f + R[1, 2] * (y - yo)) / mean[2].item()
    parameter[1][2] = (R[2, 1] * f + R[2, 2] * (y - yo)) / mean[2].item()

    parameter[0][3] = (y - yo) * m.sin(w) - (
                ((x - xo) / f) * ((x - xo) * m.cos(k) - (y - yo) * m.sin(k)) + f * m.cos(k)) * m.cos(w)
    parameter[0][4] = -f * m.sin(k) - ((x - xo) / f) * ((x - xo) * m.sin(k) + (y - yo) * m.cos(k))
    parameter[0][5] = y - yo
    parameter[1][3] = -(x - xo) * m.sin(w) - (
                ((y - yo) / f) * ((x - xo) * m.cos(k) - (y - yo) * m.sin(k)) - f * m.cos(k)) * m.cos(w)
    parameter[1][4] = -f * m.cos(k) - ((y - yo) / f) * ((x - xo) * m.sin(k) + (y - yo) * m.cos(k))
    parameter[1][5] = -(x - xo)

    return parameter

#主程序入口
if __name__ == "__main__":
    #教材实例数据   参数

    X = [36589.41, 37631.08, 39100.97, 40426.54]
    Y = [25273.32, 31324.51, 24934.98, 30319.81]
    Z = [2195.17, 728.69, 2386.50, 757.31]

    x = [-86.15, -53.40, -14.78, 10.46]
    y = [-68.99, 82.21, -76.63, 64.43]


    # 计算 distance1
    distance1 = m.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    # 计算 distance2
    distance2 = m.sqrt((X[1] - X[0]) ** 2 + (Y[1] - Y[0]) ** 2)
    # 计算 m
    k = distance2 / distance1
    # 初始化参数
    fo = wo = ko = 0
    xo = yo = 0
    f =153.24  # 153.24参数6439.7435897
    Zsum = 0
    Xsum = 0
    Ysum = 0

    # 计算 X、Y 坐标的平均值
    for i in [0, 1, 2, 3]:
        ###Zsum =Zsum + Z[i]
        Xsum = Xsum + X[i]
        Ysum = Ysum + Y[i]

    Zos = k * f #参数
    Xos = Xsum / 4
    Yos = Ysum / 4

    # 初始化近似像点坐标数组
    x_apxm = [0, 0, 0, 0]
    y_apxm = [0, 0, 0, 0]

    # 初始化旋转矩阵 R、L 矩阵、A 矩阵
    R = np.mat(np.zeros((3, 3)))
    L = np.mat(np.zeros((8, 1)))
    A = np.mat(np.zeros((8, 6)))

    # 初始化参数改正值
    f_cor = w_cor = k_cor = 1
    # 初始化迭代次数
    flag = 0
    # 迭代计算参数
    while (abs(f_cor) > 0.000001) | (abs(w_cor) > 0.000001) | (abs(k_cor) > 0.000001):
        # 计算旋转矩阵 R
        R = r_mat(fo, wo, ko)
        # 近似计算像点坐标
        x_apxm, y_apxm = xy_approximate(X, Y, Z, x, y, Xos, Yos, Zos, R,f,xo,yo)

        # 构建 L 矩阵
        for i in [0, 1, 2, 3]:
            L[2 * i] = x_apxm[i]
            L[2 * i + 1] = y_apxm[i]

        # 构建 A 矩阵
        for i in [0, 1, 2, 3]:
            A[2 * i:2 * i + 2, :] = a_parameter(X[i], Y[i], Z[i], Xos, Yos, Zos, x[i], y[i], wo, ko, R,f,xo,yo)

        # 计算参数改正值
        X_mat = np.mat(np.zeros((6, 1)))
        X_mat = (A.T * A).I * A.T * L

        f_cor = X_mat[3, 0]
        w_cor = X_mat[4, 0]
        k_cor = X_mat[5, 0]

        # 更新参数
        Xos = Xos + X_mat[0, 0]
        Yos = Yos + X_mat[1, 0]
        Zos = Zos + X_mat[2, 0]
        fo = fo + X_mat[3, 0]
        wo = wo + X_mat[4, 0]
        ko = ko + X_mat[5, 0]

        # 迭代次数加 1
        flag += 1
        # 打印迭代信息
        if flag <= 10000:
            print("第 %d 次迭代：f_cor = %f,w_cor = %f,k_cor = %f" % (flag, f_cor, w_cor, k_cor))
        else:
            print("级数不收敛，中间结果为：")
            break

    # 打印结果
    if flag <= 100:
        print("级数收敛，最终结果为：")
    print(" Xs=%f,\n Ys=%f,\n Zs=%f,\n f=%f,\n w=%f,\n k=%f" % (Xos, Yos, Zos, fo, wo, ko))
    print(" R = ", end='')
    print(R)

    # 计算单位权中误差
    V = np.mat(np.zeros((8, 1)))
    V = A * X_mat - L
    errorValue = m.sqrt((V.T * V).item() / (2 * 4 - 6))
    print("单位权中误差：%f" % errorValue)