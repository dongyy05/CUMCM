def fun1(x):
    """
    Objective function for optimization.

    Args:
    x (list or array-like): A list or array containing the variables [x1, x2].

    Returns:
    float: The value of the objective function.
    """
    # Objective function: f(x) = -x1^2 - x2^2 + x1*x2 + 2*x1 + 5*x2
    return -x[0]**2 - x[1]**2 + x[0]*x[1] + 2*x[0] + 5*x[1]


# Example usage
x = [1, 2]  # Example input
f = fun1(x)
print("Objective function value:", f)
