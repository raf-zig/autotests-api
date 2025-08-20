from pydantic import BaseModel, EmailStr, constr, Field


class UserSchema(BaseModel):
    '''
    модель данных пользователя
    '''
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    '''
    модель создаваемого пользователя
    '''
    email: EmailStr
    password: constr(min_length=3, max_length=10)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    '''
    модель созданного пользователя
    '''
    user: UserSchema
