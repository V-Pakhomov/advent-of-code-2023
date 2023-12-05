from typing import List


def solution(document: List[str]) -> int:
    result = 0

    for line in document:
        for letter in line:
            if letter.isdecimal():
                line_number = int(letter) * 10
                break
        else:
            continue

        for letter in line[::-1]:
            if letter.isdecimal():
                line_number += int(letter)
                break

        result += line_number

    return result


def get_document(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    document = get_document('input.txt')
    print(solution(document))
