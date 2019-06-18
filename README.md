# async_modular

This repository contains a template based on [PyrogramBot](https://github.com/Pyrogram/Assistant) and the instructions for setting it up yourself.

This template features [Pyrogram Asyncio](https://github.com/pyrogram/pyrogram/issues/181) and [Smart Plugins](https://docs.pyrogram.org/topics/smart-plugins). Feel free to explore the Source Code and the [Documentation](https://docs.pyrogram.org) to learn more about these topic.

## Requirements

* Python3.6 or higher.
* A [Telegram API Key](https://docs.pyrogram.org/intro/setup#api-keys).

## Run

1. `git clone https://github.com/Pyrogram/async_modular`, to download the source code.
2. `cd async_modular`, to enter the directory.
3. `pip install -r requirements.txt`, to install the requirements.
4. Create a new `my_bot.ini` file, copy-paste the folowing and replace the values with your own:

```ini
[pyrogram]
api_id = 123456
api_hash = 0123456789abcdef0123456789abcdef
```

5. Run with python3 -m my_bot, stop with <kbd>CTRL+C</kbd>

## License

MIT © 2019 [Dan](https://github.com/Delivrance) & [Colin](https://github.com/ColinTheShark)
