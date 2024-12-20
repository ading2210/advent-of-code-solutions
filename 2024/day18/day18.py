import pathlib
import math

input_file = "data.txt"
lines = pathlib.Path(input_file).read_text().split("\n")
data = [line.split(",") for line in lines]
data = [(int(x), int(y)) for x, y in data]

offsets = ((1, 0), (0, -1), (-1, 0), (0, 1))
size = 71
bytes_fallen = 1024

#example input only
if input_file == "data_test.txt":
  size = 7 
  bytes_fallen = 12

grid = []
for y in range(size):
  grid.append([])
  for x in range(size):
    grid[y].append(".")

def add_barriers(barriers):
  for x, y in barriers:
    grid[y][x] = "#"

def find_neighbors(x, y, nodes):
  neighbors = []
  for offset_x, offset_y in offsets:
    new_x, new_y = x + offset_x, y + offset_y
    if new_x < 0 or new_x >= size:
      continue
    if new_y < 0 or new_y >= size:
      continue
    if (new_x, new_y) not in nodes:
      continue
    neighbors.append(nodes[(new_x, new_y)])
  return neighbors

#a simpler version of my day 16 algorithm
def find_path_dijkstra():
  unvisited = {}
  visited = {}
  min_distance = 0
  end_node = None

  for y, row in enumerate(grid):
    for x, tile in enumerate(row):
      if tile == "#":
        continue
      unvisited[(x, y)] = [math.inf, x, y]
  unvisited[(0, 0)] = [0, 0, 0]

  while unvisited:
    x, y = min(unvisited, key=lambda i: unvisited[i][0])
    current_node = unvisited.pop((x, y))
    visited[(x, y)] = current_node
    distance = current_node[0]

    if distance == math.inf:
      break
    if (x, y) == (size-1, size-1):
      break

    neighbors = find_neighbors(x, y, unvisited)
    for neighbor in neighbors:
      old_distance, new_x, new_y = neighbor
      neighbor[0] = min(old_distance, distance + 1)
  
  return distance, visited, current_node

def get_shortest_path(visited, path, node):
  distance, x, y = node
  path.append((x, y))
  neighbors = find_neighbors(x, y, visited)
  for neighbor in neighbors:
    new_distance, new_x, new_y = neighbor
    if (new_x, new_y) in path:
      continue
    if new_distance < distance:
      get_shortest_path(visited, path, neighbor)
  return path

def get_first_blockage():
  distance, visited, end_node = find_path_dijkstra()
  shortest_path = get_shortest_path(visited, [], end_node)

  for x, y in data[bytes_fallen:]:
    grid[y][x] = "#"
    if (x, y) in shortest_path:
      distance, visited, end_node = find_path_dijkstra()
      shortest_path = get_shortest_path(visited, [], end_node)

      if distance == math.inf:
        return f"{x},{y}"
  
add_barriers(data[:bytes_fallen])
print(find_path_dijkstra()[0])
print(get_first_blockage())