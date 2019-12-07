#!/usr/bin/env python3
satellites_of = dict()
orbits_around = dict()

for line in open('input.txt', 'r'):
    k, v = line.rstrip().split(')')

    if k in satellites_of:
        satellites_of[k].append(v)
    else:
        satellites_of[k] = [v]

    if v in orbits_around:
        orbits_around[v].append(k)
    else:
        orbits_around[v] = [k]


def count_satellites_of(p):
    count = 0
    if p in satellites_of:
        count += len(satellites_of[p])
        for q in satellites_of[p]:
            count += count_satellites_of(q)
    return count


def is_orbiting(s):
    r = []
    if s in orbits_around:
        r += orbits_around[s]
        for x in orbits_around[s]:
            r += is_orbiting(x)
    return r


def solve_part_1():
    nr_orbits = 0
    for p in satellites_of:
        nr_orbits += count_satellites_of(p)
    return nr_orbits


def solve_part_2():
    me = is_orbiting('YOU')
    santa = is_orbiting('SAN')
    r = len(set(me) ^ set(santa))
    return r


if __name__ == '__main__':
    print(f'{solve_part_1()}, {solve_part_2()}')
