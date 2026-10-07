# Engineering Mathematics & ODE Toolkit

A practical, open-source Python toolkit for numerical methods, ordinary differential equations, and engineering mathematics.

The project is designed for engineering students, educators, researchers, and developers who need transparent numerical algorithms that are easy to inspect, test, and extend.

## Why this project?

Engineering mathematics often requires moving between mathematical models and reliable numerical computation. This toolkit provides small, readable implementations of core methods instead of hiding the numerical process behind a large black-box API.

## Current capabilities

### Ordinary differential equations
- Explicit Euler method for first-order ODEs
- Classical fourth-order Runge-Kutta (RK4)
- Vector-valued ODE systems
- Second-order ODEs converted to first-order systems
- Mass-spring-damper engineering example

### Numerical mathematics
- Bisection root finding
- Composite trapezoidal integration
- Central finite-difference differentiation

### Engineering-oriented workflow
- Reproducible examples
- Unit-test coverage for core methods
- GitHub Actions continuous integration
- Mathematical notes explaining the implemented methods
- MIT-licensed source code

## Installation

Python 3.10+ is recommended.

```bash
git clone https://github.com/abolfazlazizicivil-star/engineering-math-ode-toolkit.git
cd engineering-math-ode-toolkit
python -m pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest -q
```

## Quick example

```python
from engineering_math.ode import rk4

f = lambda t, y: -2*y
t, y = rk4(f, y0=1.0, t0=0.0, tf=1.0, h=0.01)

print(y[-1])
```

For this example the numerical result approaches the analytical solution
`y(t)=exp(-2t)`.

## Engineering example

The repository includes a mass-spring-damper model:

```
m x'' + c x' + k x = F(t)
```

The implementation converts the second-order equation into a first-order system and solves it using RK4.

See `examples/engineering_mass_spring.py`.

## Project structure

```
engineering_math/
  ode/
    euler.py
    rk4.py
    systems.py
    second_order.py
  numerical/
    roots.py
    integration.py
    differentiation.py
examples/
tests/
docs/
```

## Development philosophy

The project prioritizes:
1. mathematically explicit implementations;
2. reproducible numerical examples;
3. automated tests;
4. readable APIs suitable for learning and extension;
5. engineering applications that connect equations to physical systems.

## Roadmap

Planned areas include adaptive RK45 integration, symbolic ODE utilities, Laplace transforms, Fourier series, boundary-value problems, finite-difference PDE solvers, heat-transfer models, beam models, RC circuits, vibration systems, and Jupyter notebooks.

See [docs/ROADMAP.md](docs/ROADMAP.md).

## Contributing

Issues and pull requests are welcome. New numerical methods should include tests, documentation, and a reproducible example when appropriate.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).
