import pathlib
import re

data = pathlib.Path("data.txt").read_text()
tree_matches = re.findall(r'(\d+)x(\d+): (.+)$', data, flags=re.M)
trees = [(int(a), int(b), list(map(int, c.split(" ")))) for a, b, c in tree_matches]

total = sum((w // 3) * (h // 3) >= sum(counts) for w, h, counts in trees)
print(total)
