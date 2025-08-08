import httpx  # Импортируем библиотеку HTTPX

login_payload = {
    "email": "us@example.com",
    "password": "1"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("login status code:", login_response.status_code)
print("Tokens:", login_response_data)

access_token = login_response_data["token"]["accessToken"]

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})

print("Me status code:", me_response.status_code)
print("Me response:", me_response.json())
