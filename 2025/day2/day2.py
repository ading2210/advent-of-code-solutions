import pathlib

data = pathlib.Path("data.txt").read_text()
ranges_data = [r.split("-") for r in data.replace("\n", "").split(",")]
ranges = [(int(r[0]), int(r[1])) for r in ranges_data]

def test_id(id):
  for i in range(1, len(id) // 2 + 1):
    if len(id) % i != 0:
      continue
    repeated = id[:i] * (len(id) // i)
    if repeated == id:
      return True
  return False

def part_1():
  total = 0
  for first, last in ranges:
    for i in range(first, last + 1):
      id = str(i)
      h1, h2 = id[:len(id)//2], id[len(id)//2:]
      if h1 == h2:
        total += i
  return total

def part_2():
  total = 0
  for first, last in ranges:
    for i in range(first, last + 1):
      id = str(i)
      if test_id(id):
        total += i
  return total

print(part_1(), part_2())