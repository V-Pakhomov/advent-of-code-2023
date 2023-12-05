from typing import List, Optional

NUMBERS_LITERALS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def solution(document: List[str]) -> int:

    def find_first_number(line: str) -> Optional[int]:
        while line:
            if line[0].isdecimal():
                return int(line[0])

            for i, num in enumerate(NUMBERS_LITERALS, 1):
                if line.startswith(num):
                    return i

            line = line[1:]

    def find_last_number(line: str) -> Optional[int]:
        while line:
            if line[-1].isdecimal():
                return int(line[-1])

            for i, num in enumerate(NUMBERS_LITERALS, 1):
                if line.endswith(num):
                    return i

            line = line[:-1]

    result = 0

    for line in document:
        first = find_first_number(line)

        if first is None:
            continue

        last = find_last_number(line)
        result += first * 10 + last

    return result


def get_document(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    document = get_document('input.txt')
    print(solution(document))
