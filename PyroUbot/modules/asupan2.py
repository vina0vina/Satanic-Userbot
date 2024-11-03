from PyroUbot import *

__MODULE__ = "asupan 2"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ 2 』</b>
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}anime</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ʀᴀɴᴅᴏᴍ
"""

@PY.UBOT("anime")        
async def photo_anime(client, message):
    y = await message.reply_text(emoji("proses") + f"**mencari anime...**", quote=True)
    anime_channel = random.choice(["@animehikarixa", "@anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in client.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
