from pydantic import BaseModel, EmailStr, constr


class UserSchema(BaseModel):
    '''
    модель данных пользователя
    '''
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestSchema(BaseModel):
    '''
    модель создаваемого пользователя
    '''
    email: EmailStr
    password: constr(min_length=3, max_length=10)
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseSchema(BaseModel):
    '''
    модель созданного пользователя
    '''
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
