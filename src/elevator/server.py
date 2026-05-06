import asyncio
from websockets.asyncio.server import serve

import elevator


elevator = elevator.ElevatorStringController()


async def echo(websocket):
    async for message in websocket:
        message = message.split()
        response = elevator.command(*message)
        await websocket.send(str(response))


async def async_main():
    async with serve(echo, "localhost", 8765) as server:
        await server.serve_forever()


def main():
    asyncio.run(async_main())
