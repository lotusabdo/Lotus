import math

from MatrixMusic import app 

from pyrogram.types import InlineKeyboardButton

from MatrixMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],[  
            InlineKeyboardButton(text="𝙴𝙽̃𝙳", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="𝚁𝙴𝚂𝚄𝙼𝙴", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙿𝙰𝚄𝚂𝙴", callback_data=f"ADMIN Pause|{chat_id}"),
            
        ],[
            InlineKeyboardButton(text="𝚂́𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚃𝚄𝚂", url=f"https://t.me/l2_2Y"),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/jx_xll"),
        ],[
            InlineKeyboardButton(text="#بوده { كارف الكل }× „", url=f"https://t.me/jx_xr"),
        ],[
            InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك⚡", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="𝙴𝙽̃𝙳", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="𝚁𝙴𝚂𝚄𝙼𝙴", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙿𝙰𝚄𝚂𝙴", callback_data=f"ADMIN Pause|{chat_id}"),
            
        ],[
            InlineKeyboardButton(text="𝚂́𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚃𝚄𝚂", url=f"https://t.me/l2_2Y"),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/jx_xll"),
        ],[
            InlineKeyboardButton(text="#بوده { كارف الكل }× „", url=f"https://t.me/jx_xr"),
        ],[
            InlineKeyboardButton(text="⚡اضف البوت الي مجموعتك او قناتك", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝚁𝙴𝚂𝚄𝙼𝙴",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎧 𝖲𝗎𝖿𝖿𝗅𝖾",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𝖫𝗈𝗈𝗉 ↺", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮ 10 𝖲𝖾𝖼",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="10 𝖲𝖾𝖼 ❯",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["HOME"],
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["NEXT"],
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
                InlineKeyboardButton(
                    text="🕒 0.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                ),
                InlineKeyboardButton(
                    text="🕓 0.75𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                ),
                InlineKeyboardButton(
                    text="🕤 1.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                ),
                InlineKeyboardButton(
                    text="🕛 2.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                ),
            ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
                InlineKeyboardButton(
                    text="🕒 0.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                ),
                InlineKeyboardButton(
                    text="🕓 0.75𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                ),
                InlineKeyboardButton(
                    text="🕤 1.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                ),
                InlineKeyboardButton(
                    text="🕛 2.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                ),
            ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons
