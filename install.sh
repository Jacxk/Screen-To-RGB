#!/usr/bin/env bash

modules=(
  "PIL"
  "numpy"
  "scipy"
  "mss"
)

py -3 -m pip install -U pip

for module in "${modules[@]}"; do
  py -3 -m pip install "$module"
done
