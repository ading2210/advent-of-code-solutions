import pathlib
import functools
import re

patterns_str, designs_str = pathlib.Path("data.txt").read_text().split("\n\n")
patterns = patterns_str.split(", ")
designs = designs_str.split("\n")

regex_part = "|".join(patterns)
patterns_regex = fr"^({regex_part})+$"

@functools.cache
def possible_designs(design):
  possible = 0
  if design == "":
    return 1

  for pattern in patterns:
    if not pattern in design:
      continue
    if design.index(pattern) != 0:
      continue
    new_design = design[len(pattern):]
    possible += possible_designs(new_design)

  return possible

valid = sum((bool(re.findall(patterns_regex, design)) for design in designs))
possible = sum((possible_designs(design) for design in designs))

print(valid, possible)