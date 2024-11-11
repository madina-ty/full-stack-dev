import requests
import json

def get_posts():
  """Функция для получения списка постов"""
  try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()  # Проверяем статус ответа
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Ошибка при получении постов: {e}")
    return None

def get_post_by_id(post_id):
  """Функция для получения поста по ID"""
  try:
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Ошибка при получении поста: {e}")
    return None

def create_post(data):
  """Функция для создания нового поста"""
  try:
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Ошибка при создании поста: {e}")
    return None

if __name__ == "__main__":
  # Получаем список постов
  posts = get_posts()
  if posts:
    # Выбираем первый пост для примера
    first_post_id = posts[0]['id']
    post_details = get_post_by_id(first_post_id)
    if post_details:
      # Сохраняем данные первого поста в файл
      with open('dev-core-103/lesson4/posts_data.json', 'w') as f:
        json.dump(post_details, f, indent=2)

      # Создаем новый пост
      new_post_data = {'title': 'Новый пост', 'body': 'Это тело нового поста', 'userId': 1}
      created_post = create_post(new_post_data)
      print(created_post)