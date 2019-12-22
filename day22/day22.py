#!/usr/bin/env python3
def new_stack(deck):
    return deck[::-1]


def cut(deck, n):
    return list(deck[n:]) + list(deck[:n])


def deal_inc(deck, inc):
    size = len(deck)
    res = [None] * size
    res[0] = deck[0]
    for i in range(1, size):
        res[(i * inc) % size] = deck[i]
    return res


def solve_part_1(deck, shuffles):
    for shuffle, arg in shuffles:
        if shuffle == 'new':
            deck = new_stack(deck)
        elif shuffle == 'cut':
            deck = cut(deck, arg)
        elif shuffle == 'inc':
            deck = deal_inc(deck, arg)
    return deck.index(2019)


def solve_part_2():
    pass


if __name__ == '__main__':
    d = range(10007)
    s = []
    for line in open('input.txt', 'r').readlines():
        words = line.rstrip().split(' ')
        if words[0] == 'cut':
            s.append(('cut', int(words[1])))
        elif words[2] == 'increment':
            s.append(('inc', int(words[3])))
        elif words[2] == 'new':
            s.append(('new', None))

    print(f'Original {d}, shuffle: {s}')
    print(f'{solve_part_1(d, s)}, {solve_part_2()}')
