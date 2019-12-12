#!/usr/bin/env python3
import re

_m_in = re.compile(r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$')


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def make_moon(s):
    moon = dict()

    match = _m_in.match(s)
    assert match is not None

    moon['p'] = list(map(int, [match.group(1), match.group(2), match.group(3)]))
    moon['v'] = [0, 0, 0]

    return moon


def apply_gravity(moons):
    for m1 in moons:
        for m2 in moons:
            if m1 == m2:
                continue
            for i in range(3):
                if m1['p'][i] < m2['p'][i]:
                    m1['v'][i] += 1
                elif m1['p'][i] > m2['p'][i]:
                    m1['v'][i] -= 1


def apply_velocity(moons):
    for m in moons:
        for i in range(3):
            m['p'][i] = m['p'][i] + m['v'][i]


def calculate_energy(moons):
    for m in moons:
        p = sum(map(abs, m['p']))
        k = sum(map(abs, m['v']))
        yield p * k


def get_state_on_axis(moons, i):
    p_i = [m['p'][i] for m in moons]
    v_i = [m['v'][i] for m in moons]
    return f'{p_i}, {v_i}'


def solve_part_1(moons, iterations):
    for _ in range(iterations):
        apply_gravity(moons)
        apply_velocity(moons)

    return sum(calculate_energy(moons))


def solve_part_2(origin):
    periods = []
    for i in range(3):
        seen = set()
        moons = origin.copy()
        seen.add(get_state_on_axis(moons, i))
        time = 0
        while True:
            apply_gravity(moons)
            apply_velocity(moons)
            time += 1
            state = get_state_on_axis(moons, i)
            if state in seen:
                periods.append(time)
                break
            seen.add(state)

    return lcm(lcm(periods[0], periods[1]), periods[2])


if __name__ == '__main__':
    moons = []
    origin = []
    for s in open('input.txt').readlines():
        moons.append(make_moon(s.rstrip()))
        origin.append(make_moon(s.rstrip()))

#    for s in ['<x=-1, y=0, z=2>', '<x=2, y=-10, z=-7>', '<x=4, y=-8, z=8>', '<x=3, y=5, z=-1>']:
#        moons.append(make_moon(s))
#        origin.append(make_moon(s))

#    for s in ['<x=-8, y=-10, z=0>', '<x=5, y=5, z=10>', '<x=2, y=-7, z=3>', '<x=9, y=-8, z=-3>']:
#        moons.append(make_moon(s))
#        origin.append(make_moon(s))

    print(f'{solve_part_1(moons, 1000)}, {solve_part_2(origin)}')
