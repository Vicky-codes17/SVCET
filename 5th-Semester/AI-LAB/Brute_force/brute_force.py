### Brute Force Approach to the Knapsack Problem

import itertools
import random
import time
from collections import namedtuple

Item = namedtuple('Item', ['name', 'size', 'value'])

def generate_knapsack_instance(N):
    """Generate a random knapsack problem instance with N items"""
    items = []
    used_names = set()
    
    for i in range(N):
        # Generate unique name
        while True:
            name = f"item_{random.randint(1, N*100)}"
            if name not in used_names:
                used_names.add(name)
                break
                
        size = random.randint(1, 5)
        value = random.randint(1, 10)
        items.append(Item(name, size, value))
    
    return items

def brute_force_knapsack(items, capacity):
    """Brute force solution to the knapsack problem"""
    max_value = 0
    best_combination = []
    
    # Try all possible combinations of items
    for r in range(1, len(items)+1):
        for combination in itertools.combinations(items, r):
            total_size = sum(item.size for item in combination)
            total_value = sum(item.value for item in combination)
            
            if total_size <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = combination
    
    return best_combination, max_value

def measure_performance(N, capacity_factor, runs=10):
    """Measure performance for a given problem size"""
    times = []
    capacity = int(N * capacity_factor)
    
    for _ in range(runs):
        items = generate_knapsack_instance(N)
        
        start_time = time.time()
        best_combination, max_value = brute_force_knapsack(items, capacity)
        end_time = time.time()
        
        times.append(end_time - start_time)
    
    avg_time = sum(times) / runs
    min_time = min(times)
    max_time = max(times)
    
    return avg_time, min_time, max_time

def run_performance_tests(capacity_factors, problem_sizes):
    """Run performance tests for different problem sizes and capacity factors"""
    results = {}
    
    for factor in capacity_factors:
        results[factor] = {}
        for size in problem_sizes:
            avg, min_t, max_t = measure_performance(size, factor)
            results[factor][size] = {
                'avg': avg,
                'min': min_t,
                'max': max_t
            }
            print(f"Capacity factor: {factor}, Problem size: {size}")
            print(f"  Avg time: {avg:.6f}s, Min: {min_t:.6f}s, Max: {max_t:.6f}s")
    
    return results

problem_sizes = [10, 12, 14, 16, 18, 20, 22]
capacity_factors = [2.5, 1.0, 4.0]

# Run performance tests
results = run_performance_tests(capacity_factors, problem_sizes)