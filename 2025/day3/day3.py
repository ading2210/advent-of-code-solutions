import pathlib

lines = pathlib.Path("data.txt").read_text().split("\n")

def get_output(line, num_digits):
  digits = [int(char) for char in line]
  output = ""
  for i in range(0, num_digits):
    max_digit = max(digits[:len(digits)-num_digits+1+i])
    index = digits.index(max_digit)
    output += str(digits[index])
    digits = digits[index+1:]
  return int(output)

def part1():
  return sum(get_output(line, 2) for line in lines)

def part2():
  return sum(get_output(line, 12) for line in lines)

print(part1(), part2())
