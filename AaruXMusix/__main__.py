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
    # 1. Essential checks
    if not config.STRING1:
        LOGGER(__name__).error("STRING1 missing!")
        exit()

    await sudo()

    # 2. Start Main Bot (API)
    await app.start()
    LOGGER("AaruXMusix").info("Main Bot Started. Checking Log Group...")

    # --- NUCLEAR DEBUG START (Isse pata chal jayega asli galti kya hai) ---
    try:
        # 1. ID ko saaf karein (Spaces hatayein)
        raw_id = str(config.LOGGER_ID).strip()
        log_id = int(raw_id)

        # 2. Bot se kahein ki wo Group ki details nikaale (Sync)
        LOGGER("AaruXMusix").info(f"Checking access for ID: {log_id}...")
        chat = await app.get_chat(log_id)
        
        # 3. Message bhejne ki koshish
        await app.send_message(
            log_id, 
            f"✅ **Bot Online Ho Gaya Hai!**\n\n**Group Name:** {chat.title}\n**Bot Admin Hai:** Haan"
        )
        LOGGER("AaruXMusix").info(f"SUCCESS: Bot ne '{chat.title}' mein message bhej diya!")

    except Exception as e:
        # Yahan terminal par asli Error dikhega
        LOGGER("AaruXMusix").error(f"DETAILED ERROR: {e}")
        print(f"\n--- DEBUG INFO ---")
        print(f"Config ID: {config.LOGGER_ID}")
        print(f"Error Type: {type(e).__name__}")
        print(f"------------------\n")
    # --- DEBUG END ---

    # 3. Load Plugins
    for all_module in ALL_MODULES:
        importlib.import_module("AaruXMusix.plugins" + all_module)
    
    # 4. Start Assistant
    await userbot.start()
    
    # Wait for sync
    await asyncio.sleep(5)
    
    await AaruXMusix.start()

    # 5. Voice Chat Check
    try:
        await AaruXMusix.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AaruXMusix").error("Log Group Voice Chat On Nahi Hai!")
        exit()
    except Exception as e:
        LOGGER("AaruXMusix").error(f"VC Error: {e}")
        exit()

    await AaruXMusix.decorators()
    LOGGER("AaruXMusix").info("Rudra Music Bot Started!")
    
    await idle()
    await app.stop()
    await userbot.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
