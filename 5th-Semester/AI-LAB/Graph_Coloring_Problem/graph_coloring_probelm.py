### Graph Coloring Problem using Backtracking

def layout(N, C, L):
    from collections import defaultdict

    conflict_graph = defaultdict(list)
    for x, y in L:
        conflict_graph[x].append(y)
        conflict_graph[y].append(x)

    assignment = {}

    def is_safe(guest, table):
        for neighbor in conflict_graph[guest]:
            if assignment.get(neighbor) == table:
                return False
        return True

    def backtrack(guest_index):
        if guest_index == N:
            return True  

        for table in range(C):
            if is_safe(guest_index, table):
                assignment[guest_index] = table
                if backtrack(guest_index + 1):
                    return True
                del assignment[guest_index]  # Backtrack

        return False

    if backtrack(0):
        return assignment
    else:
        return False


if __name__ == "__main__":
    N = 4
    C = 2
    L = [(0, 1), (1, 2), (2, 3), (3, 0)]

    # Print the raw assignment dictionary
    print(layout(N, C, L))