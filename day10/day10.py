#!/usr/bin/env python3
import fileinput

# for y in enumerate(['.#..#', '.....', '#####', '....#', '...##']):

field = dict()
for y in enumerate(fileinput.input('input.txt')):
    print(f'{y[1].rstrip()}')
    for x in enumerate(y[1].rstrip()):
        if x[1] == '#':
            field[(x[0], y[0])] = []


def collinear(a1, a2, a3):
    """Check if a1, a2 and a3 are collinear"""
    if ((a3[0] - a1[0]) * (a2[1] - a1[1])) == ((a3[1] - a1[1]) * (a2[0] - a1[0])):
        return True
    return False


def is_in_between(a1, a2, a3):
    """Check if a3 is in between a1 and a2"""
    if not collinear(a1, a2, a3):
        return False
    elif a1[0] != a2[0]:
        return a1[0] <= a3[0] <= a2[0] or a2[0] <= a3[0] <= a1[0]
    else:
        return a1[1] <= a3[1] <= a2[1] or a2[1] <= a3[1] <= a1[1]


def solve_part_1():
    max_count, pos = 0, None
    for a in field:
        count = 0
        for b in field:
            blocked = False
            for c in field:
                if a == b or b == c or a == c:
                    continue
                if is_in_between(a, b, c):
                    blocked = True
                    break
            if not blocked and a != b:
                count += 1
                field[a].append(b)
        if count > max_count:
            max_count, pos = count, a
    return f'pos: {pos} => {max_count}'


def solve_part_2():
    for a in field:
        field[a].sort(key=lambda b: (b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2)


if __name__ == '__main__':
    print(f'{solve_part_1()}, {solve_part_2()}')


