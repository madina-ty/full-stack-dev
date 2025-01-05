#!/bin/bash

echo "Дата и время: $(date)"
echo "Пользователь: $(whoami)"

file_count=$(ls -1 | wc -l)
echo "Количество файлов в текущей директории: $file_count"