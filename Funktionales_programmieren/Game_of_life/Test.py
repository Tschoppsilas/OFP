from typing import Callable, Generator, List, Tuple

Cell_Check = Callable[[int, int], bool]
Rule = Callable[[Cell_Check, int, int], bool]
Grid = tuple[tuple[bool, ...], ...]
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
        def cell_check(x: int, y: int) -> bool:
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]
        new_grid = tuple(
            tuple(
                rule(cell_check, x, y) for y in range(len(grid[0]))
            )for x in range(len(grid)))
        return new_grid
    return step

def generations(start_grid: Grid, step_function: Step_Function) -> Generator[Grid, None, None]:
    current_grid = start_grid
    seen_grids = set()

    while current_grid not in seen_grids:
        seen_grids.add(current_grid)
        yield current_grid
        current_grid = step_function(current_grid)

def print_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(["#" if cell else "." for cell in row]))
    print("\n")


def strings_to_grid(strings: list[str]) -> Grid:
    return tuple(
        tuple(cell == "#" for cell in row)
        for row in strings
    )


if __name__ == "__main__":
    start_grid_strings = [
            ".......####....",
            "...########....",
            "...#.####.#....",
            "...########....",
            "...............",
            "...............",
            "....####.......",
            "....#..........",
            ".....#.........",
            "...###.........",
            "....#..........",
            "..............."
    ]

    start_grid = strings_to_grid(start_grid_strings)

    conway_step = step_func(conway_rule)

    gen = generations(start_grid, conway_step)

    generation_count = 0
    for current_grid in gen:
        print(f"Generation {generation_count}:")
        print_grid(current_grid)
        generation_count += 1
