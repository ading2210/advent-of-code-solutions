import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

dial_pos = 50
password_1 = 0
password_2 = 0

for line in lines:
  direction, clicks = line[0], int(line[1:])
  step = 1 if direction == "R" else -1
  
  for i in range(0, clicks):
    dial_pos += step
    if dial_pos % 100 == 0:
      password_2 += 1
  if dial_pos % 100 == 0:
    password_1 += 1

print(password_1, password_2)