from typing import List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class MappedValue:
    value: int
    offset: int

    def __iter__(self):
        return iter((self.value, self.offset))


@dataclass
class Mapper:
    src: int
    dst: int
    length: int

    def __call__(self, value: int) -> Optional[MappedValue]:
        if self.src <= value < self.src + self.length:
            return MappedValue(self.dst + value - self.src, self.src + self.length - value - 1)


class MappersSet:

    def __init__(self) -> None:
        self.mappers = list()

    def add_mapper(self, mapper: Mapper) -> None:
        self.mappers.append(mapper)

    def __call__(self, value: int) -> MappedValue:
        for m in self.mappers:
            mapped_value = m(value)
            if mapped_value is not None:
                return mapped_value

        try:
            offset = min(o for m in self.mappers if (o := m.src - value + 1) >= 0)
        except ValueError:
            offset = float('inf')
        return MappedValue(value, offset)


def solution(seeds_ranges: List[int], mappers: List[MappersSet]) -> int:
    min_location = float('inf')

    for i in range(0, len(seeds_ranges), 2):
        seed_start = int(seeds_ranges[i])
        seed_len = int(seeds_ranges[i + 1])

        j = 0
        while j < seed_len:
            value = seed_start + j
            min_offset = float('inf')

            for m in mappers:
                value, offset = m(value)
                min_offset = min(offset, min_offset)

            min_location = min(value, min_location)
            j += 1 + min_offset

    return min_location


def get_seeds_and_mappers(filename: str) -> Tuple[List[int], List[MappersSet]]:
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
