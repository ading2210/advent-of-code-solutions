import pathlib
import json
import functools

lines = pathlib.Path("data.txt").read_text().split("\n")

numpad_layout = (
  ("7", "8", "9"),
  ("4", "5", "6"),
  ("1", "2", "3"),
  (" ", "0", "A"),
)

dirpad_layout = (
  (" ", "^", "A"),
  ("<", "v", ">")
)

dir_offsets = {
  "<": (-1, 0),
  ">": (1, 0),
  "^": (0, -1),
  "v": (0, 1)
}

@functools.cache
def find_key(layout, target_key):
  for y, row in enumerate(layout):
    for x, key in enumerate(row):
      if key == target_key:
        return x, y

@functools.cache
def get_presses(keypad, target_key, curr_pos, iterations=None):
  curr_x, curr_y = curr_pos
  hole_x, hole_y = find_key(keypad, " ")
  key_x, key_y = find_key(keypad, target_key)  
  diff_x, diff_y = abs(curr_x-key_x), abs(curr_y-key_y)

  char_x = ">" if curr_x < key_x else "<"
  char_y = "v" if curr_y < key_y else "^"
  
  paths = set()
  paths.add(char_x*diff_x + char_y*diff_y)
  paths.add(char_y*diff_y + char_x*diff_x)
  
  for path in paths.copy():
    new_x, new_y = curr_pos
    for char in path:
      new_x += dir_offsets[char][0]
      new_y += dir_offsets[char][1]
      if keypad[new_y][new_x] == " ":
        paths.remove(path)
        break
  
  return [path + "A" for path in paths]

@functools.cache
def get_count(keys, iterations, first=False):
  if iterations == 0:
    return len(keys)
  
  keypad = numpad_layout if first else dirpad_layout
  total = 0
  prev_key = "A"
  for key in keys:
    curr_pos = find_key(keypad, prev_key)
    paths = get_presses(keypad, key, curr_pos, iterations)
    total += min(get_count(path, iterations-1) for path in paths)
    prev_key = key

  return total

complexity_p1 = complexity_p2 = 0
for num_keys in lines:
  num = int(num_keys.replace("A", ""))
  length = get_count(num_keys, 3, True)
  complexity_p1 += num * get_count(num_keys, 3, True)
  complexity_p2 += num * get_count(num_keys, 26, True)

print(complexity_p1, complexity_p2)