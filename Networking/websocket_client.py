"""
To create a WebSocket client in Python, use the websockets library. This client connects to a
WebSocket server and can send and receive messages in real-time.
"""

import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(response)


asyncio.run(hello())