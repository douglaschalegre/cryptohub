from pydantic import BaseModel

class UserCreateInput(BaseModel):
  name: str

class DefaultOutput(BaseModel):
  message: str

class AlternativeOutput(DefaultOutput):
  detail: str