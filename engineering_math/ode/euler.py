import numpy as np

def euler(f, y0, t0, tf, h):
    """Solve y'=f(t,y) with the explicit Euler method."""
    if h <= 0 or tf <= t0:
        raise ValueError("Require h > 0 and tf > t0.")
    t = np.arange(t0, tf + h/2, h, dtype=float)
    y = np.empty_like(t)
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i] + h * f(t[i], y[i])
    return t, y
