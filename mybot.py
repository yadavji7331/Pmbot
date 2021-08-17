# My person bot
# Only to get Request 

import os
import re
import html
import time 

from datetime import datetime
### imports == Telethon 
from telethon import Button 
from telethon import events 
from telethon import TelegramClient 
from telethon.utils import pack_bot_file_id


# config # 
from config import config
## <--- Import finish --->

### ALL CONFIGS ###

USERNAME = config.OWNER_USERNAME
OWNER_ID = config.OWNER_ID
PIC = config.PIC
DB_URI = config.DB_URI

### Here 4 later purpose ###
### Telethon ###
API_ID = config.API_ID
API_HASH = config.API_HASH
TOKEN = config.TOKEN





pm = TelegramClient("lover", API_ID, API_HASH).start(bot_token=TOKEN)






 
# <----Setup Finished----> #
# <i> © @Alone_loverboy <i/> #

text = f"""
H! ✨
I**I am @{USERNAME} Personal BoT ^•^ **
Drop Your RequestWhy are you Here😶. 
__Follow HIM IN INSTAGRAM AND TWITTER 😁🤩__\n
**Join OuR Community😘** __on Telegram__
**CHOOSE WHY ARE YOU HERE:**
"""


SOCIAL = f"""
H!👀 Welcome To Social menu 
{USERNAME} social media Is here✨
• You can follow **TWITTER**& **Instagram**
"""

TELE = """
H!✨ 
Join our community 😄
Our All community on Telegram 
 Are given below:
 
"""

@pm.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event): 
      await pm.send_file(event.chat_id, PIC, caption=text, buttons=[
            [Button.inline("Social media📱", data="social"),
             Button.inline("Telegram community👫", data="tele")
            ],
            [
              Button.inline("TO request something😓", data="some"),
              Button.inline("For Help🚶", data="hell")
              ],
              [Button.inline("HELP for my github project", data="gith")
              ],
              [Button.url("♠️Itz_Loverboy♠️", url="https://t.me/itz_loverboy")
            ]
          ],
            link_preview=True)
        
      
   
@pm.on(events.callbackquery.CallbackQuery(data="social"))
async def social(event): 
      await event.edit(SOCIAL, buttons=[
            [Button.url("Instagram", url="https://instagram.com/mesterious.person")
            ],
            [Button.url("Twitter", url="https://twitter.com/A_Modern_Mind")],
            [Button.inline("Back🚶", data="ok")],
            ])
            
         
       
     
   
@pm.on(events.callbackquery.CallbackQuery(data="tele"))
async def tele(event):
      await event.edit(TELE, buttons=[
            [Button.url("PsychoBots", url="https://t.me/Psycho_Bots"),
             Button.url("Chatting Group", url="https://t.me/Astro_Spam")
            ],
            [
             Button.url("Quotes✍️", url="https://t.me/Itz_loverboy"),
             Button.url("UserBoT", url="http://t.me/Astro_UserBot")],
             [Button.inline("Back🚶", data="ok")]
             ])
           
        
     
   
@pm.on(events.callbackquery.CallbackQuery(data="some"))
async def some(event):
      await event.edit("Yeah.... You can ask \nMy master will reply soon if he knew about me..\nBE patience😊", buttons=[
          [Button.inline("Back🏃🏻", data="ok")]
          ])
          
        
      
   
@pm.on(events.callbackquery.CallbackQuery(data="hell"))
async def hell(event):
      await event.edit("What you wanna to help🤔 Leave ur message my master will reply soon if he can help u", buttons=[
          [Button.inline("Back🏃🏻", data="ok")]
          ]) 
       
     
   
@pm.on(events.callbackquery.CallbackQuery(data="gith"))
async def gith(event):
      await event.edit("okok...You need help for your repository🙂\nLeave Your repository with your error Message or screenshot\nmy master will help u soon", buttons=[
          [Button.inline("Back🏃🏻", data="ok")]
          ])
        
      
    
@pm.on(events.callbackquery.CallbackQuery(data="ok"))
async def ok(event):
      await event.delete()
      await pm.send_file(event.chat_id, PIC, caption=text, buttons=[
            [Button.inline("Social media📱", data="social"),
             Button.inline("Telegram community👫", data="tele")
            ],
            [
              Button.inline("TO request something😓", data="some"),
              Button.inline("For Help🚶", data="hell")
              ],
              [Button.inline("HELP for my github project", data="gith")
              ],
              [Button.url("♠️Itz_Loverboy♠️", url="https://t.me/itz_loverboy")
            ]
          ],
            link_preview=True)
        
    ### QUERIES ###
   
@pm.on(events.NewMessage(pattern="/ask"))
async def ask(event):
    await event.reply(f"Hey\nThis is Lovers Personal bot😄\n\nUse ask | Your queries\n use that format and my master will reply you soon through me🙂be patience till😄\nDon't Send Media🙂")
    
### PING ## 

@pm.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    if event.fwd_from:
        return
    start = datetime.now()
    
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.reply(f"""
⎝⎝•𝙋𝙊𝙉𝙂•⎠⎠\n
. 　   ♡＿＿＿
　　   ∥  MY MS |
　　   ∥`{ms}`s |
　　   ∥￣￣￣￣
 ∧＿∧
(  ･ω･∥  ☆
丶　つ０
 しーＪ
 
**❦𝙼𝚈 𝙿𝚁𝙾 𝙼𝙰𝚂𝚃𝙴𝚁❦ **→ [🂡『𝄞⃝Ⱡⓞꪜє℟ ♪⃝⃤B͛Ꮻ𝐘』🂡](https://t.me/Alone_loverboy)
""", 
link_preview=False
)

### Help ## 

@pm.on(events.NewMessage(pattern="/help"))
async def _(event):
    await event.reply(f"H!✨.This is Personal BoT of @{USERNAME}\n\n You guys can contact to him through me😊check `/about` For more information related to my master🙂\n\n I am Totally Programmed by @{USERNAME}")
    
### UNLESS 😂###

@pm.on(events.NewMessage(pattern="/about"))
async def about(event):
    await event.reply(f"H!✨\nYou wanna to know About me😂? read Below\n\nABOUT @{USERNAME}:-\n •My name:- Dev Adarsh pandit🇮🇳\n •My age:- Unknown🙂\n •Computer language:- Web development(learning), Python more soon😁\n•I am a quotes writer too•🤤\ncheck [Itz_LoverBoy](https://t.me/Itz_loverboy) For More",
    link_preview=False 
    )
    
#### Messages Forwarder ####
# {Telethon} #
## [<---incoming--->] ##

@pm.on(events.NewMessage(func=lambda e: e.is_private))
async def one_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.get_sender()
        event.chat_id
        await event.forward_to(OWNER_ID)
        
     

# below is startup

pm.run_until_disconnected()


# © @Alone_loverboy
