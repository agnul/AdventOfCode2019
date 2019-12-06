#!/usr/bin/env python3
from math import floor

modules = [int(m) for m in open('input.txt').read().split()]


def fuel_for_mass(m):
	return floor(m / 3.0) - 2


def fuel_for_mass_and_fuel(mass):
	total = 0
	m = fuel_for_mass(mass)
	while m > 0:
		total += m
		m = fuel_for_mass(m)
	return total


def solve_part_1():
	mass = 0
	for m in modules:
		mass += fuel_for_mass(m)
	return mass


def solve_part_2():
	mass = 0
	for m in modules:
		mass += fuel_for_mass_and_fuel(m)
	return mass


if __name__ == "__main__":
	print(f'{solve_part_1()}, {solve_part_2()}')
