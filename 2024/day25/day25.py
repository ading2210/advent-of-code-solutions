import pathlib

schematics = pathlib.Path("data.txt").read_text().split("\n\n")
schematics = [s.splitlines() for s in schematics]

locks = []
keys = []

def transpose(l):
  return list(map(list, zip(*l)))

for schematic in schematics:
  if schematic[0] == "#####":
    transposed = transpose(schematic[1:])
    locks.append([col.count("#") for col in transposed])
  if schematic[-1] == "#####":
    transposed = transpose(schematic[:-1])
    keys.append([col.count("#") for col in transposed])

def check_pair(lock, key):
  for pin_height, key_height in zip(lock, key):
    if pin_height + key_height > 5:
      return False
  return True

count = 0
for lock in locks:
  for key in keys:
    if check_pair(lock, key):
      count += 1

print(count)