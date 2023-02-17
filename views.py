from fastapi import APIRouter

from services import UserService
from schemas import UserCreateInput, DefaultOutput, AlternativeOutput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model=DefaultOutput, responses={418: {'model': AlternativeOutput}})
async def user_create(user_input: UserCreateInput):
  try:
    await UserService.create_user(name=user_input.name)
    return DefaultOutput(message='OK')
  except:
    pass