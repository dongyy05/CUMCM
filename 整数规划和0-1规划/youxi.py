import numpy as np
from scipy.optimize import linprog

# 目标函数的系数 (负值用于最大化)
f = np.array([-20, -30, -40])

# 整数约束变量的索引 (Python linprog 默认处理实数，因此我们在解后进行整数处理)
intcon = [0, 1, 2]

# 不等式约束条件
A = np.array([
    [4, 8, 10],  # 4A + 8B + 10C <= 100
    [1, 1, 1]    # A + B + C <= 20
])
b = np.array([100, 20])

# 变量下界
lb = np.zeros(3)

# 调用 linprog 进行线性规划求解
result = linprog(f, A_ub=A, b_ub=b, bounds=[(0, None)]*3, method='highs')

# 获取结果并转换为整数
x = np.round(result.x).astype(int)
fval = result.fun

# 最大化目标函数的最终结果
y = -fval

print("A、B、C 三图分别通关的次数为: {}".format(x))

print("最终获得的经验为: {}".format(int(y)))

