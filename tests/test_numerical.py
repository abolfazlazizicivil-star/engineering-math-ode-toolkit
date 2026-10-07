import numpy as np
from engineering_math.numerical import bisection, trapezoidal, central_difference

def test_bisection():
    assert abs(bisection(lambda x: x*x-2, 0, 2)-np.sqrt(2)) < 1e-8

def test_integration():
    x=np.linspace(0,1,1001)
    assert abs(trapezoidal(x,x*x)-1/3) < 1e-6

def test_differentiation():
    assert abs(central_difference(lambda x:x*x, 2)-4) < 1e-5
