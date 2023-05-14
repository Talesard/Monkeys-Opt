from monkey_opt import monkey_optimization
import numpy as np

def himel(x, y):
    return  (x**2 + y - 11)**2 + (x + y**2 - 7)**2 #(1 - x) ** 2 + 100 * (y - x ** 2) ** 2

def matyas(x, y):
    return 0.26 * (x**2 + y**2) - 0.48 * x * y

def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

def goldstein_price(x, y):
    return ((1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))
            * (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)))

def rastrigin(x, y):
    A = 10
    return A*2 + (x**2 - A*np.cos(2*np.pi*x)) + (y**2 - A*np.cos(2*np.pi*y))

func = rastrigin
init_pos = 5

best_position = monkey_optimization(func=func,
                                    num_monkeys=50, # 20
                                    num_iterations=200, # 200
                                    local_jump_size=0.05, #0.05
                                    local_jumps_count=10, # 10
                                    global_jump_size_min =-2, # -1
                                    global_jump_size_max=2, # 1
                                    lx=-init_pos,
                                    rx=init_pos,
                                    ly=-init_pos,
                                    ry=init_pos,
                                    show=True,
                                    gif=True)

print("Лучшее решение: ", best_position)
print("Значение функции в лучшей точке: ", func(best_position[0], best_position[1]))
