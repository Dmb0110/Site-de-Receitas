'''import requests

url = 'http://127.0.0.1:8000/enviar'

info = {
    'nome_da_receita':'misto quente',
    'ingredientes':'pao,maionese,queijo,presunto',
    'modo_de_preparo':'passe a maiose no pao,coloque queijo e presunto e leve na chapa'
}

resposta = requests.post(url,json=info)

print(resposta.status_code)
print(resposta.text)
'''
import requests

url = 'http://127.0.0.1:8000/enviar'

info = {
    'nome_da_receita': 'misto quente',
    'ingredientes': 'pao,maionese,queijo,presunto',
    'modo_de_preparo': 'passe a maionese no pao, coloque queijo e presunto e leve na chapa'
}

try:
    resposta = requests.post(url, json=info)
    print(f"Status: {resposta.status_code}")

    # Tenta decodificar JSON apenas se houver conteúdo
    if resposta.headers.get('Content-Type') == 'application/json':
        print("Resposta JSON:", resposta.json())
    else:
        print("Resposta não está em JSON:")
        print(resposta.text)

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
'''

import language_tool_python

tool = language_tool_python.LanguageTool('pt-BR')
texto = "eu gosto de pao na chapa"
corrigido = tool.correct(texto)
print(corrigido)
'''

