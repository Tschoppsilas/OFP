from typing import Callable, Generator, Set, Tuple

Cell_Check = Callable[[int, int], bool]
Rule = Callable[[Cell_Check, int, int], bool]
Grid = Set[Tuple[int, int]]
Step_Function = Callable[[Grid], Grid]

def conway_rule(cell_check: Cell_Check, x: int, y: int) -> bool:
    neighbors = (
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
    )
    sum_neighbors = sum(map(lambda pos: cell_check(*pos), neighbors))
    return (2 <= sum_neighbors <= 3) if cell_check(x, y) else (sum_neighbors == 3)

def step_func(rule: Rule) -> Step_Function:
    def step(grid: Grid) -> Grid:
        # geändert
        def cell_check(x: int, y: int) -> bool:
            return (x, y) in grid
        new_grid = set()
        #neu, da der Rand keine begrenzung ist und somit auch die nächste zeile angeschaut wird
        potential_cells = grid | { (x + dx, y + dy) for x, y in grid for dx in range(-1, 2) for dy in range(-1, 2) }
        for x, y in potential_cells:
            if rule(cell_check, x, y):
                new_grid.add((x, y))
        return new_grid
    return step

def generations(start_grid: Grid, step_function: Step_Function) -> Generator[Grid, None, None]:
    current_grid = start_grid
    seen_grids = set()
    #geändert um unveränderbare zustände zu speichern
    while frozenset(current_grid) not in seen_grids:
        seen_grids.add(frozenset(current_grid))
        yield current_grid
        current_grid = step_function(current_grid)
#geändert, da das Grid unendlich werden soll
def print_grid(grid: Grid) -> None:
    if not grid:
        print("\n")
        return
    min_x = min(x for x, y in grid)
    max_x = max(x for x, y in grid)
    min_y = min(y for x, y in grid)
    max_y = max(y for x, y in grid)
    for y in range(min_y, max_y + 1):
        print("".join("#" if (x, y) in grid else "." for x in range(min_x, max_x + 1)))
    print("\n")
#Konvertiere Zeichenketten in ein unendliches Gitter
def strings_to_grid(strings: list[str]) -> Grid:
    return {(x, y) for y, row in enumerate(strings) for x, cell in enumerate(row) if cell == "#"}

if __name__ == "__main__":
    start_grid_strings = [
        "#####",
        ".....",
        "#.#.#",
        ".....",
        "..#.."
    ]

    start_grid = strings_to_grid(start_grid_strings)

    conway_step = step_func(conway_rule)

    gen = generations(start_grid, conway_step)

    generation_count = 0
    for current_grid in gen:
        print(f"Generation {generation_count}:")
        print_grid(current_grid)
        generation_count += 1
