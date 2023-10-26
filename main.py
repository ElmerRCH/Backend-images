from fastapi import FastAPI, UploadFile, Form, File, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymysql
import cv2

app = FastAPI()

#host = 'localhost'
#user = 'tu_usuario'
#password = 'tu_contraseña'
#database = 'tu_base_de_datos'
#db = pymysql.connect(host=host, user=user, password=password, database=database)

#cursor = db.cursor()

class Registrar_usuario(BaseModel):
    name: str
    olds: str
    password : str
    confi_password: str

class Login_usuario(BaseModel):
    name: str
    password: str

class validar_img(BaseModel):
    img: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(response: Response = Response()):
    return {"message": "403 Forbidden"}

@app.post("/registrar-usuario")
async def registrar_usuario(data: Registrar_usuario):
    return {"message": "403 Forbidden"}

@app.post("/iniciar-sesion")
async def login_usuario(data: Login_usuario):
    print('========================')
    if data.name == data.password:return True
    return False

@app.post("/recibir-imagen")
async def login_usuario(data: validar_img):
    print('========================')
    #print('========================')
    
    return False



