import pathlib
import itertools

lines = pathlib.Path("data.txt").read_text().split("\n")
lines_split = [line.split(",") for line in lines]
tiles = [(int(y), int(x)) for x, y in lines_split]

#https://stackoverflow.com/a/9997374/21330993
def ccw(a, b, c):
  return (c[0] - a[0]) * (b[1] - a[1]) > (b[0] - a[0]) * (c[1] - a[1])
def intersect(a, b, c, d):
  return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

def is_invalid(y1, x1, y2, x2, dy, dx):
  corners = [(y1, x1), (y1, x1 - dx), (y1 - dy, x1), (y2, x2)]
  corners.sort()
  inner_corners = [
    (corners[0][0] + 1, corners[0][1] + 1),
    (corners[1][0] + 1, corners[1][1] - 1),
    (corners[2][0] - 1, corners[2][1] + 1),
    (corners[3][0] - 1, corners[3][1] - 1),
  ]
  for i in range(len(inner_corners)):
    edge = inner_corners[i-1], inner_corners[i]
    for segment in segments:
      if intersect(*edge, *segment):
        return True

segments = [(tiles[i-1], tiles[i]) for i in range(len(tiles))]
p1_solution, p2_solution = 0, 0

for (y1, x1), (y2, x2) in itertools.combinations(tiles, 2):
  dy, dx = y1 - y2, x1 - x2
  area = (abs(dy) + 1) * (abs(dx) + 1)
  if dy == 0 or dx == 0:
    continue
  if area > p1_solution:
    p1_solution = area
  if area > p2_solution and not is_invalid(y1, x1, y2, x2, dy, dx):
    p2_solution = area

print(p1_solution, p2_solution)