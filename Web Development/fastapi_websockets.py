"""
FastAPI provides built-in support for WebSocket connections, allowing bidirectional
communication between the client and server. WebSockets are ideal for real-time
applications where updates need to be pushed to the client without refreshing the page,
such as chat applications or live notifications.
"""

from fastapi import FastAPI, WebSocket

app = FastAPI()

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")