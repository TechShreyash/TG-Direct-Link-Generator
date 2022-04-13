# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
<i>👋 Hᴇʏ,</i>{}\n
<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n
<i>Click On Help To Get More Information</i>\n
<b><i><u>Warning 🚸</u></i></b>\n
<b>🔞 Pron Contents Leads To Permanenet Ban You.</b>"""

        HELP_TEXT = """**How to Use Me ?**

<i>- Send Me Any File Or Media From Telegram.</i>
<i>- I Will Provide External Direct Download Link !</i>

**Download Link With Fastest Speed ⚡️**

<b><i><u>Warning 🚸</u></i></b>
<b>🔞 Pron Contents Leads To Permanenet Ban You.</b></b>\n
<i>Contact Developer Or Report Bugs</i> <b>: <a href='https://t.me/TechZBots_Support'>[ Click Here ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ My Name : TG Direct Link Generator</b>\n
<b>⚜ Username : @TGDirectLinkGenBot</b>\n
<b>🔸Version : 1.0</b>\n
<b>🔹Last Updated : [ 04-Apr-22 ]</b>
"""

        stream_msg_text ="""
<u>**Successfully Generated Your Link !**</u>\n
<b>📂 File Name :</b> {}\n
<b>📦 File Size :</b> {}\n
<b>📥 Download :</b> {}\n
<b>🖥 Watch :</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/TechZBots_Support) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ],        
        [InlineKeyboardButton("Updates Channel", url='https://t.me/TechZBots'),
        InlineKeyboardButton("Repo", url='https://github.com/TechShreyash/TG-Direct-Link-Generator')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],
        [InlineKeyboardButton("Updates Channel", url='https://t.me/TechZBots'),
        InlineKeyboardButton("Repo", url='https://github.com/TechShreyash/TG-Direct-Link-Generator')]
        ]
    )