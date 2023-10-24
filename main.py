from fastapi import FastAPI, UploadFile, Form, File, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class DatosUsuario(BaseModel):
    name: str
    olds: str
    password : str
    confi_password: str
    
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
async def registrar_usuario(data: DatosUsuario):
    if data.password == data.confi_password:
        print('contraseñas igual.....')
    
    return {"message": "403 Forbidden"}
