import numpy as np
from engineering_math.ode import euler, rk4, solve_second_order

def test_euler_decay():
    t, y = euler(lambda t,y: -2*y, 1.0, 0, 1, 0.01)
    assert abs(y[-1]-np.exp(-2)) < 0.02

def test_rk4_decay():
    t, y = rk4(lambda t,y: -2*y, 1.0, 0, 1, 0.01)
    assert abs(y[-1]-np.exp(-2)) < 1e-7

def test_second_order_shape():
    t, state = solve_second_order(1, 0.2, 4, lambda t: 0, 0.1, 0, 0, 1, 0.01)
    assert state.shape[1] == 2
