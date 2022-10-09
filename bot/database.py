### Copyright ©️ 2022 Amit Sharma <https://github.com/buddhhu>

null, true, false = None, True, False


class db:
    def __init__(self):
        self.cache = {}
        self.template = {
            "block": True,
            "delete-chat": True,
            "report": True,
            "mark-read": True,
            "media-msg": None,
            "dm-limit": 3,
            "dm-message": "Hey {mention}\nDon't dm",
        }

    def get(self, key: str):
        return self.cache.get(key)

    def update(self, value):
        self.cache = eval(value)
