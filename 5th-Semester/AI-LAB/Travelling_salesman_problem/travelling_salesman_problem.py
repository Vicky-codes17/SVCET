import itertools

def tsp_brute_force(graph, start):
    # Number of cities
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)
    min_path = None
    min_cost = float('inf')
    for perm in itertools.permutations(cities):
        current_cost = 0
        current_path = [start] + list(perm) + [start]
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i+1]]

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path
    return min_path, min_cost
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, cost = tsp_brute_force(graph, 0)
print("Minimum Cost Path:", path)
print("Total Cost:", cost)