from fastapi import FastAPI

app = FastAPI()

@app.router.get('/')
def hello_world():
  return 'Hello World!'