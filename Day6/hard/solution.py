from dataclasses import dataclass


@dataclass
class Race:
    time: int
    wr: int


def solution(race: Race) -> int:
    return sum(get_distance(race.time, t) > race.wr for t in range(race.time))


def get_distance(total_time, holding_time) -> int:
    return holding_time * (total_time - holding_time)


def get_race(filename: str) -> Race:
    with open(filename) as f:
        time = int(''.join(f.readline().split(':')[1].split()))
        wr = int(''.join(f.readline().split(':')[1].split()))
        return Race(time=time, wr=wr)


if __name__ == "__main__":
    race = get_race('input.txt')
    print(solution(race))
