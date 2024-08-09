# 线性规划
import numpy as np
from scipy.optimize import linprog

# 6个工地坐标
a = np.array([1.25, 8.75, 0.5, 5.75, 3, 7.25])
b = np.array([1.25, 0.75, 4.75, 5, 6.5, 7.75])
# 临时料场位置
x = np.array([5, 2])
y = np.array([1, 7])
# 6个工地水泥日用量
d = np.array([3, 5, 4, 7, 6, 11])

# 计算目标函数系数
l = np.zeros((6, 2))
for i in range(6):
    for j in range(2):
        l[i, j] = np.sqrt((x[j] - a[i]) ** 2 + (y[j] - b[i]) ** 2)

f = np.concatenate((l[:, 0], l[:, 1]))

# 不等式约束条件
A = np.array([[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]])
b = np.array([20, 20])

# 等式约束条件
Aeq = np.hstack((np.eye(6), np.eye(6)))
beq = d

# 变量下界
Vlb = np.zeros(12)

# 求解线性规划问题
result = linprog(f, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=(0, None))
x = result.x
fval = result.fun

print("线性规划结果：", x)
print("最小目标函数值：", fval)

# 非线性规划

# from scipy.optimize import fmincon

# # 目标函数
# def fun2(x):
#     a1 = np.array([1.25, 8.75, 0.5, 5.75, 3, 7.25])
#     b1 = np.array([1.25, 0.75, 4.75, 5, 6.5, 7.75])

#     f1 = 0
#     for i in range(6):
#         s = np.sqrt((x[12] - a1[i]) ** 2 + (x[13] - b1[i]) ** 2)
#         f1 += s * x[i]

#     f2 = 0
#     for i in range(6, 12):
#         s = np.sqrt((x[14] - a1[i-6]) ** 2 + (x[15] - b1[i-6]) ** 2)
#         f2 += s * x[i]

#     return f1 + f2

# # 非线性约束函数
# def constraint(x):
#     g = np.array([np.sum(x[:6]) - 20, np.sum(x[6:12]) - 20])
#     k = np.array([x[0] + x[6] - 3, x[1] + x[7] - 5, x[2] + x[8] - 4,
#                   x[3] + x[9] - 7, x[4] + x[10] - 6, x[5] + x[11] - 11])
#     return g, k

# # 设置初始值
# x0 = np.array([3, 5, 0, 7, 0, 1, 0, 0, 4, 0, 6, 10, 5, 1, 2, 7])

# # 变量下界
# Vlb2 = np.concatenate((np.zeros(12), -np.inf * np.ones(4)))

# # 约束条件
# A2 = np.array([[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]])
# B2 = np.array([20, 20])
# Aeq2 = np.hstack((np.eye(6), np.eye(6), np.zeros((6, 4))))
# beq2 = np.array([3, 5, 4, 7, 6, 11])

# # 调用fmincon进行非线性规划求解
# result2 = fmincon(fun2, x0, A=A2, B=B2, Aeq=Aeq2, Beq=beq2, bounds=(Vlb2, None))
# x2 = result2.x
# fval2 = result2.fun

# print("非线性规划结果：", x2)
# print("最小目标函数值：", fval2)


# 蒙特卡罗法求近似解

# import random

# p0 = float('inf')
# n = 10**6
# x_m0 = None

# for i in range(n):
#     x_m = np.concatenate([
#         np.random.randint(0, 4, 1), np.random.randint(0, 6, 1), np.random.randint(0, 5, 1),
#         np.random.randint(0, 8, 1), np.random.randint(0, 7, 1), np.random.randint(0, 12, 1),
#         np.random.randint(0, 4, 1), np.random.randint(0, 6, 1), np.random.randint(0, 5, 1),
#         np.random.randint(0, 8, 1), np.random.randint(0, 7, 1), np.random.randint(0, 12, 1),
#         9 * np.random.rand(1), 9 * np.random.rand(1), 9 * np.random.rand(1), 9 * np.random.rand(1)
#     ])

#     g, k = constraint(x_m)
#     if np.all(g <= 0) and np.all(np.abs(k) <= 1):
#         ff = fun2(x_m)
#         if ff < p0:
#             x_m0 = x_m
#             p0 = ff

# print("蒙特卡罗法结果：", x_m0)
# print("最小目标函数值：", p0)
