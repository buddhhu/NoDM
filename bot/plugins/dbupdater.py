### Copyright ©️ 2022 Amit Sharma <https://github.com/buddhhu>

from telethon.events import MessageEdited

from bot import client, db


@client.on(
    MessageEdited(
        chats=["me"],
        from_users=["me"],
        func=lambda e: e and e.id == db["database-id"],
    )
)
async def update_values(event):
    pjson = eval(event.text.replace("#NoDM").strip())
    for _ in pjson.keys():
        db.cache[_] = pjson[_]
