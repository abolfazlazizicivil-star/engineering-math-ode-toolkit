import numpy as np

def rk4(f, y0, t0, tf, h):
    """Solve y'=f(t,y) with the classical fourth-order Runge-Kutta method."""
    if h <= 0 or tf <= t0:
        raise ValueError("Require h > 0 and tf > t0.")
    t = np.arange(t0, tf + h/2, h, dtype=float)
    y = np.empty_like(t)
    y[0] = y0
    for i in range(len(t)-1):
        ti, yi = t[i], y[i]
        k1 = f(ti, yi)
        k2 = f(ti + h/2, yi + h*k1/2)
        k3 = f(ti + h/2, yi + h*k2/2)
        k4 = f(ti + h, yi + h*k3)
        y[i+1] = yi + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return t, y
