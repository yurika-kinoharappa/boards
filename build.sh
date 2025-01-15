#!/bin/bash

# Poetryのインストール
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.4 python3 -
# pip3 install poetry


# requirements.txt の生成
poetry install
echo "----export requirements.txt----"

poetry --version

poetry self add poetry-plugin-export

poetry export -f requirements.txt --output requirements.txt --without-hashes
