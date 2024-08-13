def knapsack(weights, values, capacity):
    """
    用于求解0-1背包问题的最大价值
    参数weights：物品的重量列表
    参数values：物品的价值列表
    参数capacity：背包的容量
    返回值：最大价值
    """
    n = len(weights)  # 物品数量
    dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]  # 初始化动态规划数组

    # 动态规划求解过程
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j < weights[i - 1]:  # 背包容量小于当前物品重量，不能选择当前物品
                dp[i][j] = dp[i - 1][j]
            else:  # 能选择当前物品，要选择价值更大的方案
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]
w = input('请输入物品的重量列表，用逗号分隔：')
v = input('请输入物品的价值列表，用逗号分隔：')
c = int(input('请输入背包的容量：'))
weights = [int(x) for x in w.split(',')]  # 将输入的字符串转换为整数列表
values = [int(x) for x in v.split(',')]
res = knapsack(weights, values, c)
print('最大价值为:', res)
