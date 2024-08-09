import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value

# 目标函数的系数
c = [66.8, 75.6, 87, 58.6, 57.2, 66,
     66.4, 53, 78, 67.8, 84.6, 59.4, 70, 74.2,
     69.6, 57.2, 67.4, 71, 83.8, 62.4]

# 创建问题实例
prob = LpProblem("AssignmentProblem", LpMinimize)

# 定义变量 (0-1变量)
x = [LpVariable(f"x{i+1}", cat="Binary") for i in range(20)]

# 目标函数
prob += lpSum([c[i] * x[i] for i in range(20)])

# 约束条件：每个人只能参与一次
for i in range(5):
    prob += lpSum([x[j] for j in range(4*i, 4*i+4)]) == 1

# 约束条件：每个任务只能由一个人完成
for j in range(4):
    prob += lpSum([x[i*4 + j] for i in range(5)]) == 1

# 求解问题
prob.solve()

# 获取结果
solution = np.array([value(x[i]) for i in range(20)]).reshape(5, 4)
total_cost = value(prob.objective)

print("最优解的变量值为:")
print(solution)

print("目标函数的最小值为:")
print(total_cost)
