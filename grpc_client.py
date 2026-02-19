import grpc

import user_service_pb2
import user_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

# Отправляем запрос
response = stub.GetUser(user_service_pb2.GetUserRequest(username="Alena"))
print(response.message)  # Выведет: Привет, Alice!

#Вся подробная информация здесь https://stepik.org/lesson/1707683/step/3?unit=1731144