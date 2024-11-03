from PyroUbot import *
__MODULE__ = "ᴄᴀᴛᴜʀ"
__HELP__ = """
<b>『 bantuan untuk game 』</b>

  <b>• perintah:</b> <code>{0}catur</code></code>
  <b>• penjelasan:</b> untuk memanggil game catur
"""



@PY.UBOT("catur")
async def _(client, message):
    await catur_cmd(client, message)
