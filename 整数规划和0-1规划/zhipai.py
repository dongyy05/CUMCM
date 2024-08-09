import numpy as np
import pulp

# 目标函数系数，按列展开为一维数组
c = np.array([
    [66.8, 75.6, 87, 58.6],
    [57.2, 66, 66.4, 53],
    [78, 67.8, 84.6, 59.4],
    [70, 74.2, 69.6, 57.2],
    [67.4, 71, 83.8, 62.4]
]).flatten()

# 不等式约束条件
A = np.array([
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
])
b = np.array([1, 1, 1, 1, 1])

# 等式约束条件
Aeq = np.array([
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
])
beq = np.array([1, 1, 1, 1])

# 定义问题
problem = pulp.LpProblem("Integer_Linear_Programming", pulp.LpMinimize)

# 创建变量
x = [pulp.LpVariable(f'x{i}', cat='Binary') for i in range(20)]

# 目标函数
problem += pulp.lpDot(c, x)

# 不等式约束
for i in range(5):
    problem += pulp.lpDot(A[i], x) <= b[i]

# 等式约束
for i in range(4):
    problem += pulp.lpDot(Aeq[i], x) == beq[i]

# 求解问题
problem.solve()

# 输出结果
x_values = [pulp.value(var) for var in x]
fval = pulp.value(problem.objective)

print("最优解的变量值为:")
x_values_reshape = np.reshape(x_values, (5, 4))
print(x_values_reshape)

print("目标函数的最小值为:")
print(fval)
