# # 递归算法
# def f(x):
#     """
#     递归函数，用于计算找零的最少硬币数。
#     参数x：找零的金额
#     返回值：最少硬币数量，如果无法找零，则返回无穷大
#     """
#     if x == 0:
#         return 0  # 如果找零金额为 0，则不需要任何硬币，直接返回 0
#     res = float('inf')  # 用一个很大的数表示无穷大，用于比较最小值
#     if x >= 2:
#         # 如果找零金额大于等于 2 元，尝试使用一枚 2 元硬币
#         res = min(f(x - 2) + 1, res)  # 递归调用 f 函数，并加上这一枚硬币
#     if x >= 5:
#         # 如果找零金额大于等于 5 元，尝试使用一枚 5 元硬币
#         res = min(f(x - 5) + 1, res)  # 递归调用 f 函数，并加上这一枚硬币
#     if x >= 7:
#         # 如果找零金额大于等于 7 元，尝试使用一枚 7 元硬币
#         res = min(f(x - 7) + 1, res)  # 递归调用 f 函数，并加上这一枚硬币
#     return res  # 返回最少硬币数量，如果无法找零，则返回无穷大
# n=int(input('请输入要拼的金额：'))
# res=f(n)
# print(res)

def coinChange(n):
    """
    用于计算找零的最少硬币数。
    参数n：要找零的金额
    返回值：最少硬币数量，如果无法找零，则返回-1
    """
    dp = [float('inf')] * (n + 1)  # 初始化动态规划数组
    dp[0] = 0  # 找零金额为 0 时，需要 0 枚硬币
    for i in range(1, n + 1):
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)
        if i >= 7:
            dp[i] = min(dp[i], dp[i - 7] + 1)
    if dp[n] != float('inf'):
        return dp[n]
    else:
        return -1
n=int(input('请输入要拼的金额：'))
res=coinChange(n)
print(res)