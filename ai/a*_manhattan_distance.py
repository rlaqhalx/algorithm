import heapq
from copy import deepcopy

world = [
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬛', '⬛', '⬛', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬛', '⬛', '⬛', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬛', '⬛', '⬛', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜'],
    ['⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜', '⬜']]

MOVES = [(0, -1), (1, 0), (0, 1), (-1, 0)]
start = (len(world) - 1, 0)
goal = (0, len(world) - 1)

world[start[0]][start[1]] = '🤖'
world[goal[0]][goal[1]] = '❤️'

rows, cols = len(world), len(world[0])

def green_mark_path(world, path):
    for node in path:
        if world[node[0]][node[1]] != '🤖' and world[node[0]][node[1]] != '❤️':
            world[node[0]][node[1]] = '🟩'


def print_path(world):
    for row in world:
        print("".join(row))


def check_path(world, new_row, new_col, visited):
    return 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and world[new_row][new_col] != '⬛'

def manhattan_distance(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

def calculate_fn(row, col, path):
    hn = manhattan_distance((row, col), goal)  # the estimated cost to reach the goal from the new node
    gn = len(path) + 1  # the cost of reaching the new node from the start
    return hn + gn  # the estimated total cost of the path through the new node

def a_star_search(world, start, goal, moves):
    new_world = deepcopy(world)
    visited = [[False] * cols for _ in range(rows)]
    heap = [(0, start, [])]
    visited[start[0]][start[1]] = True

    while heap:
        fn, (row, col), path = heapq.heappop(heap)
        if (row, col) == goal:
            green_mark_path(new_world, path)
            print_path(new_world)
            return None
        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy
            if check_path(new_world, new_row, new_col, visited):
                visited[new_row][new_col] = True
                fn = calculate_fn(new_row, new_col, path)
                heapq.heappush(heap, (fn, (new_row, new_col), path + [(row, col)]))
                if new_world[new_row][new_col] != '❤️' and new_world[new_row][new_col] != '🤖':
                    new_world[new_row][new_col] = '🟨'
    return None


result_1 = a_star_search(world, start, goal, MOVES)
print(result_1)