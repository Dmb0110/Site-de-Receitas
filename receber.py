import requests

url = 'http://127.0.0.1:8000/receber'

resposta = requests.get(url)

print(resposta.status_code)
print(resposta.text)
