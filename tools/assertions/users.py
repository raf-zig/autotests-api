from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет корректность данных пользователя
    :param actual: Фактические данные (UserSchema из ответа API).
    :param expected: Ожидаемые данные (UserSchema, с которыми сравниваем).
    """
    assert_equal(actual.user.id, expected.user.id, "id")
    assert_equal(actual.user.email, expected.user.email, "email")
    assert_equal(actual.user.last_name, expected.user.last_name, "last_name")
    assert_equal(actual.user.first_name, expected.user.first_name, "first_name")
    assert_equal(actual.user.middle_name, expected.user.middle_name, "middle_name")

def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что данные пользователя при создании (create) и при запросе (get) совпадают.
    :param get_user_response: Ответ API при получении пользователя.
    :param create_user_response: Ответ API при создании пользователя.

    """
    assert_user(actual=get_user_response, expected=create_user_response)
