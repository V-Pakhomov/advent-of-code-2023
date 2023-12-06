from typing import List, Set, Tuple


def solution(cards: List[Tuple[Set[str], Set[str]]]) -> int:
    result = 0

    for card in cards:
        points = 0
        w_nums, card_nums = card

        for num in card_nums:
            if num in w_nums:
                points = points * 2 or 1

        result += points

    return result


def get_cards(filename: str) -> List[str]:
    cards = list()

    with open(filename) as f:
        for line in f.readlines():
            numbers = line.split(':')[1]
            winning_numbers, card_numbers = map(lambda x: set(x.split()), numbers.split('|'))
            cards.append((winning_numbers, card_numbers))

    return cards


if __name__ == "__main__":
    cards = get_cards('input.txt')
    print(solution(cards))
