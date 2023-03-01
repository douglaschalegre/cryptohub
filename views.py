from typing import List
from asyncio import gather

from fastapi import APIRouter, HTTPException

from services import UserService, FavoriteService, AssetService
from schemas import UserCreateInput, DefaultOutput, ErrorOutput, UserFavoriteAddInput, UserListOutput, DaySummaryOutput

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

@user_router.get('/list', description='This route lists all users', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
async def list_user():
  try:
    return await UserService.list_user()
  except Exception as error:
    raise HTTPException(400, detail=str(error))

@assets_router.get('/day-summary/{user_id}', description='This route show the yesterday sumarry for a specific coin', response_model=List[DaySummaryOutput], responses={400: {'model': ErrorOutput}})
async def day_sumarry(user_id: int):
  try:
    user = await UserService.get_user_by_id(user_id=user_id)
    user_favorites = [favorite.symbol for favorite in user.favorites]

    tasks = [AssetService.day_summary(symbol=symbol) for symbol in user_favorites]
    response = await gather(*tasks)
    return response

  except Exception as error:
    raise HTTPException(400, detail=str(error))