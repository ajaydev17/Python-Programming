"""
# Making multiple requests with the same session
response1 = session.get("https://api.example.com/profile")
response2 = session.get("https://api.example.com/settings")
# Displaying responses
print("Profile Data:", response1.json())
print("Settings Data:", response2.json())
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