def bisection(f, a, b, tol=1e-10, max_iter=100):
    """Find a root of f on [a,b] using the bisection method."""
    fa, fb = f(a), f(b)
    if fa == 0: return a
    if fb == 0: return b
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    for _ in range(max_iter):
        m = (a+b)/2
        fm = f(m)
        if abs(fm) < tol or (b-a)/2 < tol:
            return m
        if fa*fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a+b)/2
