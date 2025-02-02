import pathlib
import functools
import math

stones = pathlib.Path("data.txt").read_text().split()
stones = [int(s) for s in stones]

@functools.cache
def engrave(stone):
  if stone == 0:
    return [1]
  digits = int(math.log(stone) + 1)
  if digits % 2 == 0:
    n = 10 ** (digits // 2)
    return [stone // n, stone % n]
  return [stone * 2024]

@functools.cache
def do_blink(stone, iterations):
  if iterations == 0: 
    return 1
  return sum([do_blink(s, iterations - 1) for s in engrave(stone)])

total_p1 = sum([do_blink(s, 25) for s in stones])
print(total_p1)
total_p2 = sum([do_blink(s, 75) for s in stones])
print(total_p2)
