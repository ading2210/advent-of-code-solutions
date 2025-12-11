import pathlib
import functools
import itertools
import math

lines = pathlib.Path("data.txt").read_text().split("\n")
lines_split = [line.split(": ") for line in lines]
devices = {id: devices_str.split(" ") for id, devices_str in lines_split}

@functools.cache
def paths(start, end):
  if start == end: return 1
  if not start in devices: return 0
  return sum(paths(output, end) for output in devices[start])

def paths_chained(*devices):
  return math.prod(paths(*pair) for pair in itertools.pairwise(devices))

def part1():
  return paths("you", "out")

def part2():
  return paths_chained("svr", "fft", "dac", "out") + paths_chained("svr", "dac", "fft", "out")

print(part1(), part2())