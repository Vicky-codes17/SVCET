### Write a program to implement Hill Climbing Algorithm  f(x) = -x^2 + 10x

def hill_climbing(f, x_start, step_size, max_iterations):
    x = x_start
    for i in range(max_iterations):
        current_value = f(x)
        next_value = f(x + step_size)
        
        if next_value > current_value:
            x += step_size
        else:
            break  
    return x, f(x)


# Objective Function f(x) = -x^2 + 10x
def objective_function(x):
    return -x**2 + 10*x

x_start = 0
step_size = 0.1
max_iterations = 1000

# Run Hill Climbing
solution, value = hill_climbing(objective_function, x_start, step_size, max_iterations)

print(f"Peak found at x = {solution}, f(x) = {value}")