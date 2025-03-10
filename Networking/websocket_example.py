"""
WebSocket is a protocol that enables bidirectional communication between client and
server, ideal for real-time applications like chat or gaming. Unlike HTTP, which is requestresponse-based, WebSocket establishes a persistent connection, allowing continuous data
exchange. WebSocket starts with an HTTP handshake, then upgrades to a WebSocket
connection.
"""

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)


start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()