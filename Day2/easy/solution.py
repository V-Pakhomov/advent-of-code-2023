from typing import List
from dataclasses import dataclass

LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_feet_limit(self) -> bool:
        return self.red <= LIMITS['red'] and self.green <= LIMITS['green'] and self.blue <= LIMITS['blue']


@dataclass
class Game:
    id: int
    rounds: List[Round]


def solution(games: List[Game]) -> int:
    result = 0

    for game in games:
        if all([r.is_feet_limit() for r in game.rounds]):
            result += game.id

    return result


def get_games(filename: str) -> List[str]:
    games = list()
    index = 0

    with open(filename) as f:
        for line in f.readlines():
            index += 1
            game = Game(id=index, rounds=list())

            game_info = line.split(':')[1]
            raw_rounds = game_info.split(';')
            for round_info in raw_rounds:
                cubes = round_info.split(',')
                cubes = [c.split() for c in cubes]
                cubes = {color: int(number) for number, color in cubes}
                game.rounds.append(Round(**cubes))

            games.append(game)

    return games


if __name__ == "__main__":
    games = get_games('input.txt')
    print(solution(games))
