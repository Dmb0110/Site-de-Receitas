from fastapi import FastAPI
from models import Base,engine
from crud import router as crud_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from autenticacao10.jwt_auth2 import router as jwt_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique o domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(crud_router)
app.include_router(jwt_router)

app.mount('/',StaticFiles(directory='front3',html=True), name='static')



# COMO EVITAR BAIXAR OS ARQUIVOS DO LANGUAGE TOOL





# docker compose up --build
# docker logs projeto10sitedereceita-web-1

#  docker compose logs web

# docker-compose up = para rodar a api

# nao apaga dados
# docker compose up --build
# docker compose down = para tudo

# para tudo e apaga os dados
# docker compose up --build
# docker compose down --volumes

# cad usuaio2 = login
# cad usuario3 = registrar
# cadastrar = cadastrar receita
# index4 = pagina principal
# receita = mostrar receita




# docker compose up --build

# docker compose run web ls




'''
###############################
FROM python:3.11-slim

WORKDIR /app

# Instala Java (necessário para language_tool_python)
RUN apt-get update && apt-get install -y default-jre && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY front3/ front3/
COPY main.py .
COPY models.py .
COPY schemas.py .
COPY crud.py .
COPY autenticacao10/ autenticacao10/

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]








services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: davi9090
      POSTGRES_DB: banco_dmb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:davi9090@db:5432/banco_dmb
      LANGUAGETOOL_URL: http://languagetool:8010/v2/check  # se sua API usar isso
    depends_on:
      - db
      - languagetool
  languagetool:
    image: silviof/docker-languagetool
    container_name: languagetool
    ports:
      - "8081:8010"
    restart: unless-stopped

volumes:
  pgdata:










services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: davi9090
      POSTGRES_DB: banco_dmb
    ports:
      - "5432:5432"

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:davi9090@db:5432/banco_dmb
    depends_on:
      - db
      - languagetool  # garante que o LanguageTool esteja pronto antes da API

  languagetool:
    image: silviof/docker-languagetool
    container_name: languagetool
    ports:
      - "8081:8010"  # corrige o mapeamento para a porta interna correta
    restart: unless-stopped









services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: davi9090
      POSTGRES_DB: banco_dmb
    ports:
      - "5432:5432"

  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:davi9090@db:5432/banco_dmb
    depends_on:
      - db





docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://postgres:davi9090@db:5432/banco_dmb \
  site-de-receitas


# Copia o restante do projeto
COPY front3/ front3/
COPY main.py .
COPY models.py .
COPY schemas.py .
COPY crud.py .
COPY autenticacao10/ autenticacao10/





###############################################3
services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: davi9090
      POSTGRES_DB: banco_dmb
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  web:
    build: .
    depends_on:
      - db
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:davi9090@db:5432/banco_dmb

volumes:
  pgdata:







<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Cadastrar Receita</title>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Quicksand', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #fffaf4;
      color: #333;
    }

    header {
      background-color: #ff7043;
      color: white;
      padding: 15px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .voltar {
      background: none;
      border: none;
      color: white;
      font-size: 18px;
      cursor: pointer;
    }

    .form-container {
      max-width: 800px;
      margin: 40px auto;
      background-color: #fff3e0;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    input, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 12px;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 14px;
    }

    button {
      background-color: #ff7043;
      color: white;
      border: none;
      padding: 10px 16px;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s;
    }

    button:hover {
      background-color: #e64a19;
    }
  </style>
</head>
<body>

  <header>
    <button class="voltar" onclick="window.location.href='index4.html'">← Voltar</button>
    <h1>Nova Receita</h1>
    <div></div>
  </header>

  <div class="form-container">
    <h2>Cadastrar Receita</h2>
    <input type="text" id="nome" placeholder="Nome da receita">
    <textarea id="ingredientes" placeholder="Ingredientes (um por linha)"></textarea>
    <textarea id="modo" placeholder="Modo de preparo"></textarea>
    <button onclick="handleCriar()">Salvar Receita</button>
  </div>

  <script>
    const API_BASE = "http://localhost:8000";

    async function criarReceita(dados) {
      const token = localStorage.getItem("access_token");

      if (!token) {
        alert("Você precisa estar logado para cadastrar uma receita.");
        return;
      }

      try {
        const res = await fetch(`${API_BASE}/enviar`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
          },
          body: JSON.stringify(dados)
        });

        const result = await res.json();

        if (!res.ok) {
          alert(result.detail || "Erro ao salvar receita.");
          return;
        }

        alert("Receita cadastrada com sucesso!");
        window.location.href = "index4.html";
      } catch (error) {
        alert("Erro de conexão com o servidor.");
      }
    }

    async function handleCriar() {
      const nome = document.getElementById("nome").value;
      const ingredientes = document.getElementById("ingredientes").value;
      const modo = document.getElementById("modo").value;

      if (!nome || !ingredientes || !modo) {
        alert("Preencha todos os campos!");
        return;
      }

      const novaReceita = {
        nome_da_receita: nome,
        ingredientes,
        modo_de_preparo: modo
      };

      await criarReceita(novaReceita);
    }
  </script>

</body>
</html>







<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Registro</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }

    .top-bar {
      background-color: #fff;
      padding: 10px;
      display: flex;
      align-items: center;
    }

    .back-button {
      background-color: #007BFF;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 4px;
      cursor: pointer;
      margin-left: 10px;
    }

    .container {
      max-width: 400px;
      margin: 50px auto;
      background-color: white;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    input {
      width: 100%;
      padding: 10px;
      margin: 8px 0;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      width: 100%;
      background-color: #28a745;
      color: white;
      padding: 10px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      background-color: #218838;
    }

    .message {
      margin-top: 15px;
      text-align: center;
      color: green;
    }

    .error {
      color: red;
    }
  </style>
</head>
<body>

  <div class="top-bar">
    <button class="back-button" onclick="window.location.href='index4.html'">← Voltar</button>
  </div>

  <div class="container">
    <h2>Registro</h2>
    <form id="registerForm">
      <input type="text" id="username" placeholder="Nome de usuário" required>
      <input type="password" id="password" placeholder="Senha" required>
      <button type="submit">Registrar</button>
    </form>
    <div class="message" id="message"></div>
  </div>

  <script>
    const form = document.getElementById("registerForm");
    const message = document.getElementById("message");

    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
      };

      try {
        const response = await fetch("/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
          message.textContent = result.msg;
          message.classList.remove("error");
        } else {
          message.textContent = result.detail || "Erro ao registrar";
          message.classList.add("error");
        }
      } catch (err) {
        message.textContent = "Erro de conexão com o servidor";
        message.classList.add("error");
      }
    });
  </script>

</body>
</html>




<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Login - Receitas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f9f9f9;
      margin: 0;
      padding: 0;
    }

    .top-bar {
      background-color: #ffffff;
      padding: 10px 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      display: flex;
      align-items: center;
    }

    .back-button {
      text-decoration: none;
      color: #007bff;
      font-weight: bold;
      font-size: 16px;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 100px;
    }

    form {
      background: white;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    input {
      display: block;
      margin-bottom: 15px;
      padding: 10px;
      width: 250px;
    }

    button {
      padding: 10px 20px;
      background: #28a745;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    #response {
      margin-top: 20px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <div class="top-bar">
    <a href="index4.html" class="back-button">← Voltar</a>
  </div>

  <div class="container">
    <form id="loginForm">
      <h2>Login</h2>
      <input type="text" id="username" placeholder="Usuário" required />
      <input type="password" id="password" placeholder="Senha" required />
      <button type="submit">Entrar</button>
    </form>

    <div id="response"></div>
  </div>

  <script>
    const form = document.getElementById('loginForm');
    const responseDiv = document.getElementById('response');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;

      try {
        const res = await fetch('http://localhost:8000/login10', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username, password })
        });

        const data = await res.json();

        if (res.ok) {
          responseDiv.textContent = 'Login bem-sucedido!';
          responseDiv.style.color = 'green';
          localStorage.setItem('access_token', data.access_token);
        } else {
          responseDiv.textContent = data.detail || 'Erro ao fazer login.';
          responseDiv.style.color = 'red';
        }
      } catch (error) {
        responseDiv.textContent = 'Erro de conexão com o servidor.';
        responseDiv.style.color = 'red';
      }
    });
  </script>

</body>
</html>









<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Cadastrar Receita</title>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Quicksand', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #fffaf4;
      color: #333;
    }

    header {
      background-color: #ff7043;
      color: white;
      padding: 15px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .voltar {
      background: none;
      border: none;
      color: white;
      font-size: 18px;
      cursor: pointer;
    }

    .form-container {
      max-width: 800px;
      margin: 40px auto;
      background-color: #fff3e0;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    h2 {
      text-align: center;
      margin-bottom: 20px;
    }

    input, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 12px;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 14px;
    }

    button {
      background-color: #ff7043;
      color: white;
      border: none;
      padding: 10px 16px;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.3s;
    }

    button:hover {
      background-color: #e64a19;
    }
  </style>
</head>
<body>

  <header>
    <button class="voltar" onclick="window.location.href='index4.html'">← Voltar</button>
    <h1>Nova Receita</h1>
    <div></div>
  </header>

  <div class="form-container">
    <h2>Cadastrar Receita</h2>
    <input type="text" id="nome" placeholder="Nome da receita">
    <textarea id="ingredientes" placeholder="Ingredientes (um por linha)"></textarea>
    <textarea id="modo" placeholder="Modo de preparo"></textarea>
    <button onclick="handleCriar()">Salvar Receita</button>
  </div>

  <script>
    const API_BASE = "http://localhost:8000";

    async function criarReceita(dados) {
      const res = await fetch(`${API_BASE}/enviar`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
      });
      if (!res.ok) {
        alert("Erro ao salvar receita");
        return;
      }
      alert("Receita cadastrada com sucesso!");
      window.location.href = "index4.html";
    }

    async function handleCriar() {
      const nome = document.getElementById("nome").value;
      const ingredientes = document.getElementById("ingredientes").value;
      const modo = document.getElementById("modo").value;

      if (!nome || !ingredientes || !modo) {
        alert("Preencha todos os campos!");
        return;
      }

      const novaReceita = {
        nome_da_receita: nome,
        ingredientes,
        modo_de_preparo: modo
      };

      await criarReceita(novaReceita);
    }
  </script>

</body>
</html>











linha 190
<a href="index.html">← Voltar</a>
<a href="/">← Voltar</a>
<a href="javascript:history.back()">← Voltar</a>
<a href="/" style="text-decoration: none; color: #333; font-weight: bold;">← Voltar</a>
const ingredientes = receita.ingredientes.split("\n").filter(i => i.trim() !== "");

<button onclick="mostrarFormulario()">Cadastrar Receita</button>

menu.style.display = menu.style.display === "block" ? "none" : "block";



<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Detalhes da Receita</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #fffaf4;
      padding: 30px;
      max-width: 800px;
      margin: auto;
    }

    h2 {
      color: #ff7043;
      margin-bottom: 20px;
    }

    ul {
      padding-left: 20px;
      margin-bottom: 30px;
    }

    li {
      margin-bottom: 8px;
    }

    .modo-preparo {
      background-color: #fff3e0;
      padding: 15px;
      border-radius: 6px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.1);
    }

    a {
      display: inline-block;
      margin-bottom: 20px;
      color: #ff7043;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>

  <a href="javascript:history.back()">← Voltar</a>
  <h2 id="titulo-receita">Receita</h2>
  <h3>Ingredientes</h3>
  <ul id="lista-ingredientes"></ul>
  <h3>Modo de Preparo</h3>
  <div class="modo-preparo" id="modo-preparo"></div>

  <script>
    const API_BASE = "http://localhost:8000";

    function getIdFromURL() {
      const params = new URLSearchParams(window.location.search);
      return params.get("id");
    }

    async function buscarReceitaPorId(id) {
      const res = await fetch(`${API_BASE}/especifico/${id}`);
      if (!res.ok) throw new Error("Erro ao buscar receita");
      return await res.json();
    }

    async function carregarDetalhes() {
      const id = getIdFromURL();
      const receita = await buscarReceitaPorId(id);

      document.getElementById("titulo-receita").textContent = receita.nome_da_receita;

      const ingredientes = receita.ingredientes.split(",").map(i => i.trim()).filter(i => i !== "");
      const lista = document.getElementById("lista-ingredientes");
      ingredientes.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        lista.appendChild(li);
      });

      document.getElementById("modo-preparo").textContent = receita.modo_de_preparo;
    }

    carregarDetalhes();
  </script>

</body>
</html>




'''
'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Login com Google</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://accounts.google.com/gsi/client" async defer></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fffaf4;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }

    h2 {
      margin-bottom: 20px;
    }

    #g_id_onload, .g_id_signin {
      margin-top: 10px;
    }
  </style>
</head>
<body>

  <h2>👤 Faça login com sua conta Google</h2>

  <!-- Configuração do botão Google -->
  <div id="g_id_onload"
       data-client_id="SEU_CLIENT_ID_AQUI"
       data-context="signin"
       data-ux_mode="popup"
       data-callback="handleCredentialResponse"
       data-auto_prompt="false">
  </div>

  <div class="g_id_signin"
       data-type="standard"
       data-size="large"
       data-theme="outline"
       data-text="sign_in_with"
       data-shape="pill"
       data-logo_alignment="left">
  </div>

  <script>
    function handleCredentialResponse(response) {
      // Aqui você pode enviar o token para seu backend
      console.log("Token JWT recebido:", response.credential);

      // Exemplo: redirecionar após login
      alert("Login realizado com sucesso!");
      window.location.href = "pagina-principal.html"; // ou qualquer outra página
    }
  </script>

</body>
</html>




    .btn-voltar {
      margin-top: 30px;
      padding: 10px 16px;
      background-color: #ff7043;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 16px;
    }






'''


