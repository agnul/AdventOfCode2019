#!/usr/bin/env python3
def is_valid(p):
    return list(p) == sorted(p) and max(map(p.count, p)) > 1


def is_valid_for_part_2(p):
    return list(p) == sorted(p) and 2 in map(p.count, p)


def solve_part1():
    return sum(is_valid(str(n)) for n in range(183564, 657474 + 1))


def solve_part2():
    return sum(is_valid_for_part_2(str(n)) for n in range(183564, 657474 + 1))


if __name__ == '__main__':
    print(f'{solve_part1()}, {solve_part2()}')
