from typing import List, Set, Tuple
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    wr: int


def solution(races: List[Race]) -> int:
    result = 1

    for race in races:
        result *= sum(get_distance(race.time, t) > race.wr for t in range(race.time))

    return result


def get_distance(total_time, holding_time) -> int:
    return holding_time * (total_time - holding_time)


def get_races(filename: str) -> List[Race]:
    races = list()

    with open(filename) as f:
        times = f.readline().split(':')[1].split()
        wrs = f.readline().split(':')[1].split()
        for t, wr in zip(times, wrs):
            races.append(Race(time=int(t), wr=int(wr)))

    return races


if __name__ == "__main__":
    races = get_races('input.txt')
    print(solution(races))
