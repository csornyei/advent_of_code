from typing import Any, Optional
from time import sleep


Map = list[list[Any]]
Position = tuple[int, int]

map: Map = []


def letter_to_height(letter: str):
    if letter == "S":
        return 0
    elif letter == "E":
        return ord('z') - ord('a') + 1
    return ord(letter) - ord("a") + 1


def get_height(map: Map, pos: Position):
    return map[pos[0]][pos[1]]


def print_map(map: Map):
    print("\033[2J")
    print("\033[H")
    for row in map:
        for height in row:
            print(f"{height}", end="")
        print()


def find_start(map: Map):
    for row in map:
        for height in row:
            if height == 0:
                return (map.index(row), row.index(height))
    return (-1, -1)


def find_possible_starts(map: Map):
    possible_starts = [find_start(map)]
    for row_idx, row in enumerate(map):
        for height_idx, height in enumerate(row):
            if height == 1:
                possible_starts.append((row_idx, height_idx))
    return possible_starts


def find_end(map: Map):
    for row in map:
        for height in row:
            if height == ord('z') - ord('a') + 1:
                return (map.index(row), row.index(height))
    return (-1, -1)


def get_neighbors(map: Map, pos: Position):
    neighbors = []
    x, y = pos
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(map) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(map[0]) - 1:
        neighbors.append((x, y + 1))
    return neighbors


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path


def get_available_neighbors(map: Map, pos: Position, direction="UP"):
    current_height = get_height(map, pos)
    neighbors = get_neighbors(map, pos)
    available_neighbors = []
    for n in neighbors:
        n_height = get_height(map, n)
        if direction == "UP":
            if n_height - 1 == current_height:
                available_neighbors.append(n)
            elif n_height <= current_height:
                available_neighbors.append(n)
        elif direction == "DOWN":
            if n_height + 1 == current_height:
                available_neighbors.append(n)
            elif n_height >= current_height:
                available_neighbors.append(n)
    return available_neighbors


def astart(start: Position, goal: Position):
    open_set = set([start])

    gscore = {start: 0}

    fscore = {start: 0}

    came_from = {}

    while open_set:
        current = min(open_set, key=lambda x: fscore[x])
        if current == goal:
            return gscore[current], reconstruct_path(came_from, current)

        open_set.remove(current)

        for neighbor in get_available_neighbors(map, current):
            tentative_gscore = gscore[current] + 1
            if neighbor not in gscore or tentative_gscore < gscore[neighbor]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_gscore
                fscore[neighbor] = tentative_gscore + \
                    abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1])
                if neighbor not in open_set:
                    open_set.add(neighbor)
    return -1, []


def generate_visited_map(map: Map, visited: set[Position], start: Position):
    visited_map = []
    for line in map:
        visited_map.append([])
        for i in range(len(line)):
            visited_map[-1].append(".")
    for node in visited:
        visited_map[node[0]][node[1]] = "X"
    visited_map[start[0]][start[1]] = "S"
    return visited_map


def bfs(map: Map, start: Position):
    queue = [start]
    visited: set[Position] = set()
    lower_visiteds: set[Position] = set()
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if get_height(map, current) < 2:
            lower_visiteds.add(current)
        for neighbor in get_available_neighbors(map, current, "DOWN"):
            if neighbor not in visited:
                queue.append(neighbor)
    return visited, lower_visiteds


if __name__ == "__main__":
    file = open("../input.txt", "r")

    for line in file:
        line = line.strip()
        map.append([])
        for char in line:
            map[-1].append(letter_to_height(char))

    start_node = find_start(map)
    end_node = find_end(map)
    lengths = []
    gscore, path = astart(start_node, end_node)
    visited_map = []
    for line in map:
        visited_map.append([])
        for i in range(len(line)):
            visited_map[-1].append(".")
    print(len(path))
    visited, lower_visiteds = bfs(map, end_node)
    lower_visiteds_paths = []
    for node in lower_visiteds:  # type: ignore
        gscore, path = astart(node, end_node)
        lower_visiteds_paths.append(path)
    lowest_path = min(lower_visiteds_paths, key=lambda x: len(x))
    print(len(lowest_path))
