import pathlib
import copy

lines = pathlib.Path("data.txt").read_text().split("\n")
data = [list(line) for line in lines]

def tilt_north(board):
  for x in range(0, len(board[0])):
    for i in range(0, len(board) - 1):
      modified = False
      for y in range(0, len(board) - 1):
        if board[y][x] == "." and board[y+1][x] == "O":
          board[y][x] = "O"
          board[y+1][x] = "."
          modified = True
      if not modified:
        break

def tilt_south(board):
  tilt_north(board[::-1])

def tilt_west(board):
  for y in range(0, len(board)):
    for i in range(0, len(board[0]) - 1):
      modified = False
      for x in range(0, len(board[0]) - 1):
        if board[y][x] == "." and board[y][x+1] == "O":
          board[y][x] = "O"
          board[y][x+1] = "."
          modified = True
      if not modified:
        break

def tilt_east(board):
  for row in board:
    row.reverse()
  tilt_west(board)
  for row in board:
    row.reverse()

def run_cycle(board):
  tilt_north(board)
  tilt_west(board)
  tilt_south(board)
  tilt_east(board)

def hash_board(board):
  board_tuple = tuple(tuple(row) for row in board)
  return hash(board_tuple)

def get_load(board):
  total_load = 0
  for y in range(0, len(board)):
    for x in range(0, len(board[0])):
      if board[y][x] == "O":
        total_load += len(board) - y
  return total_load

def part1():
  board = copy.deepcopy(data)
  tilt_north(board)
  return get_load(board)

def part2():
  board = copy.deepcopy(data)
  results = []
  i = 0
  while True:
    run_cycle(board)
    board_load = get_load(board)
    board_hash = hash_board(board)
    if (board_load, board_hash) in results:
      break
    results.append((board_load, board_hash))
    i += 1
  
  start_index = results.index((board_load, board_hash))
  repeating_results = results[start_index:]
  final_index = (1_000_000_000 - 1 - start_index) % len(repeating_results)
  final_load = repeating_results[final_index][0]
  return final_load
  
print(part1(), part2())