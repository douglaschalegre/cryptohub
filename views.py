from fastapi import APIRouter, HTTPException

from services import UserService, FavoriteService
from schemas import UserCreateInput, DefaultOutput, ErrorOutput, UserFavoriteAddInput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', description='This route creates a new user', response_model=DefaultOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
  try:
    await UserService.create_user(name=user_input.name)
    return DefaultOutput(message='OK')
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@user_router.delete('/delete/{user_id}', description='This route deletes a user', response_model=DefaultOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_id: int):
  try:
    await UserService.delete_user(user_id)
    return DefaultOutput(message='User deleted')
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@user_router.post('/favorite/add', description='This route add a new favorite to a user', response_model=DefaultOutput, responses={400: {'model': ErrorOutput}})
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
  try:
    await FavoriteService.add_favorite(user_id=favorite_add.user_id, symbol=favorite_add.symbol)
    return DefaultOutput(message='OK')
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@user_router.delete('/favorite/remove/{user_id}', description='This route deletes a user', response_model=DefaultOutput, responses={400: {'model': ErrorOutput}})
async def user_favorite_remove(user_id: int, symbol: str):
  try:
    await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
    return DefaultOutput(message='Favorite removed')
  except Exception as error:
    raise HTTPException(400, detail=str(error))