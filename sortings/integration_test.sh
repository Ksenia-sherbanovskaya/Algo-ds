#!/bin/bash

status=true

# ---------------------------------------------------

# Запуск демо-скрипта
result=$(python3 ~/Рабочий\ стол/sortings/sortings/demo.py 2>&1)

# Проверка, что сортировка работает
if [[ $result == *"True"* ]]; then
    status=true
else
    status=false
fi

# ---------------------------------------------------

# Запуск unit-тестов
pytest_result=$(python3 -m pytest ~/Рабочий\ стол/sortings/sortings/sorting_test.py -v 2>&1)

if [[ $pytest_result == *"passed"* ]]; then
    status=true
else
    status=false
fi

# ---------------------------------------------------

echo "Integration test status: $status"