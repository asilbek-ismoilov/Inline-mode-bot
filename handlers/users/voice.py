from aiogram.types import Message, InlineQuery, InlineQueryResultCachedVoice
from loader import dp, db
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

# -----------------------------------------------------------------------

# @dp.inline_query() 
# async def inline_voice_search(inline_query: InlineQuery): 
#     results = [ 
#         InlineQueryResultCachedVoice( 
#             id="1", 
#             voice_file_id="AwACAgIAAxkBAAJBs2fHQ7_pIjU2CCskTjOgzqk4kyfKAAJ7bwAC2hT4SWiRnt19hlFsNgQ",
#             title="Maqtov yorlig'i" 
#         )
#     ] 
 
#     await inline_query.answer(results=results)

#     ""AwACAgQAAxkBAAJBt2fHRFCvod73lJoXguI9M8N37kbNAAJrAgACdQeNUDOBtWMa7so7NgQ",
#     "AwACAgQAAxkBAAJBuGfHRFBRDHL56qGfmYQ2jq_yNMF2AAJxAgACRgABlVCRAAHqgXDkozQ2BA"

# -----------------------------------------------------------------------


@dp.inline_query()
async def inline_voice_search(inline_query: InlineQuery):
    title = inline_query.query
    print("title", title)

    audiolar = db.search_voices_title(title)  

    results = [
        InlineQueryResultCachedVoice(
            id=f"{audio[0]}",         # `id`
            voice_file_id=audio[2],   # `voice_file_id`
            title=audio[1]            # `name`
        ) for audio in audiolar[:5]
    ]
    await inline_query.answer(results=results)
