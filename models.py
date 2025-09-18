
from fastapi import FastAPI
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker
import os

DATABASE_URL = "postgresql://postgres:davi9090@db:5432/banco_dmb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()
# docker
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)  # pode ser o e-mail
    password = Column(String)

class Receita(Base):
    __tablename__ = 'receitas'

    id = Column(Integer,primary_key=True,index=True)
    nome_da_receita = Column(String)
    ingredientes = Column(String)
    modo_de_preparo = Column(String)
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:davi9090@localhost:5432/banco_dmb"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios10'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

Base.metadata.create_all(bind=engine)

'''

