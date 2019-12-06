#!/usr/bin/env python3
def load():
    program = []
    with open("input.txt") as file:
        for line in file:
            line = line.rstrip()
            for m in line.split(','):
                program.append(int(m))
    return program


def run(memory, p_in=1):
    ip = 0
    p_out = []
    done = False
    while not done:
        word = str(memory[ip])
        op, modes = word[-2:].zfill(2), word[:-2].zfill(3)
        if op == '01':
            assert modes[-3] == '0'
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1]), \
                           read_p(memory, modes[-2], memory[ip + 2]), \
                           memory[ip + 3]
            memory[dest] = int(p1) + int(p2)
            ip += 4
        elif op == '02':
            assert modes[-3] == '0'
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1]), \
                           read_p(memory, modes[-2], memory[ip + 2]), \
                           memory[ip + 3]
            memory[dest] = int(p1) * int(p2)
            ip += 4
        elif op == '03':
            assert modes[-1] == '0'
            dest = memory[ip + 1]
            memory[dest] = p_in
            ip += 2
        elif op == '04':
            p1 = read_p(memory, modes[-1], memory[ip + 1])
            p_out.append(p1)
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
    return run(load())


def solve_part_2():
    return run(load(), 5)


if __name__ == '__main__':
    print(f'{solve_part_1()}, {solve_part_2()}')
