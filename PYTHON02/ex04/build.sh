#!/bin/sh

python3 -m pip install --upgrade pip
python3 -m pip install setuptools wheel twine
python3 -m pip install --upgrade setuptools wheel twine
python3 -m pip install --upgrade build
python3 -m build
pip install ./dist/my_minipack-1.0.0.tar.gz
# pip install ./dist/my_minipack-1.0.0-py3-none-any.whl