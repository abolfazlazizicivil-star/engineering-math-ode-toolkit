import numpy as np

def rk4_system(f, y0, t0, tf, h):
    """Solve y'=f(t,y) for vector-valued y using classical RK4."""
    if h <= 0 or tf <= t0:
        raise ValueError("Require h > 0 and tf > t0.")
    t = np.arange(t0, tf + h/2, h, dtype=float)
    y = np.empty((len(t), len(np.asarray(y0, dtype=float))))
    y[0] = np.asarray(y0, dtype=float)
    for i in range(len(t)-1):
        ti, yi = t[i], y[i]
        k1 = np.asarray(f(ti, yi))
        k2 = np.asarray(f(ti+h/2, yi+h*k1/2))
        k3 = np.asarray(f(ti+h/2, yi+h*k2/2))
        k4 = np.asarray(f(ti+h, yi+h*k3))
        y[i+1] = yi + h*(k1+2*k2+2*k3+k4)/6
    return t, y
