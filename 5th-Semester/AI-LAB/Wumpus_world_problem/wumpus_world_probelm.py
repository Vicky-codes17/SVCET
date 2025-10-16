### Write a program to implement the Wumpus World problem.

# Constants
EMPTY = ' '
PIT = 'P'
WUMPUS = 'W'
GOLD = 'G'
AGENT = 'A'

world = [
    [' ', ' ', ' ', 'P'],
    [' ', 'W', ' ', ' '],
    [' ', ' ', ' ', ' '],
    ['A', ' ', ' ', 'G']
]

# Agent position
agent_pos = [3, 0]

visited = [[False for _ in range(4)] for _ in range(4)]

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def is_valid(x, y):
    return 0 <= x < 4 and 0 <= y < 4
def dfs(x, y):
    if not is_valid(x, y) or visited[x][y]:
        return False
    visited[x][y] = True

    if world[x][y] == PIT or world[x][y] == WUMPUS:
        print(f"Agent died at ({x}, {y})!")
        return False
  
    if world[x][y] == GOLD:
        print(f"Gold found at ({x}, {y})! Agent wins!")
        return True
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y) and not visited[new_x][new_y]:
            if dfs(new_x, new_y):
                print(f"Moved to ({new_x}, {new_y})")
                return True
    return False

# Start search
print("Starting DFS to find the gold...")
if not dfs(agent_pos[0], agent_pos[1]):
    print("No path to gold found!")