#!/bin/bash

base_path="$(dirname "$(realpath "$0")")"

puzzle_dirs=$(ls -1 "$base_path/2024/"| sort -n -k 1.4)

for puzzle_dir in $puzzle_dirs; do
  cd "$base_path/2024/$puzzle_dir"
  echo running day*.py
  pypy3 day*.py
done
