from aiogram.types import Message
from loader import dp
from aiogram import F
from aiogram.filters import or_f

# @dp.message(or_f(F.voice, F.audio))
# async def voice_handler(message: Message):
#     if message.voice:
#         file_id = message.voice.file_id
#         text = f"Voice ID: <code>{file_id}</code>"
#         await message.answer(text, parse_mode="HTML")
#         await message.answer_voice(file_id)
    
#     elif message.audio:
#         file_id = message.audio.file_id
#         text = f"Audio ID: <code>{file_id}</code>"
#         await message.answer(text, parse_mode="HTML")
