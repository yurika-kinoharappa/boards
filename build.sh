#!/bin/bash

# Poetryのインストール
curl -sSL https://install.python-poetry.org | python3 -
# pip3 install poetry

# PATHを設定
export PATH=$PATH:$HOME/.local/bin

# requirements.txt の生成
poetry install
echo "----export requirements.txt----"
poetry export -f requirements.txt --output requirements.txt --without-hashes
