import random
import time

def create_grid(rows, cols):
     return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def get_neighbours(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= row + i < rows and 0 <= col + j < cols:
                neighbours.append(grid[row + i][col + j])
    return neighbours

def apply_rules(cell, neighbours):
    live_neighbours = sum(neighbours)
    if cell == 1 and (live_neighbours < 2 or live_neighbours > 3):
        return 0
    elif cell == 0 and live_neighbours == 3:
        return 1
    else:
        return cell

def next_generation(curr_gen):
    rows, cols = len(curr_gen), len(curr_gen[0])
    new_gen = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbours = get_neighbours(curr_gen, i, j)
            new_gen[i][j] = apply_rules(curr_gen[i][j], neighbours)
    return new_gen

def display(grid):
    for row in grid:
        for cell in row:
            print(u'\u25A0' if cell == 1 else ' ', end=' ')
        print()
    print()

if __name__ == "__main__":
    rows, cols = 25, 25
    game_grid = create_grid(rows, cols)
    while True:
        display(game_grid)
        game_grid = next_generation(game_grid)
        time.sleep(0.2)
        os.system('cls')
