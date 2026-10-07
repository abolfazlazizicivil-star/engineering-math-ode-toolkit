import numpy as np

def trapezoidal(x, y):
    """Composite trapezoidal integration for sampled data."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.size != y.size or x.size < 2:
        raise ValueError("x and y must have the same length >= 2.")
    return np.trapezoid(y, x)
