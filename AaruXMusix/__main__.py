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
    # 1. String Session Check
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()

    # 2. Sudo and Database Load
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    # 3. Main Bot (app) Start
    await app.start()
    LOGGER("AaruXMusix").info("Main Bot Started ✅")

    # 4. Main Bot Permission Test (Log Group Check)
    try:
        await app.send_message(
            config.LOGGER_ID, 
            "✨ **Main Bot Online!**\n\nAb Assistant start ho raha hai, thoda intezaar karein..."
        )
        LOGGER("AaruXMusix").info("Main Bot ne Log Group mein startup message bhej diya hai.")
    except Exception as e:
        LOGGER("AaruXMusix").error(
            f"Main Bot Log Group me message nahi bhej pa raha!\n"
            f"Reason: {e}\n"
            f"Fix: Bot ko Log Group me Admin banayein."
        )
        # Hum bot ko band nahi karenge, shayad assistant bhej sake, par error dikhayenge.

    # 5. Load Plugins
    for all_module in ALL_MODULES:
        importlib.import_module("AaruXMusix.plugins" + all_module)
    LOGGER("AaruXMusix.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    # 6. Start Assistant (Userbot)
    await userbot.start()
    
    # --- VC SYNC DELAY (IMPORTANT) ---
    LOGGER("AaruXMusix").info("Assistant sync ho raha hai... 7 second rukein.")
    await asyncio.sleep(7) 
    
    # Start Music Core (PyTgCalls)
    await AaruXMusix.start()

    # 7. Voice Chat Detection Check
    try:
        # Check if VC is active in the Log Group
        await AaruXMusix.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AaruXMusix").error(
            "\n\n❌ ERROR: LOG GROUP ME VOICE CHAT NAHI MILI!\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "FIX: Apne Log Group me Voice Chat ON karein aur Assistant ko Admin banayein.\n"
            "Bot ab band ho raha hai kyunki bypass allowed nahi hai.\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        )
        exit()
    except Exception as e:
        LOGGER("AaruXMusix").error(f"Startup Call Error: {e}")
        exit()

    await AaruXMusix.decorators()
    LOGGER("AaruXMusix").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗥𝗨𝗗𝗥𝗔☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    
    # Keep bot running
    await idle()
    
    # Stop all services on shutdown
    await app.stop()
    await userbot.stop()
    LOGGER("AaruXMusix").info("𝗦𝗧𝗢𝗣 𝗥𝗨𝗗𝗥𝗔 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    # Python 3.10+ event loop fix
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
