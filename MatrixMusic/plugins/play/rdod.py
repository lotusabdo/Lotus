import asyncio
from pyrogram import Client, filters ,enums
from strings.filters import command
from pyrogram.types import *
from MatrixMusic import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ParseMode, ChatMemberStatus

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}AHMEDRD")[1].replace("\n",""))
    return False

def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}AHMEDRD{rd}\n")
    return True


def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return



def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return


@app.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "- قائمة المشرفين\n— — — — —\n"
    async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f"› {'@'+admins.user.username if admins.user.username else admins.user.mention} - `{admins.user.id}` .\n"
    await message.reply(text=(admin))

@app.on_message(filters.regex("^البوتات$"))
async def botslist(_, message):
    chat_id = message.chat.id
    rnryr = "- قائمة البوتات\n— — — — —\n"
    async for b in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
           rnryr+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(ahmed))

@app.on_message(filters.regex("^بايو$"))
async def Bio(_, message):
    if not message.reply_to_message:
     me = message.from_user.id
     b = await app.get_chat(me)
     bio = b.bio
     await message.reply_text(bio)
	


