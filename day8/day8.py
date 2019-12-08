#!/usr/bin/env python3
import sys


_in = ''
for line in open('input.txt', 'r'):
    _in += (line.rstrip())


def load_data(data, width, height, depth):
    image_data = [{'pixels': [], 'counters': [0] * 10} for _ in range(depth)]
    for offset in range(0, width * height * depth):
        layer = int(offset / (width * height))
        pixels = image_data[layer]['pixels']
        counters = image_data[layer]['counters']

        p = int(data[offset])
        pixels.append(p)
        counters[p] += 1
    return image_data


def solve_part_1(data, width, height):
    image_data = load_data(data, width, height, int(len(data) / (width * height)))
    res = None
    _min = sys.maxsize
    for layer in image_data:
        if layer['counters'][0] < _min:
            _min = layer['counters'][0]
            res = layer
    return res['counters'][1] * res['counters'][2]


def solve_part_2(data, width, height):
    depth = int(len(data) / (width * height))
    image_data = load_data(data, width, height, depth)
    password = [0] * (width * height)
    for offset in range(width * height):
        for layer in range(depth):
            if image_data[layer]['pixels'][offset] == 0:
                password[offset] = ' '
                break
            elif image_data[layer]['pixels'][offset] == 1:
                password[offset] = '#'
                break
    for i in range(height):
        start, finish = i * width, (i + 1) * width
        print("".join(password[start:finish]))


if __name__ == '__main__':
    print(f'{solve_part_1(_in, 25, 6)}')
    solve_part_2(_in, 25, 6)
