"""
Implementing a WebSocket server in Python can be achieved using the websockets library.
A WebSocket server listens for incoming client connections and manages real-time,
bidirectional communication. The server can handle multiple clients, sending and receiving
messages asynchronously.
"""

import asyncio
import websockets

# Define the server handler to manage incoming connections
async def server(websocket, path):
    # Receive and print messages from the client
    async for message in websocket:
        print(f"Received message: {message}")
        # Send a response back to the client
        await websocket.send(f"Message received: {message}")


# Start the WebSocket server on localhost:8765
start_server = websockets.serve(server, "localhost", 8765)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()