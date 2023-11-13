from sympy import symbols, exp, integrate, oo

# Variables
lambda_ = symbols('lambda', real=True, positive=True)
t = symbols('t', real=True)

# Def f(t)
f_t = lambda_ * exp(-lambda_ * t)

# Integranding
integral_result = integrate(f_t, (t, 0, oo))

print(f'Integral result: {integral_result}')
