# tmp_test_request.py
import requests

url = "http://127.0.0.1:8000/questions/"
data = {"text": "Точно?"}

response = requests.post(url, json=data)
print(response.json())  # Печать ответа от сервера
