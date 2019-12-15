#!/usr/env python3
import math
from collections import defaultdict


class Reaction:
    def __init__(self, s):
        lhs, rhs = s.split('=>')
        self.materials = []
        for e in lhs.split(','):
            q, o = e.split()
            self.materials.append((int(q), o))
        rhs = rhs.split()
        self.produces, self.quantity = rhs[1], int(rhs[0])

    def __str__(self):
        return f'{self.quantity} {self.produces} <- {self.materials}'


def parse_reactions(reactions_s):
    result = dict()
    for r_s in reactions_s:
        r = Reaction(r_s)
        result[r.produces] = r
    return result


def count_materials(available, q, p):
    if p == 'ORE':
        return q
    elif available[p] >= q:
        available[p] -= q
        return 0
    else:
        need, available[p] = q - available[p], 0
        batches = math.ceil(need / reactions[p].quantity)
        extra = batches * reactions[p].quantity - need
        available[p] += extra
        return sum(count_materials(available, batches * m[0], m[1]) for m in reactions[p].materials)


def solve_part_1():
    return count_materials(defaultdict(lambda: 0), 1, 'FUEL')


def solve_part_2():
    pass


if __name__ == '__main__':
    first_test = ['10 ORE => 10 A',
                  '1 ORE => 1 B',
                  '7 A, 1 B => 1 C',
                  '7 A, 1 C => 1 D',
                  '7 A, 1 D => 1 E',
                  '7 A, 1 E => 1 FUEL']

    second_test = ['9 ORE => 2 A',
                   '8 ORE => 3 B',
                   '7 ORE => 5 C',
                   '3 A, 4 B => 1 AB',
                   '5 B, 7 C => 1 BC',
                   '4 C, 1 A => 1 CA',
                   '2 AB, 3 BC, 4 CA => 1 FUEL']

    reactions = parse_reactions(open('input.txt', 'r'))

    print(f'{solve_part_1()}, {solve_part_2()}')
