import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AaruXMusix import LOGGER, app, userbot
from AaruXMusix.core.call import AaruXMusix
from AaruXMusix.misc import sudo
from AaruXMusix.plugins import ALL_MODULES
from AaruXMusix.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # Check if strings are provided
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()

    await sudo()

    # Load Banned Users
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    # Start Bot (app)
    await app.start()
    LOGGER("AaruXMusix").info("Bot Started ✅")

    # Load Plugins
    for all_module in ALL_MODULES:
        importlib.import_module("AaruXMusix.plugins" + all_module)
    LOGGER("AaruXMusix.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    # Start Assistant (Userbot)
    await userbot.start()
    
    # --- PROPER SYNC FIX ---
    # Assistant ko group ke details fetch karne ke liye thoda waqt dena zaroori hai
    LOGGER("AaruXMusix").info("Assistant sync ho raha hai... 7 second rukein.")
    await asyncio.sleep(7) 
    
    # Start PyTgCalls (Music Core)
    await AaruXMusix.start()

    # Stream Check in Log Group
    try:
        await AaruXMusix.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AaruXMusix").error(
            "\n\n❌ ERROR: LOG GROUP ME VOICE CHAT NAHI MILI!\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "1. Check karein ki Log Group me Voice Chat ON hai.\n"
            "2. Check karein ki ASSISTANT group me ADMIN hai.\n"
            "3. Admin permissions me 'MANAGE VIDEO CHATS' ON hona chahiye.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        )
        exit()
    except Exception as e:
        LOGGER("AaruXMusix").error(f"Startup Call Error: {e}")
        # Agar koi aur badi error ho tabhi band karein
        exit()

    await AaruXMusix.decorators()
    LOGGER("AaruXMusix").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗥𝗨𝗗𝗥𝗔☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AaruXMusix").info("𝗦𝗧𝗢𝗣 𝗥𝗨𝗗𝗥𝗔 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    # Python 3.10+ loop correction
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
