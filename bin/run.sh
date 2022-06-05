#!/usr/bin/env bash

# Cause the script to exit if a single command fails
set -eo pipefail -v

PYTHONPATH=. python ./src/scripts/run.py
