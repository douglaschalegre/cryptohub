from pydantic import BaseModel

class UserCreateInput(BaseModel):
  name: str

class UserFavoriteAddInput(BaseModel):
  user_id: int
  symbol: str

class DefaultOutput(BaseModel):
  message: str

class ErrorOutput(DefaultOutput):
  detail: str