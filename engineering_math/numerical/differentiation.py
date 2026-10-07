def central_difference(f, x, h=1e-5):
    """Approximate f'(x) with a central finite difference."""
    if h <= 0:
        raise ValueError("h must be positive.")
    return (f(x+h)-f(x-h))/(2*h)
