#!/usr/bin/env python3


def load():
	memory = []
	with open("input.txt") as f:
		for l in f:
			l = l.rstrip()
			for m in l.split(','):
				memory.append(int(m))
	return memory


def init(memory, noun, verb):
	memory[1] = noun
	memory[2] = verb


def run(memory):
	ip = 0
	while memory[ip] != 99:
		if memory[ip] == 1:
			memory[memory[ip + 3]] = memory[memory[ip + 1]] + memory[memory[ip + 2]]
		elif memory[ip == 2]:
			memory[memory[ip + 3]] = memory[memory[ip + 1]] * memory[memory[ip + 2]]
		ip += 4
	
	return memory


def day2():
	memory = load()

	init(memory, 12, 2)

	memory = run(memory)

	return memory


def day2b():
	for noun in range(100):
		for verb in range(100):
			memory = load()

			init(memory, noun, verb)

			run(memory)

			if memory[0] == 19690720:
				print(f'{noun}, {verb}')
				exit()

			
if __name__ == '__main__':
	day2b()
