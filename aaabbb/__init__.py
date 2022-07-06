"""aaabbb"""
import asyncio

__version__ = "0.0.1"


async def count():
    """ Count seconds indefinitely. """
    i = 0
    while True:
        print(i)
        i = i + 1
        await asyncio.sleep(1)


fizzbuzz = {
    "fives": {
        "message": "buzz",
        "wait": 5,
    },
    "threes": {
        "message": "fizz",
        "wait": 3,
    },
}


class Connection:
    """ A connection to an endpoint. """
    def __init__(self, connection):
        self.message = connection["message"]
        self.open = True
        self.wait = connection["wait"]
        print(f"say {self.message} every {self.wait} seconds")

    def close(self):
        """ Close the connection. """
        self.open = False

    async def listen(self):
        """ Manage the connection. """
        while self.open:
            await asyncio.sleep(self.wait)
            print(self.message)


class Client:
    """ A client may have many connections. """
    def __init__(self, config):
        self.config = config
        # connections = config.get("connections", [])
        self.connections = fizzbuzz
        self.active = []
        asyncio.run(self.run())

    async def connect(self, connection):
        """ Initiate a connection. """
        cnx = Connection(connection)
        task = await asyncio.create_task(cnx.listen())
        self.active.append(task)

    async def run(self):
        """ Include each connection in the event loop. """
        try:
            await asyncio.wait_for(asyncio.gather(
                count(),
                *[
                    self.connect(connection)
                    for connection in self.connections.values()
                ],
            ), 17)
        except asyncio.TimeoutError:
            print("Done for now.")


def serve():
    """Start server."""
    # config = load_config_from_file(CONFIG_FILE)
    config = {}
    Client(config)
