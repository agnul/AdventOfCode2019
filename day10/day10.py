#!/usr/bin/env python3
import fileinput


def collinear(a, b, c):
    if ((b[1] - a[1]) / (b[0] - a[0])) == ((c[1] - b[1]) / (c[0] - b[0])):
        return True
    return False


def in_between(a, b, c):
    return a[0] < c[0] < b[0] or a[1] < c[1] < b[1]


field = dict()
for y in enumerate(fileinput.input('input.txt')):
    print(y)
    for x in enumerate(y[1].rstrip()):
        print(x[1])
        if x[1] == '#':
            field[(x[0], y[0])] = []


for a in field:
    for b in field:
        for c in field:
            if a == b or b == c or a == c:
                continue
            if collinear(a, b, c):
                if in_between(a, b, c):
                    field[a].append(c)
                elif in_between(a, c, b):
                    field[a].append(b)

if __name__ == '__main__':
    print(field)


