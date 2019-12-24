#!/usr/bin/env python3
import os


class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [['.'] * self.size for _ in range(self.size)]

    def cell_at(self, i, j):
        return self.cells[i][j]

    def set_cell_at(self, i, j, alive):
        self.cells[i][j] = '#' if alive else '.'

    def tick(self):
        next_gen = [['.'] * self.size for _ in range(self.size)]
        for i, row in enumerate(self.cells):
            for j, c in enumerate(row):
                count = self.count_alive(self.neighbours(i, j))
                if self.cell_at(i, j) == '#' and count != 1:
                    next_gen[i][j] = '.'
                elif self.cell_at(i, j) == '.' and (count == 1 or count == 2):
                    next_gen[i][j] = '#'
                else:
                    next_gen[i][j] = self.cell_at(i, j)
        self.cells = next_gen

    def count_alive(self, cells):
        return sum(self.cell_at(i, j) == '#' for i, j in cells)

    def neighbours(self, i, j):
        res = []
        if (i - 1) < 0:
            res.append((i + 1, j))
        elif (i + 1) == self.size:
            res.append((i - 1, j))
        else:
            res.append((i - 1, j))
            res.append((i + 1, j))
        if (j - 1) < 0:
            res.append((i, j + 1))
        elif (j + 1) == self.size:
            res.append((i, j - 1))
        else:
            res.append((i, j - 1))
            res.append((i, j + 1))
        return res

    def diversity(self):
        d = 0
        for i, row in enumerate(self.cells):
            for j, c in enumerate(row):
                d += 2 ** (self.size * i + j) if self.cell_at(i, j) == '#' else 0
        return d

    def __str__(self):
        s = ''
        for row in self.cells:
            s += ' '.join(row)
            s += os.linesep
        return s


def solve_part_1(lines):
    b = Board(len(lines))
    for i, l in enumerate(lines):
        for j, c in enumerate(l.rstrip()):
            b.set_cell_at(i, j, c == '#')
    seen = set()
    d = b.diversity()
    while d not in seen:
        seen.add(d)
        b.tick()
        d = b.diversity()
    return d


def solve_part_2(lines):
    b = Board(len(lines))
    for i, l in enumerate(lines):
        for j, c in enumerate(l.rstrip()):
            b.set_cell_at(i, j, c == '#')
    for _ in range(5):
        b.tick()
    print(b)
    pass


if __name__ == '__main__':
    lines = [
        '....#',
        '#..#.',
        '#..##',
        '..#..',
        '#....',
    ]
    # lines = open('input.txt', 'r').readlines()
    print(f'{solve_part_1(lines)}, {solve_part_2(lines)}')
