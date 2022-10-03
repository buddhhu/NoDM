### Copyright ©️ 2022 Amit Sharma <https://github.com/buddhhu>

from bot import db


def approve_in_db(user_id: int, name: str):
    if int(user_id) not in db.get("approved"):
        db.cache["approved"][int(user_id)] = name


def disapprove_in_db(user_id: int):
    if int(user_id) in db.get("approved"):
        del db.cache["approved"][int(user_id)]
