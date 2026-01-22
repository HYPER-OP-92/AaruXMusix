from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.clients = []
        # Hum 1 se 5 tak check karenge ki kitni strings available hain
        for i in range(1, 6):
            string = getattr(config, f"STRING{i}", None)
            if string:
                client = Client(
                    name=f"AaruXAss{i}",
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=str(string),
                    no_updates=True,
                )
                self.clients.append((i, client))
                # Purane format ke liye compatibility
                if i == 1: self.one = client
                elif i == 2: self.two = client
                elif i == 3: self.three = client
                elif i == 4: self.four = client
                elif i == 5: self.five = client

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        
        # Logger ID ko number mein badlein
        try:
            log_id = int(config.LOGGER_ID)
        except (ValueError, TypeError):
            LOGGER(__name__).error("LOGGER_ID galat hai! Please check config.")
            log_id = None

        for i, client in self.clients:
            await client.start()
            
            # Group Join Logic (Dns_Official_Channel)
            try:
                await client.join_chat("Dns_Official_Channel")
            except Exception:
                pass

            # Logger Group Check
            if log_id:
                try:
                    await client.send_message(log_id, f"Assistant {i} Started ✅")
                except Exception as e:
                    LOGGER(__name__).error(
                        f"Assistant {i} log group tak nahi pahunch pa raha. "
                        f"Reason: {e}"
                    )
                    # exit() ko hata diya hai taki bot band na ho
            
            # Details save karein
            client.me = await client.get_me()
            client.id = client.me.id
            client.name = client.me.mention
            client.username = client.me.username
            
            assistants.append(i)
            assistantids.append(client.id)
            LOGGER(__name__).info(f"Assistant {i} Started as {client.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        for _, client in self.clients:
            try:
                await client.stop()
            except:
                pass
