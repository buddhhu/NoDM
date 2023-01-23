### Copyright ©️ 2022 Amit Sharma <https://github.com/buddhhu>

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import User
from telethon.utils import get_display_name

from bot import message
from bot.ad import approve_in_db, disapprove_in_db


@message("ping$")
async def ping(event):
    await event.edit("Pong...")


@message("u(b|nblock)( (.*)|$)")
async def unblock(event):
    if match := event.pattern_match.group(1):
        match = [int(_) if _.isdigit() else str(_) for _ in match.strip().split(" ")]
        user = []
        for _ in match:
            try:
                user.append(await event.client.get_entity(_))
            except BaseException:
                pass
    elif event.is_private:
        user = [await event.get_chat()]
    elif event.reply_to_message_id:
        user = [(await event.get_reply_message()).sender]
    else:
        return await event.edit("`Whom to block?`")
    users = [_user for _user in user if isinstance(_user, User)]
    text = "`Unblocked` "
    for u in users:
        try:
            await event.client(UnblockRequest(u.id))
            text += f"[{get_display_name(u)}](tg://user?id={u.id}), "
        except BaseException:
            pass
    await event.edit(text[:-2])


@message("b(lock|)( (.*)|$)")
async def block(event):
    if match := event.pattern_match.group(1):
        match = [int(_) if _.isdigit() else str(_) for _ in match.strip().split(" ")]
        user = []
        for _ in match:
            try:
                user.append(await event.client.get_entity(_))
            except BaseException:
                pass
    elif event.is_private:
        user = [await event.get_chat()]
    elif event.reply_to_message_id:
        user = [(await event.get_reply_message()).sender]
    else:
        return await event.edit("`Whom to block?`")
    users = [_user for _user in user if isinstance(_user, User)]
    text = "`Blocked and Disapproved` "
    for u in users:
        try:
            await event.client(BlockRequest(u.id))
            disapprove_in_db(u.id)
            text += f"[{get_display_name(u)}](tg://user?id={u.id}), "
        except BaseException:
            pass
    await event.edit(text[:-2])


@message("a(p|pprove|)( (.*)|$)")
async def approve(event):
    if match := event.pattern_match.group(1):
        match = [int(_) if _.isdigit() else str(_) for _ in match.strip().split(" ")]
        user = []
        for _ in match:
            try:
                user.append(await event.client.get_entity(_))
            except BaseException:
                pass
    elif event.is_private:
        user = [await event.get_chat()]
    elif event.reply_to_message_id:
        user = [(await event.get_reply_message()).sender]
    else:
        return await event.edit("`Whom to approve?`")
    users = [_user for _user in user if isinstance(_user, User)]
    text = "`Approved` "
    for u in users:
        approve_in_db(u.id, get_display_name(u.id))
        text += f"[{get_display_name(u)}](tg://user?id={u.id}), "
    await event.edit(text[:-2])


@message("d(a|isapprove|)( (.*)|$)")
async def dapprove(event):
    if match := event.pattern_match.group(1):
        match = [int(_) if _.isdigit() else str(_) for _ in match.strip().split(" ")]
        user = []
        for _ in match:
            try:
                user.append(await event.client.get_entity(_))
            except BaseException:
                pass
    elif event.is_private:
        user = [await event.get_chat()]
    elif event.reply_to_message_id:
        user = [(await event.get_reply_message()).sender]
    else:
        return await event.edit("`Whom to disapprove?`")
    users = [_user for _user in user if isinstance(_user, User)]
    text = "`Disapproved` "
    for u in users:
        disapprove_in_db(u.id)
        text += f"[{get_display_name(u)}](tg://user?id={u.id}), "
    await event.edit(text[:-2])
