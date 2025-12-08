import pathlib
import itertools
import collections
import math

lines = pathlib.Path("data.txt").read_text().split("\n")
boxes = [tuple(map(int, line.split(","))) for line in lines]
p1_iterations = 1000

def merge_circuits(circuits, id1, id2):
  circuit1 = circuits[id1]
  circuit2 = circuits[id2]
  if circuit1 == circuit2:
    return
  for i, circuit in enumerate(circuits):
    if circuit == circuit2:
      circuits[i] = circuit1

distances = []
best_distance = math.inf
circuits = list(range(len(boxes)))

for box1, box2 in itertools.combinations(boxes, 2):
  distance = math.dist(box1, box2)
  if distance < best_distance:
    best_distance = distance
  elif distance > best_distance * 20:
    continue #optimization: don't bother with box pairs very far away
  distances.append((distance, boxes.index(box1), boxes.index(box2)))
distances.sort()

for i, (distance, id1, id2) in enumerate(distances):
  merge_circuits(circuits, id1, id2)

  if i == p1_iterations - 1:
    circuits_counted = collections.Counter(circuits)
    largest_circuits = circuits_counted.most_common(3)
    p1_solution = math.prod(count for circuit, count in largest_circuits)
    print(p1_solution)

  if len(set(circuits)) == 1:
    break

p2_solution = boxes[id1][0] * boxes[id2][0]
print(p2_solution)
