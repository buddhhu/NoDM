### Copyright ©️ 2022 Amit Sharma <https://github.com/buddhhu>

from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.utils import get_display_name

from bot import db, message

__ = {}


@message(
    incoming=True,
    func=lambda event: event.is_private
    and event.sender_id not in db.get("approved")
    and not event.out
    and not event.sender.bot
    and not event.sender.is_self
    and not event.sender.verified,
)
async def inco_ming(event):
    user = await event.get_sender()
    __[user.id] = __.get(user.id, 0) + 1
    twarns = db.get("dm-limit")
    if db.get("mark-read"):
        await event.client.read(user.id)
    if __[user.id] == twarns or __[user.id] > twarns:
        if db.get("report"):
            await event.client(ReportSpamRequest(user.id))
        if db.get("block"):
            await event.client(BlockRequest(user.id))
        if db.get("delete"):
            await event.client.delete_dialog(user.id)
        await event.reply((db.get("block-message") or "Bye"))
        try:
            del __[user.id]
        except KeyError:
            pass
        return
    first_name = user.first_name
    last_name = user.last_name
    fullname = get_display_name(user)
    mention = f"[{fullname}](tg://user?id={user.id})"
    if db.get("dm-message"):
        await event.reply(
            db.get("dm-message").format(
                first_name=first_name,
                last_name=last_name,
                fullname=fullname,
                mention=mention,
                id=user.id,
                username=user.username,
                warns=__.count(user.id),
                twarns=twarns,
            ),
            link_preview=False,
        )
