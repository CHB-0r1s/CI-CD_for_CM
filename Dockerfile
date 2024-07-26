# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем необходимые пакеты для работы с git
RUN apt-get update && apt-get install -y git && apt-get clean

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем скрипт зависимостей в контейнер
COPY deps.sh .

# Устанавливаем зависимости
RUN sh deps.sh

# Клонируем приватный репозиторий
RUN git clone https://github.com/CHB-0r1s/lab_1_tests

# Перемещаем файлы из клонированного репозитория в рабочую директорию
RUN mv lab_1_tests/* . && rm -rf lab_1_tests

# Устанавливаем зависимости для тестов
RUN python3 -m pip install --no-cache-dir -r test_lab1_requirements.txt

# Копируем все остальные необходимые файлы в контейнер (если есть)
COPY . .

# Запускаем pytest
CMD ["python3", "-m", "pytest", "test_input_format.py"]