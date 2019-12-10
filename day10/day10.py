#!/usr/bin/env python3
import fileinput


def collinear(a, b, c):
    if ((b[1] - a[1]) * (c[0] - b[0]))  == ((c[1] - b[1]) * (b[0] - a[0])):
        return True
    return False


def in_between(a, b, c):
    return a <= c <= b or a <= c <= b


field = dict()
for y in enumerate(fileinput.input('input.txt')):
    for x in enumerate(y[1].rstrip()):
        if x[1] == '#':
            field[(x[0], y[0])] = []


for a in field:
    for b in field:
        for c in field:
            if a == b or b == c or a == c:
                continue
            if collinear(a, b, c):
                if a[0] != b[0]:
                    if in_between(a[0], c[0], b[0]):
                        break
                else:
                    if in_between(a[1], c[1], b[1]):
                        break
            field[a].append(c)


if __name__ == '__main__':
    print(field)
    print(max (len(field[f]) for f in field))


