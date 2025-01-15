#!/bin/bash

# Poetryのインストール
curl -sSL https://install.python-poetry.org | python3 -
# pip3 install poetry


# requirements.txt の生成
PATH=$PATH:$HOME/.local/bin poetry install
echo "----export requirements.txt----"

PATH=$PATH:$HOME/.local/bin poetry -h

PATH=$PATH:$HOME/.local/bin poetry export -f requirements.txt --output requirements.txt --without-hashes
