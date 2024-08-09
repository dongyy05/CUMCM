import numpy as np
from scipy.optimize import linprog

# 目标函数的系数 (负值用于最大化)
c = -np.array([540, 200, 180, 350, 60, 150, 280, 450, 320, 120])

# 整数约束变量的索引
intcon = list(range(10))

# 不等式约束条件
A = np.array([[6, 3, 4, 5, 1, 2, 3, 5, 4, 2]])
b = np.array([30])

# 等式约束条件 (此题中没有等式约束)
Aeq = None
beq = None

# 变量下界
lb = np.zeros(10)

# 变量上界
ub = np.ones(10)

# 调用 linprog 进行线性规划求解
result = linprog(c, A_ub=A, b_ub=b, bounds=list(zip(lb, ub)), method='highs')

# 获取结果并转换为整数
x = np.round(result.x).astype(int)
fval = -result.fun

print("最优解的变量值为:")
print(x)

print("目标函数的最大值为:")
print(fval)
