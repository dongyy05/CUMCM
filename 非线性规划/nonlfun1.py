def nonlfun1(x):
    """
    非线性约束函数。
    
    Args:
    x (list or array-like): 变量列表或数组，包含 [x1, x2]。

    Returns:
    tuple: 返回一个包含两个元素的元组。
           - c: 不等式约束列表。
           - ceq: 等式约束列表，若无等式约束，则为空列表。
    """
    # 不等式约束条件: -(x1-1)^2 + x2 >= 0
    c = [(x[0] - 1)**2 - x[1]]  # 注意：等价于 (x1-1)^2 - x2 <= 0

    # 没有等式约束条件，返回空列表
    ceq = []

    return c, ceq


# 示例调用
x = [0, 0]  # 示例输入
c_value, ceq_value = nonlfun1(x)
print("不等式约束:", c_value)
print("等式约束:", ceq_value)
