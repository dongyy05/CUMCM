import numpy as np


def constraint(x):
    # Convert the input to a numpy array in case it's not already
    x = np.array(x)

    # Inequality constraints: Sum of the first 6 columns, minus 20
    g1 = np.sum(x[:6]) - 20  # For the first set
    g2 = np.sum(x[6:12]) - 20  # For the second set

    # Equality constraints: specific sums must equal [3, 5, 4, 7, 6, 11]
    k1 = x[0] + x[6] - 3
    k2 = x[1] + x[7] - 5
    k3 = x[2] + x[8] - 4
    k4 = x[3] + x[9] - 7
    k5 = x[4] + x[10] - 6
    k6 = x[5] + x[11] - 11

    # Combine inequality and equality constraints
    g = np.array([g1, g2])
    k = np.array([k1, k2, k3, k4, k5, k6])

    return g, k


# Example usage
x = np.random.rand(12)  # Example input vector
g, k = constraint(x)
print("Inequality constraints:", g)
print("Equality constraints:", k)
