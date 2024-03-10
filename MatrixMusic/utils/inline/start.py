from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url= "https://t.me/jx_xll"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور البوت", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/jx_xll"), 
        ],
        [
            
            InlineKeyboardButton(text="𝚂́𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚃𝚄𝚂", url=f"https://t.me/l2_2Y") , 
        ],
    ]
    return buttons
