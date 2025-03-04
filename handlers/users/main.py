from loader import dp
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

# @dp.inline_query()
# async def inline_query(query: InlineQuery):
#     text = query.query  # Foydalanuvchi yozgan so'z
    
#     # Agar foydalanuvchi hech narsa yozmasa, natija berilmaydi
#     if not text:
#         return
    
#     results = [
#         InlineQueryResultArticle(
#             id="1",
#             title="Salom!",
#             input_message_content=InputTextMessageContent(message_text="Assalomu alaykum!"),
#         ),
#         InlineQueryResultArticle(
#             id="2",
#             title="Qanday?",
#             input_message_content=InputTextMessageContent(message_text="Qandaysiz?"),
#         ),
#         InlineQueryResultArticle(
#             id="3",
#             title="Rahmat",
#             input_message_content=InputTextMessageContent(message_text="Rahmat!"),
#         ),
#     ]

#     await query.answer(results, cache_time=1)  # 1 soniya cache qilish
