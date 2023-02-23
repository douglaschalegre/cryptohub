from fastapi import APIRouter

from services import UserService
from schemas import UserCreateInput, DefaultOutput, ErrorOutput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', description='This route creates a new user', response_model=DefaultOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
  try:
    await UserService.create_user(name=user_input.name)
    return DefaultOutput(message='OK')
  except:
    pass

