import random
import requests
from PyroUbot import *

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ai"
__HELP__ = f"""
<b>『 chat gpt 』</b>

  <b>• perintah:</b> <code>.ai</code>
  <b>• penjelasan:</b> buat pertanyaan contoh .ai siapa nama presiden Indonesia
"""

@PY.UBOT("gemini")
async def chat_gemini(ubot, message):
    try:
        await ubot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "Contoh :-\n.gemini siapa nama presiden Indonesia?"
            )
        else:
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://widipe.com/openai?text={a}')

            try:
                # Check if "results" key is present in the JSON response
                if "text" in response.json():
                    x = response.json()["text"]                  
                    await message.reply_text(
                      f"{x}",
                        parse_mode=ParseMode.MARKDOWN
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                # Handle any other KeyError that might occur
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"**á´‡Ê€Ê€á´Ê€: {e} ")
