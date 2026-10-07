import numpy as np
import matplotlib.pyplot as plt
from engineering_math.ode import rk4

f = lambda t, y: -2*y + np.sin(t)
t, y = rk4(f, 1.0, 0.0, 10.0, 0.01)

plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("First-order ODE solved with RK4")
plt.grid(True)
plt.show()
