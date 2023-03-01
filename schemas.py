from pydantic import BaseModel
from typing import List

class UserCreateInput(BaseModel):
  name: str

class UserFavoriteAddInput(BaseModel):
  user_id: int
  symbol: str

class DefaultOutput(BaseModel):
  message: str

class ErrorOutput(DefaultOutput):
  detail: str

class Favorite(BaseModel):
  id: int
  symbol: str
  user_id: int

  class Config:
    orm_mode = True

class UserListOutput(BaseModel):
  id: int
  name: str
  favorites: List[Favorite]

  class Config:
    orm_mode = True

class DaySummaryOutput(BaseModel):
  symbol: str
  opening: float
  closing: float
  lowest: float
  highest: float
  volume: float
  quantity: float
  amount: float
  avg_price: float