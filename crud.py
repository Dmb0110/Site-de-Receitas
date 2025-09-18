from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from models import SessionLocal,Receita,Usuario
from schemas import ReceitaOut,CriarReceita,Atualizar,LoginRequest,RegisterRequest
from typing import List
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
#from autenticacao10.jwt_auth2 import authenticate_user,create_token,pwd_context

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
@router.get("/login/google")
def login_google():
    # Aqui você faria a autenticação com Google
    # Após sucesso, gere o JWT e redirecione com ele
    token = "seu_jwt_gerado_aqui"
    return RedirectResponse(url=f"http://localhost:8000/login.html?token={token}")

@router.post("/login")
def login(usuario: str, senha: str, response: Response):
    if autenticar(usuario, senha):
        token = criar_jwt({"sub": usuario})
        response.set_cookie(key="access_token", value=token, httponly=True)
        return {"mensagem": "Login realizado"}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

@router.post("/login10")
async def login(request: LoginRequest,db: Session = Depends(get_db)):
    username = request.username
    password = request.password
    user = authenticate_user(db,username,password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token({"sub": username})
    return {"access_token": token}

@router.post("/register", status_code=201)
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(Usuario).filter(Usuario.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    hashed_password = pwd_context.hash(request.password)
    novo_usuario = Usuario(
        username=request.username,
        password=hashed_password,
        email=request.email,
        full_name=request.full_name
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"msg": "Usuário registrado com sucesso"}


@router.post('/enviar',response_model=ReceitaOut)
def enviar(criar: CriarReceita,db: Session = Depends(get_db)):
    nova_receita = Receita(**criar.dict())
    db.add(nova_receita)
    db.commit()
    db.refresh(nova_receita)
    return nova_receita
'''
@router.get('/receber',response_model=List[ReceitaOut])
def receber(db: Session = Depends(get_db)):
    return db.query(Receita).all()

@router.put('/trocar/{id}',response_model=ReceitaOut)
def trocar(id: int,at: Atualizar,db: Session = Depends(get_db)):
    receita = db.query(Receita).filter(Receita.id == id).first()
    if not receita:
        raise HTTPException(status_code=404,detail='receita nao encontrada')
    
    if at.nome_da_receita is not None:
        receita.nome_da_receita = at.nome_da_receita
    if at.ingredientes is not None:
        receita.ingredientes = at.ingredientes
    if at.modo_de_preparo is not None:
        receita.modo_de_preparo = at.modo_de_preparo

    db.commit()
    db.refresh(receita)
    return receita

@router.delete('/delete/{id}')
def deletar(id: int,db: Session = Depends(get_db)):
    receita = db.query(Receita).filter(Receita.id == id).first()
    if not receita:
        raise HTTPException(status_code=404,detail='receita nao encontrada')
    
    db.delete(receita)
    db.commit()
    return {'mensagem':'receita apagada com sucesso'}

@router.get('/especifico/{id}',response_model=ReceitaOut)
def espefico(id: int,db: Session = Depends(get_db)):
    receita = db.query(Receita).filter(Receita.id == id).first()
    if not receita:
        raise HTTPException(status_code=404,detail='receita nao encontrada')
    return receita
