#!/usr/bin/env python3

A, B = open('input.txt').read().split()
A, B = [x.split(',') for x in [A, B]]

DX = dict(zip('LRUD', [-1, 1, 0, 0]))
DY = dict(zip('LRUD', [0, 0, 1, -1]))


def get_points(a):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in a:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


PA = get_points(A)
PB = get_points(B)

both = set(PA.keys()) & set(PB.keys())
part1 = min(abs(x) + abs(y) for x, y in both)
part2 = min(PA[p] + PB[p] for p in both)

print(part1, part2)
