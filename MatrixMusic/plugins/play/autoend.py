from pyrogram import filters

import config
from strings.filters import command
from MatrixMusic import app
from MatrixMusic.misc import SUDOERS
from MatrixMusic.utils.database import autoend_off, autoend_on
from MatrixMusic.utils.decorators.language import language


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "انهاء البث التلقائي.\n\nيسترك المساعد المكالمه تلقائيا لان بقي وحيدا دون مستمعين مده طويله."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("المغادره التلقائيه معطله")
    else:
        await message.reply_text(usage)
