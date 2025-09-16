# tmp_test_request.py
import requests

url = "http://127.0.0.1:8000/api/v1/questions/"
data = {"text": "????"}

response = requests.post(url, json=data)
print(response.json())  # Печать ответа от сервера
