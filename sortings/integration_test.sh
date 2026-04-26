#!/bin/bash

status=true

# ---------------------------------------------------


result=$(python3 ~/Рабочий\ стол/sortings/sortings/demo.py 2>&1)


if [[ $result != *"True"* ]]; then
    status=false
fi

# ---------------------------------------------------


pytest_result=$(python3 -m pytest ~/Рабочий\ стол/sortings/sortings/sorting_test.py -v 2>&1)

if [[ $pytest_result != *"passed"* ]]; then
    status=false

fi

# ---------------------------------------------------

echo "Integration test status: $status"