from pyrogram import Client, filters
from AaruXMusix import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(filters.command("owner") & filters.group)


async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://files.catbox.moe/ars2tf.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/II_RAJPUT_SHIV_OP_II"
                    )],
            ]
        ),
    )


@app.on_message(filters.command("owner") & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://files.catbox.moe/ars2tf.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/II_RAJPUT_SHIV_OP_II"
                    )],
            ]
        ),
    )


@app.on_message(filters.command("owner") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://files.catbox.moe/ars2tf.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐎ᴡɴᴇʀ 🗡️", url=f"https://t.me/II_RAJPUT_SHIV_OP_II"
                    )],
            ]
        ),
    )
