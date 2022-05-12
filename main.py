from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="


Shikari = Client(
    "Lyrics_Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Shikari.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hai {} \n\n**I Am Lawless Lyrics Bot❤️. Send Me A Song Name, I Will Give You The Lyrics. ** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel 🔰", url = "https://t.me/Lawless_Updates"),InlineKeyboardButton("Support Group ⭕️", url = "https://t.me/ShikariSupportNetwork")],[InlineKeyboardButton("Repo 🗂️", url = "https://github.com/ShikariBaaZ/Lyrics_Bot"),InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/ShikariBaaZ/Lyrics_Bot")],[InlineKeyboardButton("Developer 💡", url = "https://github.com/ShikariBaaZ/")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Shikari.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me A Song Name, I Will Give You Lyrics Of That Song. \nBot By💐 @Lawless_Updates "
    HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Channel", url = "https://t.me/Lawless_Updates"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/ShikariBaaZ/Lyrics_Bot")]])
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Shikari.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**🤖 Bot :** Lawless Lyrics Bot\n\n**🧑‍💻 Developer :** [Shikari](https://github.com/ShikariBaaZ)\n\n**💻 Channel :** @Lawless_Updates\n\n**☎️ Support :** @ShikariSupportNetwork \n\n**🗂️ Source Code :** [Lawless Lyrics Bot](https://github.com/ShikariBaaZ/Lyrics_Bot)\n\n**⚙️ Language :** Python 3\n\n**🛡️ Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)

@Shikari.on_message(filters.private & filters.text)
async def sng(bot, message):
        hy = await message.reply_text("`Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song)
        await hy.delete()
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Dev 🔥 ", url = f"github.com/ShikariBaaZ")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://t.me/Lawless_Updates"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/ShikariBaaZ/Lyrics_Bot")]]))
        except Exception as e:
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer🔥", url = f"github.com/ShikariBaaZ")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://t.me/Lawless_Updates"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/ShikariBaaZ/Lyrics_Bot")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Made With ❤️ By @Lawless_Updates**'
        return text


Ek.run()
