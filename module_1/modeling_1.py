import sympy
from sympy.plotting import plot

U = sympy.symbols('U') # V
T_m = sympy.symbols('T_m') #  time constant (s)
t = sympy.symbols('t')  # s
k_e = sympy.symbols('k_e', positive=True) # k_e > 0
omega = sympy.Function('omega') # rad/s

ode = sympy.Eq(omega(t).diff(t), U/(k_e*T_m) - omega(t)/T_m)

ode_sol = sympy.dsolve(ode, omega(t), ics={omega(0): 0})

ode_num = ode_sol.subs({U: 8, T_m: 0.08, k_e: 0.5})

if __name__ == '__main__':
    plot(ode_num.rhs, (t, 0, 0.5), line_color='red')