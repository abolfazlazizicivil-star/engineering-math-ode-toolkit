# Mathematical Notes

## Euler Method
For the initial-value problem y' = f(t,y), the explicit Euler method uses
y_(n+1) = y_n + h f(t_n,y_n).

## Classical RK4
The classical fourth-order Runge-Kutta method evaluates four slopes:
k1, k2, k3, and k4, then combines them as
y_(n+1) = y_n + h(k1 + 2k2 + 2k3 + k4)/6.

## Second-order systems
A x'' + B x' + C x = F(t) can be rewritten with v=x':
x' = v
v' = (F(t) - Bv - Cx)/A.
This representation allows standard first-order ODE solvers to be applied.
