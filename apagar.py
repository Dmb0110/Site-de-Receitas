import requests

url = 'http://127.0.0.1:8000/delete/4'

resposta = requests.delete(url)

print(resposta.status_code)
print(resposta.json())
