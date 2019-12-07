#!/usr/bin/env python3
import itertools


def load():
    program = []
    with open("input.txt") as file:
        for line in file:
            line = line.rstrip()
            for m in line.split(','):
                program.append(int(m))
    return program


def test_load():
    return [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
            27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]


def run(memory, p_in):
    ip = 0
    p_out = None
    done = False
    while not done:
        word = str(memory[ip])
        op, modes = word[-2:].zfill(2), word[:-2].zfill(3)
        if op == '01':
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1]), \
                           read_p(memory, modes[-2], memory[ip + 2]), \
                           memory[ip + 3]
            memory[dest] = int(p1) + int(p2)
            ip += 4
        elif op == '02':
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1]), \
                           read_p(memory, modes[-2], memory[ip + 2]), \
                           memory[ip + 3]
            memory[dest] = int(p1) * int(p2)
            ip += 4
        elif op == '03':
            dest = memory[ip + 1]
            memory[dest] = p_in.pop()
            ip += 2
        elif op == '04':
            p1 = read_p(memory, modes[-1], memory[ip + 1])
            p_out = p1
            ip += 2
        elif op == '05':
            p1, p2 = read_p(memory, modes[-1], memory[ip + 1]), \
                     read_p(memory, modes[-2], memory[ip + 2])
            ip = p2 if p1 else ip + 3
        elif op == '06':
            p1, p2 = read_p(memory, modes[-1], memory[ip + 1]), \
                     read_p(memory, modes[-2], memory[ip + 2])
            ip = ip + 3 if p1 else p2
        elif op == '07':
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1]), \
                           read_p(memory, modes[-2], memory[ip + 2]), \
                           memory[ip + 3]
            memory[dest] = 1 if p1 < p2 else 0
            ip += 4
        elif op == '08':
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1]), \
                           read_p(memory, modes[-2], memory[ip + 2]), \
                           memory[ip + 3]
            memory[dest] = 1 if p1 == p2 else 0
            ip += 4
        else:
            done = True
    return p_out


def read_p(memory, mode, address):
    if mode == '0':
        return memory[address]
    elif mode == '1':
        return address
    else:
        raise AssertionError('invalid address mode')


def solve_part_1():
    max_thruster = 0
    phase_settings = [0, 1, 2, 3, 4]
    for p in itertools.permutations(phase_settings):
        out_a = run(load(), [0, p[0]])
        out_b = run(load(), [out_a, p[1]])
        out_c = run(load(), [out_b, p[2]])
        out_d = run(load(), [out_c, p[3]])
        out_e = run(load(), [out_d, p[4]])

        if out_e > max_thruster:
            max_thruster = out_e

    return max_thruster


def solve_part_2():
    pass


if __name__ == '__main__':
    print(f'{solve_part_1()}, {solve_part_2()}')
