from typing import List, Optional


def solution(field: List[str]) -> int:
    height = len(field)
    width = len(field[0])
    result = 0

    for i in range(height):
        for j in range(width):
            if not field[i][j].isdigit() or j > 0 and field[i][j - 1].isdigit():
                continue

            number = get_number_if_touching_symbol(field, i, j)
            if number is not None:
                result += number

    return result


def get_number_if_touching_symbol(field: List[str], row: int, column: int) -> Optional[int]:

    def is_symbol(row: int, column: int) -> bool:
        char = field[row][column]
        return char != '.' and not char.isdecimal()

    height = len(field)
    width = len(field[0])
    line = field[row]

    num_len = 1
    while column + num_len < width and line[column + num_len].isdigit():
        num_len += 1

    left_right_coords = [(row + i, column + j) for i in (-1, 0, 1) for j in (-1, num_len)]
    top_bottom_coords = [(row + i, column + j) for i in (-1, 1) for j in range(num_len)]
    valid_coords = list(filter(lambda x: 0 <= x[0] < height and 0 <= x[1] < width,
                               left_right_coords + top_bottom_coords))
    if any(is_symbol(i, j) for i, j in valid_coords):
        return int(line[column:column + num_len])


def get_field(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    field = get_field('input.txt')
    print(solution(field))
