from typing import List


def solution(field: List[str]) -> int:
    height = len(field)
    width = len(field[0])
    result = 0

    for i in range(height):
        for j in range(width):
            if field[i][j] != '*':
                continue

            numbers = get_neighboring_numbers(field, i, j)

            if len(numbers) != 2:
                continue

            n1, n2 = numbers
            result += n1 * n2

    return result


def get_neighboring_numbers(field: List[str], row: int, column: int) -> int:
    height = len(field)
    width = len(field[0])

    numbers = list()

    for offset in (-1, 1):
        row_ = row + offset
        column_ = column + offset

        if 0 <= column_ < width and field[row][column_].isdigit():
            numbers.append(get_full_number(field[row], column_))

        if not 0 <= row_ < height:
            continue

        line = [0] * 3
        for j in (-1, 0, 1):
            if 0 <= column + j < width and field[row_][column + j].isdigit():
                line[j + 1] = 1
        if line == [1, 0, 1]:
            numbers += [get_full_number(field[row_], column - 1), get_full_number(field[row_], column + 1)]
        else:
            for i, v in enumerate(line, -1):
                if v:
                    numbers.append(get_full_number(field[row_], column + i))
                    break

    return numbers


def get_full_number(line: str, column: int):
    start = column
    while start - 1 >= 0 and line[start - 1].isdigit():
        start -= 1

    end = column
    while end < len(line) and line[end].isdigit():
        end += 1

    return int(line[start:end])


def get_field(filename: str) -> List[str]:
    with open(filename) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    field = get_field('input.txt')
    print(solution(field))
