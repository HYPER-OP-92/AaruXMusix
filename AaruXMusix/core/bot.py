import asyncio
import uvloop
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER

# --- LOOP FIX ---
try:
    uvloop.install()
except Exception:
    pass
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

class AaruX(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="AaruXMusix",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        # --- DEBUGGING START ---
        print(f"DEBUG: Aapki LOGGER_ID ki value hai: '{config.LOGGER_ID}'")
        print(f"DEBUG: LOGGER_ID ka type hai: {type(config.LOGGER_ID)}")
        # -----------------------

        try:
            # ID ko saaf (clean) karke convert karte hain
            if config.LOGGER_ID:
                # Agar ID string hai, toh spaces hatakar integer banayenge
                raw_id = str(config.LOGGER_ID).strip()
                log_chat_id = int(raw_id)
            else:
                print("ERROR: LOGGER_ID khali hai! config check karein.")
                exit()
        except ValueError:
            print(f"ERROR: '{config.LOGGER_ID}' ek sahi number nahi hai. Isme sirf numbers hone chahiye.")
            exit()

        try:
            await self.send_message(
                chat_id=log_chat_id,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except Exception as ex:
            print(f"LOG MESSAGE SEND FAILED: {ex}")
            # Agar log group fail ho jaye, tab bhi bot ko chalne dete hain:
            pass 

        try:
            a = await self.get_chat_member(log_chat_id, self.id)
            if a.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("Please promote your bot as an admin in your log group.")
        except Exception:
            pass

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
