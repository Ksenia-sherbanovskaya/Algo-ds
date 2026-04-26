#!/bin/bash

script="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
status=true

# ---------------------------------------------------
result=$(python3 "$script/demo.py" 2>&1)

if [[ $result != *"True"* ]]; then
    status=false
fi

# ---------------------------------------------------
pytest_result=$(python3 -m pytest "$script/sorting_test.py" -v 2>&1)

if [[ $pytest_result != *"passed"* ]]; then
    status=false
fi

# ---------------------------------------------------
echo "Integration test status: $status"