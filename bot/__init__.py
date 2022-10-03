### Copyright ©️ 2022 Amit Sharma <https://github.com/buddhhu>

import os
import time
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from re import compile
from traceback import format_exc
from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.sessions.string import StringSession
from telethonpatch import apply

from bot.database import db
from config import ENV

db = db()


apply()

v = 1.0
start_time = time.time()

if os.path.exists("logs.txt"):
    os.remove("logs.txt")
basicConfig(
    format="%(asctime)s || %(name)s [%(levelname)s] - %(message)s",
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
    handlers=[FileHandler("logs.txt"), StreamHandler()],
)
getLogger("Telethon").setLevel(WARNING)

log = getLogger("No DM")


client = TelegramClient(
    StringSession(ENV.SESSION), api_id=int(ENV.API_ID), api_hash=ENV.API_HASH
).start()


def message(
    pattern=None,
    **kwargs,
):
    if pattern is not None:
        pattern = compile("\\" + (db.get("handler") or ".") + pattern)
        kwargs["outgoing"] = True
    if "func" not in kwargs:
        kwargs["func"] = (
            lambda event: event.is_private
            and not event.via_bot_id
            and not event.fwd_from
        )

    def decorator(func):
        async def wrapper(event):
            try:
                await func(event)
            except Exception:
                log.error(format_exc())
                await event.client.send_message(
                    "me",
                    f"```{format_exc()}```\n\n**Report this to** @its_buddhhu",
                )

        client.add_event_handler(wrapper, NewMessage(pattern=pattern, **kwargs))
        return wrapper

    return decorator
