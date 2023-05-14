import random
import math
import matplotlib.pyplot as plt
import numpy as np

def calc_center(monkeys):
    xx = 0.0
    yy = 0.0
    for m in monkeys:
        xx += m[0]
        yy += m[1]
    return (xx / len(monkeys), yy / len(monkeys))

def plot(Q_def, monkeys=[], lx=-5, rx=5, ly=-5, ry=5, gridsize=50, levels=(10), delay=0.01, i=0, gif=False): # levels = (50)
    a = np.linspace(lx, rx, gridsize)
    b = np.linspace(ly, ry, gridsize)
    _x, _y = np.meshgrid(a, b)
    c = plt.contour(_x, _y, Q_def(_x, _y), levels)
    center = calc_center(monkeys)
    for m in monkeys:
        if abs(m[0]) > 5 or abs(m[1]) > 5:
            continue
        c = plt.scatter(m[0], m[1])
        c = plt.plot((center[0], m[0]), (center[1], m[1]), c='g', linewidth=0.1)
    plt.grid()
    plt.show(block=False)
    plt.pause(delay)
    if gif:
        plt.savefig(f'gif_frames/{i}.png')
    plt.cla()


def init_monkeys(num_monkeys, lx=-5, rx=5, ly=-5, ry=5):
    monkeys = []
    for i in range(num_monkeys):
        x = random.uniform(lx, rx)
        y = random.uniform(ly, ry)
        monkeys.append((x, y))
    return monkeys

def local_jump(monkey, step_size):
    direction = random.uniform(0, 2 * math.pi)
    x = monkey[0] + step_size * math.cos(direction)
    y = monkey[1] + step_size * math.sin(direction)
    return (x, y)

def global_jump(monkey, all_monkeys, global_min, global_max):
    center = calc_center(all_monkeys)
    x1, y1 = monkey
    x2, y2 = center
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dx = (x2 - x1) / distance
    dy = (y2 - y1) / distance
    distance_from_first_point = random.uniform(global_min, global_max)
    x3 = x1 + distance_from_first_point * dx
    y3 = y1 + distance_from_first_point * dy
    # print('global', math.sqrt((x3 - x1)**2 + (y3 - y1)**2))
    return (x3, y3)

def monkey_optimization(func, num_monkeys, num_iterations, local_jump_size, local_jumps_count, global_jump_size_min, global_jump_size_max, lx=-5, rx=5, ly=-5, ry=5, show=False, gif=False):
    monkeys = init_monkeys(num_monkeys, lx, rx, ly, ry)
    local_counters = [0] * num_monkeys
    global_minimum_value = math.inf
    global_minimum_point = (0,0)
    for i in range(num_iterations):
        if show: print(i,  end='\r') # himel
        for j in range(num_monkeys):
            new_monkey = local_jump(monkeys[j], local_jump_size)
            if local_counters[j] >= local_jumps_count:
                monkeys[j] = global_jump(monkeys[j], monkeys, global_jump_size_min, global_jump_size_max)
                local_counters[j] = 0
            else:
                new_value = func(new_monkey[0], new_monkey[1])
                if new_value < func(monkeys[j][0], monkeys[j][1]):
                    monkeys[j] = new_monkey
                    local_counters[j] = 0
                    if new_value < global_minimum_value:
                        global_minimum_value = new_value
                        global_minimum_point = new_monkey
            local_counters[j] += 1
        if show:
            plot(func, monkeys, delay=0.01, i=i, gif=gif)

    # best_position = min(monkeys, key=lambda x: func(x[0], x[1]))

    return global_minimum_point