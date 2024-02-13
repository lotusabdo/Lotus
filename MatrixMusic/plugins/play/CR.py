import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/8e889b909ac6011b4cde2.mp4",
        caption=f"""\nمرحبا بك عزيزي {message.from_user.mention} في قسم سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/jx_xll"), 
                 InlineKeyboardButton(
                   "𝚂́𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚃𝚄𝚂",       url=f"https://t.me/l2_2Y"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "#بوده { كارف الكل }× „", url=f"https://t.me/jx_xr"), 
                 
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس","المبرمج","مبرمج"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("jx_xr")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𓏺 َِՏΌႮᎡᏟᎬ ᎡᎥΝΌ \n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\nՏΌႮᎡᏟᎬ ᎡᎥΝΌ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["بوده" , "فوديكا","ميشو"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("jx_xr")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𓏺➥𝚂́𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚃𝚄𝚂♲ .\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n➥𝚂́𝙾𝚄𝚁𝙲𝙴 𝙻𝙾𝚃𝚄𝚂♲", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



