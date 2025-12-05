import pathlib
import itertools

fresh_ranges_str, ids_str = pathlib.Path("data.txt").read_text().split("\n\n")
ingredient_ids = [int(line) for line in ids_str.split("\n")]
fresh_ranges_split = [line.split("-") for line in fresh_ranges_str.split("\n")]
fresh_ranges = [(int(r[0]), int(r[1])) for r in fresh_ranges_split]

def part1():
  spoiled = 0
  for id in ingredient_ids:
    spoiled += any(id >= start and id <= end for start, end in fresh_ranges)
  return spoiled

def part2():
  merged_ranges = set(fresh_ranges)
  overlaps = True
  while overlaps:
    overlaps = False
    for (start, end), (other_start, other_end) in itertools.combinations(merged_ranges, 2):
      if max(start, other_start) <= min(end, other_end): 
        merged_ranges -= {(start, end), (other_start, other_end)}
        merged_ranges.add((min(start, other_start), max(end, other_end)))
        overlaps = True
  
  return sum(end - start + 1 for start, end in merged_ranges)

print(part1(), part2())
