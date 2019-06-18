from configparser import ConfigParser

from pyrogram import Client


class My_Bot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()  # The name of the Class
        config_file = f"{name}.ini"

        config = ConfigParser()
        config.read(config_file)

        super().__init__(
            name,
            config_file=config_file,
            workers=8,
            plugins=dict(root=f"{name}/plugins")
        )

        async def start(self):
            await super().start()
            print("Successfully logged in as @" + self.get_me().first_name)

        async def stop(self):
            await super().stop()
            print("Successfully stopped")
