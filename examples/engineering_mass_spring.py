import matplotlib.pyplot as plt
from engineering_math.ode import solve_second_order

m, c, k = 1.0, 0.4, 4.0
forcing = lambda t: 0.0

t, state = solve_second_order(m, c, k, forcing, x0=0.1, v0=0.0,
                              t0=0.0, tf=20.0, h=0.01)

plt.plot(t, state[:, 0], label="displacement")
plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Mass-Spring-Damper System")
plt.grid(True)
plt.legend()
plt.show()
