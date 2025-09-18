#!/bin/bash
set -euo pipefail
python3 -m pip install --upgrade pip pytest >/dev/null
pytest -q
