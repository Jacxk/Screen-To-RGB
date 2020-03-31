#!/usr/bin/env bash

echo "Checking python version..."
IFS=' '
read -ra ADDR <<<"$(python --version)"

version=$(echo "${ADDR[1]}" | cut -c1)

if [ "$version" -eq "3" ]; then
  echo "Suported version of Python found..."
else
  echo "Unsuported version of Python. Please install Python 3."
  exit 1
fi

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt
