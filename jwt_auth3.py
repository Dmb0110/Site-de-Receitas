from fastapi import APIRouter, Request, HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.context import CryptContext
from pydantic import BaseModel
from models import Usuario,Receita
from crud import get_db
from schemas import LoginRequest,ReceitaOut,CriarReceita
from typing import List

router = APIRouter()

# Configurações do JWT
SECRET_KEY = "sua_chave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Funções auxiliares
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def verificar_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente ou mal formatado")

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@router.post("/login10")
async def login(request: LoginRequest,db: Session = Depends(get_db)):
    username = request.username
    password = request.password

    user = authenticate_user(db,username,password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token({"sub": username})
    return {"access_token": token}
