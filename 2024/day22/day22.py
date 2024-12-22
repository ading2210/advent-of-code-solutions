import pathlib
import itertools
import collections

lines = pathlib.Path("data.txt").read_text().split("\n")
secrets = [int(s) for s in lines]

def calculate_secret(secret):
  secret ^= secret * 64
  secret %= 16777216
  secret ^= secret // 32
  secret %= 16777216
  secret ^= secret * 2048
  secret %= 16777216
  return secret

secret_total = 0
sequence_prices = collections.defaultdict(lambda: 0)

for secret in secrets:
  changes = []
  prices = []
  for i in range(2000):
    new_secret = calculate_secret(secret)
    changes.append((new_secret % 10) - (secret % 10))
    prices.append(new_secret % 10)
    secret = new_secret
  
  sequences = list(zip(changes, changes[1:], changes[2:], changes[3:]))
  prices_map = dict(zip(reversed(sequences), reversed(prices)))

  secret_total += secret
  for sequence, price in prices_map.items():
    sequence_prices[sequence] += price

print(secret_total)
print(max(sequence_prices.values()))
