import pathlib

board = pathlib.Path("data.txt").read_text().split("\n")

offsets = {
  ">": (0, 1),
  "<": (0, -1),
  "v": (1, 0),
  "^": (-1, 0)
}

reflections = {
  ("/", ">"): "^",
  ("/", "<"): "v",
  ("/", "^"): ">",
  ("/", "v"): "<",
  ("\\", ">"): "v",
  ("\\", "<"): "^",
  ("\\", "^"): "<",
  ("\\", "v"): ">"
}

def find_energized(initial_beam):
  beams = [initial_beam]
  energized = set()
  visited = set()

  while len(beams) > 0:
    for beam in beams[:]:
      y, x, direction = beam
      offset_y, offset_x = offsets[direction]
      new_y, new_x = y + offset_y, x + offset_x
      
      if new_y < 0 or new_x < 0 or new_y >= len(board) or new_x >= len(board[0]):
        beams.remove(beam)
        continue

      if (x, y, direction) in visited:
        beams.remove(beam)
        continue

      new_tile = board[new_y][new_x]
      visited.add((x, y, direction))
      energized.add((new_y, new_x))
      
      if new_tile in ("/", "\\"):
        new_direction = reflections[(new_tile, direction)]
        beam[0:3] = [new_y, new_x, new_direction]
        continue
      
      elif new_tile in ("-", "|"):
        if new_tile == "|" and direction in (">", "<"):
          beam[0:3] = [new_y, new_x, "^"]
          beams.append([new_y, new_x, "v"])
          continue
        elif new_tile == "-" and direction in ("v", "^"):
          beam[0:3] = [new_y, new_x, "<"]
          beams.append([new_y, new_x, ">"])
          continue
      
      beam[0:3] = [new_y, new_x, direction]
          
  return len(energized)

def part1():
  return find_energized([0, -1, ">"])

def part2():
  best = 0
  for y in range(0, len(board)):
    best = max(best, find_energized([y, -1, ">"]))
    best = max(best, find_energized([y, len(board[0]), "<"]))
  for x in range(0, len(board[0])):
    best = max(best, find_energized([-1, x, "v"]))
    best = max(best, find_energized([len(board[0]), x, "^"]))
  return best

print(part1(), part2())