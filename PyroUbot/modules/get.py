
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from PyroUbot.core.helpers.msg_type import ReplyCheck
from PyroUbot import *

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

__MODULE__ = "ɢᴇᴛ"
__HELP__ = f"""
『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴇᴛ 』

• ᴘᴇʀɪɴᴛᴀʜ: <code>.ɢᴇᴛsᴇʟᴇs</code>
• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴜsᴇʀ ʀᴇsᴇʟʟᴇʀ ᴅɪ ᴜsᴇʀʙᴏᴛ

• ᴘᴇʀɪɴᴛᴀʜ: <code>.ɢᴇᴛᴘʀᴇᴍ</code>
• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴜsᴇʀ ᴘʀᴇᴍɪᴜᴍ ᴅɪ ᴜsᴇʀʙᴏᴛ

ᴋʜᴜsᴜs ʟᴇxᴄᴢ
"""
