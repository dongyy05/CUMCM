import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# 参数设置：W1 和 W2 为两个目标函数的权重
W1 = np.arange(0.1, 0.5 + 0.001, 0.001)  # W1 从 0.1 到 0.5，步长为 0.001
W2 = 1 - W1  # W2 是 W1 的补数
n = len(W1)  # 权重组合的数量

# 初始化结果数组
F1 = np.zeros(n)  # 存储目标函数 f1 的值
F2 = np.zeros(n)  # 存储目标函数 f2 的值
X1 = np.zeros(n)  # 存储决策变量 x1 的值
X2 = np.zeros(n)  # 存储决策变量 x2 的值
FVAL = np.zeros(n)  # 存储综合目标函数的值

# 线性规划约束条件
A = np.array([[-1, -1]])  # 不等式约束 A*x <= b
b = np.array([-7])  # 约束右侧常数
lb = np.array([0, 0])  # 变量的下界
ub = np.array([5, 6])  # 变量的上界

# 执行线性规划计算
for i in range(n):
    w1 = W1[i]  # 当前权重 w1
    w2 = W2[i]  # 当前权重 w2
    # 目标函数系数 c = w1*f1 + w2*f2
    c = np.array([w1 / 30 * 2 + w2 / 2 * 0.4, w1 / 30 * 5 + w2 / 2 * 0.3])
    # 设置变量边界条件
    bounds = [(lb[j], ub[j]) for j in range(len(lb))]
    # 求解线性规划问题
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    
    if res.success:  # 如果求解成功
        x = res.x  # 取出最优解
        F1[i] = 2 * x[0] + 5 * x[1]  # 计算 f1 的值
        F2[i] = 0.4 * x[0] + 0.3 * x[1]  # 计算 f2 的值
        X1[i] = x[0]  # 存储 x1 的值
        X2[i] = x[1]  # 存储 x2 的值
        FVAL[i] = res.fun  # 存储综合目标函数的值
    else:
        print(f"Optimization failed at iteration {i}.")  # 如果求解失败，输出提示信息

# 绘制图形
plt.figure(1)  # 创建第一个图形窗口
plt.plot(W1, F1, label='f1')  # 绘制 f1 的值随权重变化的曲线
plt.plot(W1, F2, label='f2')  # 绘制 f2 的值随权重变化的曲线
plt.xlabel('f1 Weight')  # x 轴标签
plt.ylabel('f1, f2 values')  # y 轴标签
plt.legend()  # 添加图例

plt.figure(2)  # 创建第二个图形窗口
plt.plot(W1, X1, label='x1')  # 绘制 x1 的值随权重变化的曲线
plt.plot(W1, X2, label='x2')  # 绘制 x2 的值随权重变化的曲线
plt.xlabel('f1 Weight')  # x 轴标签
plt.ylabel('x1, x2 values')  # y 轴标签
plt.legend()  # 添加图例

plt.figure(3)  # 创建第三个图形窗口
plt.plot(W1, FVAL)  # 绘制综合目标函数值随权重变化的曲线
plt.xlabel('f1 Weight')  # x 轴标签
plt.ylabel('Comprehensive indicators:')  # y 轴标签

plt.show()  # 显示所有图形
