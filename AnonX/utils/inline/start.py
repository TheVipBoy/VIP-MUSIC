from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌹𝐀𝐃𝐃🔥𝐌𝐄🙈𝐁𝐀𝐁𝐘🌹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="💫𝐑𝐄𝐏𝐎💫", url=f"https://t.me/vip_creators"),
            InlineKeyboardButton(
                text="✨𝐕𝐈𝐏 𝐃𝐔𝐍𝐈𝐀✨", url=f"https://t.me/VIP_DUNIA"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🔥𝐓𝐠 𝐌𝐚𝐧𝐚𝐠𝐞𝐫 𝐑𝐨𝐛𝐨𝐭🔥", url=f"https://t.me/TG_MANAGER_ROBOT?startgroup=true"
                )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌹𝐀𝐃𝐃🔥𝐌𝐄🙈𝐁𝐀𝐁𝐘🌹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="💫𝐑𝐄𝐏𝐎💫", url=f"https://t.me/vip_creators"),
            InlineKeyboardButton(
                text="✨𝐕𝐈𝐏 𝐃𝐔𝐍𝐈𝐀✨", url=f"https://t.me/VIP_DUNIA"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🔥𝐓𝐠 𝐌𝐚𝐧𝐚𝐠𝐞𝐫 𝐑𝐨𝐛𝐨𝐭🔥", url=f"https://t.me/TG_MANAGER_ROBOT?startgroup=true"
                )
        ],
     ]
    return buttons
