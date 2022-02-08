#!/usr/bin/env bash

echo "Checking python version..."
IFS=' '
read -ra ADDR <<<"$(python3 --version)"

version=$(echo "${ADDR[1]}" | cut -c1)

if [ "$version" -eq "3" ]; then
  echo "Suported version of Python found..."
else
  echo "Unsuported version of Python. Please install Python 3."
  exit 1
fi

echo "Upgrading pip..."
python3 -m pip3 install --upgrade pip3

echo "Installing requirements..."
pip3 install -r requirements.txt
