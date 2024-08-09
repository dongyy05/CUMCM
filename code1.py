import numpy as np
from scipy.optimize import minimize
from scipy.stats import uniform

# Objective function
def fun1(x):
    return -x[0]**2 - x[1]**2 + x[0]*x[1] + 2*x[0] + 5*x[1]

# Nonlinear constraint function
def nonlfun1(x):
    return [-(x[0] - 1)**2 + x[1], 2*x[0] - 3*x[1] + 6]

# Bounds and constraints
x0 = np.array([0, 0])  # Initial guess
A = np.array([-2, 3])
b = 6
constraints = {'type': 'ineq', 'fun': lambda x: nonlfun1(x)}

# Optimization with different algorithms
# Interior-point algorithm equivalent
result = minimize(fun1, x0, method='trust-constr', constraints=constraints)
print("Interior-point result:", -result.fun)

# Sequential quadratic programming (SQP) equivalent
result = minimize(fun1, x0, method='SLSQP', constraints=constraints)
print("SQP result:", -result.fun)

# Change initial guess
x0 = np.array([1, 1])
result = minimize(fun1, x0, method='SLSQP', constraints=constraints)
print("SQP with different initial guess:", -result.fun)

# Using random search to find a better initial guess
n = 10000000  # Number of random samples
x1 = uniform.rvs(-100, 200, size=n)
x2 = uniform.rvs(-100, 200, size=n)
fmin = np.inf

for i in range(n):
    x = np.array([x1[i], x2[i]])
    if ((x[0] - 1)**2 - x[1] <= 0) and (-2*x[0] + 3*x[1] - 6 <= 0):
        result = -x[0]**2 - x[1]**2 + x[0]*x[1] + 2*x[0] + 5*x[1]
        if result < fmin:
            fmin = result
            x0 = x

print("Random search initial guess:", x0)
result = minimize(fun1, x0, method='SLSQP', constraints=constraints)
print("Optimization result with random initial guess:", -result.fun)
