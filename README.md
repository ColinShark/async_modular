# async_modular

A modular asynchronous Pyrogram Client.

## Installation

First install the requirements:

```powershell
pip install -r requirements.txt
```

Then place a `my_bot.ini` in the root folder of this repository.

```ini
[pyrogram]
api_id = <your API ID here>
api_hash = <your API HASH here>
```

The values needed for the `.ini` are available at [my.telegram.org](https://my.telegram.org/auth?to=apps).

After that, execute with

```powershell
python -m my_bot
```

## More Plugins / Modules

To add more functionality, just add another file in the [my_bot/plugins](my_bot/plugins) folder.

Each module should start like this:

```python
from pyrogram import Filters

from ..my_bot import My_Bot
```

## Documentation

Each usable Method is explained and documented on [Pyrogram.org](https://docs.pyrogram.org).

There is some commentary in the example files of this repository.
