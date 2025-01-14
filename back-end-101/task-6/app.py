import requests
import numpy as np

# Пример использования requests
response = requests.get('https://api.github.com')
print('Status Code:', response.status_code)

# Пример использования numpy
array = np.array([1, 2, 3, 4, 5])
print('Numpy Array:', array)
print('Mean of Array:', np.mean(array))
