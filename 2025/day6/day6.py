import pathlib
import re
import math
import itertools

lines = pathlib.Path("data.txt").read_text().split("\n")
operators = re.findall(r'\S+', lines[-1])

def solve_problem(numbers, operator):
  return sum(numbers) if operator == "+" else math.prod(numbers)

def part1():
  numbers = [map(int, re.findall(r'\d+', line)) for line in lines[:-1]]
  transposed = list(map(list, zip(*numbers)))

  problems = zip(transposed, operators)
  return sum(solve_problem(*problem) for problem in problems)

def part2():
  transposed = list(map(list, zip(*lines[:-1])))
  flattened = ["".join(row).strip() for row in transposed]
  grouped = itertools.groupby(flattened, lambda z: not z)
  numbers = [list(map(int, group)) for key, group in grouped if not key]

  problems = zip(numbers, operators)
  return sum(solve_problem(*problem) for problem in problems)

print(part1(), part2())