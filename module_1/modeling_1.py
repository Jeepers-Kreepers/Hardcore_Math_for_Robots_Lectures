import sympy                                        # Импортирует библиотеку SymPy для символьных вычислений.
from sympy.plotting import plot                     # Импортирует функцию plot для построения графиков.

U = sympy.symbols('U')                              # Определяет символ U (напряжение).
T_m = sympy.symbols('T_m')                          # Определяет символ T_m (Константа / Электромеханическая Постоянная времени).
t = sympy.symbols('t')                              # Определяет символ t (время).
k_e = sympy.symbols('k_e', positive=True)    # Опр k_e > 0 коэффициент обратной ЭДС (конструктивная постоянная)
omega = sympy.Function('omega')                     # Определяет функцию omega(t) - угловая скорость rad/s

ode = sympy.Eq(omega(t).diff(t),
               U/(k_e*T_m) - omega(t)/T_m)          # Определяет уравнение для угловой скорости

# решение уравнения (определение изменения угловой скорости dc двигателя)
ode_sol = sympy.dsolve(ode, omega(t), ics={omega(0): 0})    # Решает уравнение исходя из начальных условий
ode_num = ode_sol.subs({U: 8, T_m: 0.08, k_e: 0.5})         # Преобразует символьные выражения в числовые


theta_eq = sympy.integrate(ode_sol.rhs, (t, 0, t))  # интегрирование уравнения для получения уравнения углового смещения
theta = sympy.Function('theta')  # обозначение функции углового смещения

ode_theta = sympy.Eq(theta(t).diff(t, 2), -theta(t).diff(t) / T_m + U / (T_m * k_e))  # дифференциальное уравнение углового смещения
ode_sol_theta = sympy.dsolve(ode_theta, theta(t), ics={theta(0): 0, theta(t).diff(t).subs(t, 0): 0})  # решение дифференциального уравнения
theta_num = ode_sol_theta.subs({k_e: 0.5, T_m: 0.08, U: 8})  # подстановка числовых значений в уравнение




if __name__ == '__main__':
    t0 = float(input("Введите начальное время (ex = 0): "))
    t_end = float(input("Введите конечное время (ex = 0.5): "))
    plot(ode_num.rhs, (t, t0, t_end))     # Построение графика угловой скорости в зависимости от времени
    plot(theta_num.rhs, (t, 0, 0.5), line_color='red',
         title='Разгон двигателя', xlabel='time,[sec]',
         ylabel='angle, [rad]')  # изображение графика с различными настройками