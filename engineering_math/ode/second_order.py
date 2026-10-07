from .systems import rk4_system

def solve_second_order(a, b, c, forcing, x0, v0, t0, tf, h):
    """Solve a*x'' + b*x' + c*x = forcing(t) by converting it to a first-order system."""
    if a == 0:
        raise ValueError("Coefficient a must be nonzero.")
    def system(t, state):
        x, v = state
        return [v, (forcing(t) - b*v - c*x)/a]
    return rk4_system(system, [x0, v0], t0, tf, h)
