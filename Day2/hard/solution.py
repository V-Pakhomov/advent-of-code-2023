from typing import List
from dataclasses import dataclass


@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class Game:
    id: int
    rounds: List[Round]


def solution(games: List[Game]) -> int:
    result = 0

    for game in games:
        min_red = max(r.red for r in game.rounds)
        min_green = max(r.green for r in game.rounds)
        min_blue = max(r.blue for r in game.rounds)
        result += min_red * min_green * min_blue

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
