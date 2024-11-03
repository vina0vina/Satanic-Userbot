
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot.core.helpers.msg_type import ReplyCheck
from PyroUbot import *


@ubot.on_message(filters.command("seles") & filters.me)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("unseles") & filters.me)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("prem") & filters.me)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@ubot.on_message(filters.command("unprem") & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

__MODULE__ = "ᴏᴡɴᴇʀ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴡɴᴇʀ 』

• ᴘᴇʀɪɴᴛᴀʜ: <code>.seles</code>
• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴᴊᴀᴅɪᴋᴀɴ ᴜsᴇʀ ᴍᴇɴᴊᴀᴅɪ ʀᴇsᴇʟʟᴇʀ

• ᴘᴇʀɪɴᴛᴀʜ: <code>.unseles</code>
 ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴɢʜᴀᴘᴜs ᴜsᴇʀ ᴅᴀʀɪ ʀᴇsᴇʟʟᴇʀ
•
• ᴘᴇʀɪɴᴛᴀʜ: <code>.prem</code>
• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴᴊᴀᴅɪᴋᴀɴ ᴜsᴇʀ ᴍᴇɴᴊᴀᴅɪ ᴘʀᴇᴍɪᴜᴍ

• ᴘᴇʀɪɴᴛᴀʜ: <code>.unprem</code>
• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴍᴇɴɢʜᴀᴘᴜs ᴜsᴇʀ ᴅᴀʀɪ ᴘʀᴇᴍɪᴜᴍ
"""
