from typing import Any, List, Optional, Set, Tuple
from dataclasses import dataclass


@dataclass
class Mapper:
    src: List[int]
    dst: List[int]
    length: int

    def __call__(self, value: int) -> Optional[int]:
        if self.src <= value < self.src + self.length:
            return self.dst + value - self.src


class MappersSet:

    def __init__(self) -> None:
        self.mappers = list()

    def add_mapper(self, mapper: Mapper) -> None:
        self.mappers.append(mapper)

    def __call__(self, value: int) -> int:
        for m in self.mappers:
            mapped_value = m(value)
            if mapped_value is not None:
                return mapped_value
        return value


def solution(seeds: List[int], mappers: List[MappersSet]) -> int:
    min_location = float('inf')

    for seed in seeds:
        value = int(seed)

        for m in mappers:
            value = m(value)

        min_location = min(value, min_location)

    return min_location


def get_seeds_and_mappers(filename: str) -> Tuple[List[str], List[MappersSet]]:
    mappers = list()

    with open(filename) as f:
        seeds_line = f.readline()
        seeds = seeds_line.split(':')[1].split()

        for line in f.read().splitlines():
            if not line:
                continue

            if line.endswith(':'):
                mapper_set = MappersSet()
                mappers.append(mapper_set)
                continue

            dst, src, length = map(int, line.split())
            mapper_set.add_mapper(Mapper(src, dst, length))

    return seeds, mappers


if __name__ == "__main__":
    seeds, mappers = get_seeds_and_mappers('input.txt')
    print(solution(seeds, mappers))
