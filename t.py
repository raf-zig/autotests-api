import websockets

print(hasattr(websockets, 'WebSocketServerProtocol'))  # Должно быть True
print(dir(websockets))  # Посмотри, есть ли WebSocketServerProtocol