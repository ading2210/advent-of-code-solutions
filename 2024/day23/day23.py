import pathlib
import collections
import itertools
import functools

lines = pathlib.Path("data.txt").read_text().split("\n")

#i have no knowledge of graph theory. this code reflects that

network = collections.defaultdict(lambda: [])
for line in lines:
  c1, c2 = line.split("-")
  network[c1].append(c2)
  network[c2].append(c1)

def check_pair(c1, c2):
  return c1 in network[c2]

def check_multi(computers):
  for c1, c2 in itertools.combinations(computers, 2):
    if not check_pair(c1, c2):
      return False
  return True

def check_names(triple):
  for computer in triple:
    if computer[0] == "t":
      return True
  return False

sets_of_three = itertools.combinations(network.keys(), 3)
count = sum((check_names(three) and check_multi(three) for three in sets_of_three))
print(count)

interconnected_sets = set()
for computer, connections in network.items():
  subgraph = collections.defaultdict(lambda: [])
  for c1, c2 in itertools.combinations(connections, 2):
    if check_pair(c1, c2):
      subgraph[c1].append(c2)
      subgraph[c2].append(c1)
  lens = [len(v) for v in subgraph.values()]
  if lens.count(lens[0]) != len(lens):
    continue
  if lens[0] != len(subgraph) - 1:
    continue
  interconnected = frozenset([computer] + list(subgraph.keys()))
  interconnected_sets.add(interconnected)

longest = max(interconnected_sets, key=lambda x: len(x))
print(",".join(sorted(longest)))
