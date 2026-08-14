from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def teste():
  return {"teste": "Deu certo!"}

@app.get("/teste2")
async def teste2():
    return {"teste": "Deu certo 2!"}

@app.get("/numAleatorio")
async def numAleatorio():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}