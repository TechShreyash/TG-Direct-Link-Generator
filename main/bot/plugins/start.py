# This file is a part of TG-Direct-Link-Generator

from main.bot import StreamBot
from main.vars import Var
from pyrogram import filters
from main.utils.Translation import Language, BUTTON

@StreamBot.on_message(~filters.user(Var.BANNED_USERS) & filters.command('start') & ~filters.edited)
async def start(b, m):
    # lang = getattr(Language, m.from_user.language_code)
    lang = getattr(Language, "en")
    await m.reply_text(
        text=lang.START_TEXT.format(m.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTON.START_BUTTONS
        )


@StreamBot.on_message(~filters.user(Var.BANNED_USERS) & filters.command(["about"]) & ~filters.edited)
async def start(bot, update):
    # lang = getattr(Language, update.from_user.language_code)
    lang = getattr(Language, "en")
    await update.reply_text(
        text=lang.ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTON.ABOUT_BUTTONS
    )


@StreamBot.on_message((filters.command('help')) & ~filters.edited & ~filters.user(Var.BANNED_USERS))
async def help_handler(bot, message):
    # lang = getattr(Language, message.from_user.language_code)
    lang = getattr(Language, "en")
    await message.reply_text(
        text=lang.HELP_TEXT.format(Var.UPDATES_CHANNEL),        
        disable_web_page_preview=True,
        reply_markup=BUTTON.HELP_BUTTONS
        )
