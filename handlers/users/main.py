from aiogram.types import InlineQuery, InlineQueryResultCachedVoice, InlineQueryResultArticle, InputTextMessageContent
import wikipedia as wiki  
from loader import dp, db

from aiogram.types import InlineQuery, InlineQueryResultCachedVoice
from loader import dp, db

@dp.inline_query()
async def inline_voice_search(inline_query: InlineQuery):
    title = inline_query.query.strip()

    if not title:
        return  # Agar foydalanuvchi hech narsa yozmasa, hech narsa qaytarmaymiz.

    voices = await db.search_voices_title(title)

    results = [
        InlineQueryResultCachedVoice(
            id=str(voice[0]),  # id ustuni (avvalgi `voice[0]`)
            voice_file_id=voice[2],  # To‘g‘ri indekslangan `voice_file_id`
            title=voice[1]  # `name` maydoni
        ) for voice in voices[:10]
    ]

    await inline_query.answer(results=results, cache_time=1)



# @dp.inline_query()
# async def maqola(inline_query:InlineQuery):
#     results = [
#         InlineQueryResultArticle(
#             id="1",
#             title="Navoiy",
#             input_message_content=InputTextMessageContent(message_text="https://en.wikipedia.org/wiki/Navoiy"),
#             description="Navoiy go'zal shaxar",
#             thumbnail_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Rabati_Malik%2C_Navoiy%2C_Uzbekistan.jpg/375px-Rabati_Malik%2C_Navoiy%2C_Uzbekistan.jpg"
#         )
#     ]
#     await inline_query.answer(results=results)

