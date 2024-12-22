import pathlib

maze = pathlib.Path("data.txt").read_text().split("\n")
offsets = ((1, 0), (0, -1), (-1, 0), (0, 1))
threshold = 100

for y, row in enumerate(maze):
  for x, tile in enumerate(row):
    if tile == "S":
      start_x, start_y = x, y
    elif tile == "E":
      end_x, end_y = x, y

def get_path():
  x, y = start_x, start_y
  path = [(x, y)]
  while (x, y) != (end_x, end_y):
    x, y = path[-1]
    for offset_x, offset_y in offsets:
      new_x, new_y = x + offset_x, y + offset_y
      if maze[new_y][new_x] == "#":
        continue
      if (new_x, new_y) in path:
        continue
      path.append((new_x, new_y))
  return path

def find_cheats(path, max_distance):
  #find pairs of points in the path that are close to each other
  cheats = 0
  for i in range(0, len(path)-1):
    x1, y1 = path[i]
    for j in range(i+1, len(path)):
      x2, y2 = path[j]
      distance = abs(x1-x2) + abs(y1-y2)
      if distance > max_distance:
        continue
      savings = j - i - distance
      if savings >= threshold:
        cheats += 1
  return cheats

path = get_path()
print(find_cheats(path, 2))
print(find_cheats(path, 20))
