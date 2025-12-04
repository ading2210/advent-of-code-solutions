import pathlib
import itertools

lines = pathlib.Path("data.txt").read_text().split("\n")
board = [list(line) for line in lines]

offsets = [
  (-1, -1), (-1, 0), (-1, 1),
  (0,  -1),          (0,  1),
  (1,  -1), (1,  0), (1,  1)
]

def find_accessible():
  for y, row in enumerate(board):
    for x, char in enumerate(row):
      if char != "@":
        continue
      
      adjacent = 0
      for offset_y, offset_x in offsets:
        new_y, new_x = y + offset_y, x + offset_x
        if new_y < 0 or new_y >= len(board):
          continue
        if new_x < 0 or new_x >= len(row):
          continue
        if board[new_y][new_x] == "@":
          adjacent += 1
      
      if adjacent < 4:
        yield y, x

def part1():
  return len(list(find_accessible()))

def part2():
  total = 0
  while True:
    accessible = list(find_accessible())
    if not accessible:
      break
    total += len(accessible)
    for y, x in accessible:
      board[y][x] = "."

  return total

print(part1(), part2())