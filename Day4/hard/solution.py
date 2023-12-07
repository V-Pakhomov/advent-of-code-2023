from typing import List, Set, Tuple


def solution(cards: List[Tuple[Set[str], Set[str]]]) -> int:
    cards_count = [1] * len(cards)

    for i, card in enumerate(cards):
        card_count = cards_count[i]
        w_nums, card_nums = card
        points = len(card_nums & w_nums)

        for j in range(points):
            cards_count[i + j + 1] += card_count

    return sum(cards_count)


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
