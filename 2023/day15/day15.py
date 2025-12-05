import pathlib
import re

sequence = pathlib.Path("data.txt").read_text().split(",")

def get_hash(string):
  value = 0
  for char in string:
    value += ord(char)
    value *= 17
    value %= 256
  return value

def part1():
  return sum(get_hash(item) for item in sequence)

def part2():
  boxes = [[] for i in range(0, 256)]
  item_regex = r'([a-z]+)([=-])(\d*)'

  for item in sequence:
    new_label, operation, length_str = re.findall(item_regex, item)[0]
    new_length = int(length_str) if length_str else None
    box_index = get_hash(new_label)
    box = boxes[box_index]

    if operation == "-":
      for i, (label, length) in enumerate(box):
        if new_label == label:
          box.pop(i)
          break
    
    elif operation == "=":
      for i, (label, length) in enumerate(box):
        if new_label == label:
          box[i] = (new_label, new_length)
          break
      else:
        box.append((new_label, new_length))
      
  focusing_power = 0
  for i, box in enumerate(boxes):
    for j, (label, length) in enumerate(box):
      focusing_power += (i + 1) * (j + 1) * length
  return focusing_power

print(part1(), part2())