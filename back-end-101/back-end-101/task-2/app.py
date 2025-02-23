import requests
import numpy as np
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значений переменных окружения
api_key = os.environ.get('API_KEY')
debug_mode = os.environ.get('DEBUG_MODE')

# Вывод значений переменных на экран
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")

# Пример использования переменных в логике приложения
if debug_mode == 'True':
    print("Debug mode is enabled.")
else:
    print("Debug mode is disabled.")

# Пример использования библиотеки requests
response = requests.get('https://api.github.com')
print('Status Code:', response.status_code)

# Пример использования библиотеки numpy
array = np.array([1, 2, 3, 4, 5])
print('Numpy Array:', array)
print('Mean of Array:', np.mean(array))