import math
import random

# Objective function
def objective_function(x):
    return x ** 2

# Annealing Algorithm
def simulated_annealing(objective, bounds, initial_temp, cooling_rate, max_iter):
    current_x = random.uniform(bounds[0], bounds[1])
    current_cost = objective(current_x)

    best_x = current_x
    best_cost = current_cost

    temperature = initial_temp

    for i in range(max_iter):
        candidate_x = current_x + random.uniform(-1, 1)
        candidate_x = max(min(candidate_x, bounds[1]), bounds[0]) 
        candidate_cost = objective(candidate_x)

        cost_diff = candidate_cost - current_cost
        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
            current_x = candidate_x
            current_cost = candidate_cost

            if candidate_cost < best_cost:
                best_x = candidate_x
                best_cost = candidate_cost

        temperature *= cooling_rate

    return best_x, best_cost

bounds = [-10, 10]
initial_temp = 1000
cooling_rate = 0.95
max_iter = 1000

best_solution, best_value = simulated_annealing(objective_function, bounds, initial_temp, cooling_rate, max_iter)

print(f"Best solution: x = {best_solution:.5f}, f(x) = {best_value:.5f}")
