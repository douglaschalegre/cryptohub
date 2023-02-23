from pydantic import BaseModel

class UserCreateInput(BaseModel):
  name: str

class DefaultOutput(BaseModel):
  message: str

class ErrorOutput(DefaultOutput):
  detail: str