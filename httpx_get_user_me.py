import httpx

login_payload = {
    "email": "Alena@example.com",
    "password": "123"
}
# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)
login_response_data = login_response.json()

access_token = login_response_data["token"]["accessToken"]

print(access_token)

user_me_response = httpx.get("http://localhost:8000/api/v1/users/me",
                             headers={"Authorization": f"Bearer {access_token}"})

print(user_me_response.json())