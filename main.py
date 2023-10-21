from fastapi import FastAPI, UploadFile, Form, File, Response


app = FastAPI()

@app.get("/")
async def root(response: Response = Response()):
    return {"message": "403 Forbidden"}

@app.post("registrar-usuario")
async def root(name: str = Form(),
               gmail: str = Form(),
               password: str = Form(),
               confi_password: str = Form()):
    
    print('name: ',name)
    return {"message": "403 Forbidden"}
