import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from MatrixMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus


iddof = []

@app.on_message(
     command(["قفل ايدي","تعطيل ايدي"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    haya = (6456857472)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == haya:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــــن"
    else:   
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")    
     
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"يا {message.from_user.mention}\n الايدي مقفله من قبل")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الايدي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")

@app.on_message(
    command(["فتح ايدي","تفعيل ايدي"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (6456857472)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == haya:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in dev:
        rotba = "مطـور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")       
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\nالايدي معفل من قبل**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم فتح امر ايدي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 
   



@app.on_message(
    filters.command(["ايدي","id","ا"], "")
& filters.group
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""🤡 ¦𝙽𝙰𝙼𝙴 :{message.from_user.mention}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{message.from_user.username}\n🎃 ¦𝙸𝙳 :`{message.from_user.id}`\n💌 ¦𝙱𝙸𝙾 :{usr.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙶𝚁𝙾𝚄𝙿 :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



iddof = []
@app.on_message(
    command(["قفل صورتي","تعطيل صورتي"])
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    haya = (6456857472)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == haya:
         rotba= "مّمٌَـبـ ـࢪمـج السوࢪس" 

    elif message.from_user.id in dev:
         rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"

    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**يا {message.from_user.mention}\n صورتي مقفلها من قبل**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**تم قفل امر صورتي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
    
@app.on_message(
    command(["فتح صورتي","تفعيل صورتي"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (5676384368)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if int(message.from_user.id) == haya:
       rotba= "مّمٌَـبـ ـࢪمـج السوࢪس"
    elif message.from_user.id in dev:
        rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمــــــن"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــــألك"
    else :
        await message.reply_text(f"**انت لست مشرفا هنا**")   
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention} صورتي مقفلها من قبل")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**تم تفعيل امر صورتي بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 



@app.on_message(
    command(["صورتي"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا طرف انت \n│ \n└ʙʏ: {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )

