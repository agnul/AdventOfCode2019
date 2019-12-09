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
    base = 0
    p_out = []
    done = False
    while not done:
        word = str(memory[ip])
        op, modes = word[-2:].zfill(2), word[:-2].zfill(3)
        if op == '01':
            assert modes[-3] != '1'
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1], base), \
                           read_p(memory, modes[-2], memory[ip + 2], base), \
                           memory[ip + 3] if modes[-3] == '0' else base + memory[ip + 3]
            write_p(memory, dest, p1 + p2)
            ip += 4
        elif op == '02':
            assert modes[-3] != '1'
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1], base), \
                           read_p(memory, modes[-2], memory[ip + 2], base), \
                           memory[ip + 3] if modes[-3] == '0' else base + memory[ip + 3]
            write_p(memory, dest, p1 * p2)
            ip += 4
        elif op == '03':
            assert modes[-1] != '1'
            dest = memory[ip + 1] if modes[-1] == '1' else base + memory[ip + 1]
            write_p(memory, dest, p_in)
            ip += 2
        elif op == '04':
            p1 = read_p(memory, modes[-1], memory[ip + 1], base)
            p_out.append(p1) 
            ip += 2
        elif op == '05':
            p1, p2 = read_p(memory, modes[-1], memory[ip + 1], base), \
                     read_p(memory, modes[-2], memory[ip + 2], base)
            ip = p2 if p1 else ip + 3
        elif op == '06':
            p1, p2 = read_p(memory, modes[-1], memory[ip + 1], base), \
                     read_p(memory, modes[-2], memory[ip + 2], base)
            ip = ip + 3 if p1 else p2
        elif op == '07':
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1], base),  \
                           read_p(memory, modes[-2], memory[ip + 2], base), \
                           memory[ip + 3] if modes[-3] == '0' else base + memory[ip + 3]
            write_p(memory, dest, 1 if p1 < p2 else 0)
            ip += 4
        elif op == '08':
            p1, p2, dest = read_p(memory, modes[-1], memory[ip + 1], base), \
                           read_p(memory, modes[-2], memory[ip + 2], base), \
                           memory[ip + 3] if modes[-3] == '0' else base + memory[ip + 3]
            write_p(memory, dest, 1 if p1 == p2 else 0)
            ip += 4
        elif op == '09':
            p1 = read_p(memory, modes[-1], memory[ip + 1], base)
            base = base + p1
            ip += 2
        else:
            done = True
    return p_out


def read_p(memory, mode, address, base=0):
    if mode == '0':
        grow_memory(memory, address)
        return memory[address]
    elif mode == '1':
        return address
    elif mode == '2':
        grow_memory(memory, address + base)
        return memory[address + base]
    else:
        raise AssertionError('invalid address mode')


def write_p(memory, address, data):
    grow_memory(memory, address)
    memory[address] = data


def grow_memory(memory, max_address):
    mem_size = len(memory)
    if max_address > mem_size:
        memory.extend([0] * (mem_size + max_address + 1))


def solve_part_1():
    return run(load())


def solve_part_2():
    return run(load(), 2)


if __name__ == '__main__':
    print(f'{solve_part_1()}, {solve_part_2()}')
