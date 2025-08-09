import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "st",
    "lastName": "str",
    "firstName": "stri",
    "middleName": "strin"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create status code:", create_user_response.status_code)
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login status code:", login_response.status_code)
print('Login data:', login_response_data)

# Получаем данные пользователя
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

patch_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=get_user_headers,
    json={
      "email": get_random_email(),
      "lastName": "st",
      "firstName": "str",
      "middleName": "stri"
    }
)
patch_user_response_data = patch_user_response.json()

print("Patch status code:", patch_user_response.status_code)
print('Patch user data:', patch_user_response_data)