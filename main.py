from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')
def hello_world():
  return 'Hello World!'

app.include_router(prefix='/v1', router=router)