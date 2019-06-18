from configparser import ConfigParser
# Import ConfigParser, so we can parse our config file

from pyrogram import Client
# Import the Client from pyrogram


class My_Bot(Client):
    def __init__(self):
        # Initialise the My_Bot class, which inherites from Client
        name = self.__class__.__name__.lower()  # The name of the Class
        config_file = f"{name}.ini"

        config = ConfigParser()  # Initialise ConfigParser
        config.read(config_file)  # read our configuration file

        super().__init__(
            name,
            config_file=config_file,
            workers=8,
            plugins=dict(root=f"{name}/plugins")
        )

        async def start(self):
            # Overwriting the Client.start() method, which is called by .run()
            await super().start()
            print("Successfully logged in as @" + self.get_me().first_name)

        async def stop(self):
            # Overwriting the Client.stop() method,
            # which is called when we stop the Client.
            await super().stop()
            print("Successfully stopped")
