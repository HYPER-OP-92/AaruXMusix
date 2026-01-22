from pyrogram import Client
import config
from ..logging import LOGGER
import asyncio

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AaruXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1) if config.STRING1 else None,
            no_updates=True,
        )
        # Add more assistants here if needed (self.two, etc.)

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        
        if config.STRING1:
            await self.one.start()
            
            # --- PEER ID INVALID FIX START ---
            # Hum Assistant ko force karenge ki wo saare groups ki list update kare
            try:
                async for dialog in self.one.get_dialogs(limit=20):
                    pass 
                LOGGER(__name__).info("Assistant 1 ki cache sync ho gayi hai.")
            except Exception as e:
                LOGGER(__name__).error(f"Sync error: {e}")
            # ----------------------------------

            try:
                log_id = int(config.LOGGER_ID)
                # Assistant se check karwa rahe hain ki kya use group dikh raha hai
                await self.one.get_chat(log_id) 
                await self.one.send_message(log_id, "Assistant 1 Online ✅")
            except Exception as e:
                LOGGER(__name__).error(f"Assistant 1 abhi bhi log group ko nahi dekh paa raha: {e}")
                # exit() hata diya taaki bot band na ho
            
            self.one.me = await self.one.get_me()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            assistants.append(1)
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

    async def stop(self):
        if config.STRING1:
            await self.one.stop()
