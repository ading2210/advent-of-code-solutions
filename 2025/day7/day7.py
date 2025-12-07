import pathlib
import collections

board = pathlib.Path("data.txt").read_text().split("\n")
beams = collections.defaultdict(int)
beams[board[0].index("S")] = 1
splits = 0

for y in range(len(board)-1):
  for x, count in list(beams.items()):
    tile = board[y + 1][x]

    if tile == "^":
      beams[x-1] += count
      beams[x+1] += count
      del beams[x]
      splits += 1

print(splits) 
print(sum(beams.values()))