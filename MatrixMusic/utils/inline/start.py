from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="[ 𝐴𝐿𝑃𝑂𝑃 ]ِ", url=f"https://t.me/VIP_ALPOP"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text=" ⌞ 𝑆𝑂𝐔𝑅𝐶𝐸 𝐴𝐿𝑃𝑂𝑃 ⌝ ", url=f"https://t.me/SOURCE_ALPOP"
            )
        ],
     ]
    return buttons
