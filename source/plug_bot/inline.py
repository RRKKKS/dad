from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("①",callback_data="help1"),
             InlineKeyboardButton("②",callback_data="help2"),
             InlineKeyboardButton("③",callback_data="help3"),
             ],
             [
             InlineKeyboardButton("④",callback_data="help4"),
             InlineKeyboardButton("⑤",callback_data="help5"),
             InlineKeyboardButton("⑥",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("⑦",callback_data="help7"),
             InlineKeyboardButton("⑧",callback_data="help8"),
             InlineKeyboardButton("⑨",callback_data="help9"),
             InlineKeyboardButton("⑩",callback_data="help10"),
             ],
             [
             InlineKeyboardButton("✅ - قناه السورس - ✅",url="https://t.me/S_EG_P"),
             ],
             [
             InlineKeyboardButton("🔺️ - جروب المساعدة - 🔻",url="https://t.me/SORS0Coo"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "• ⟣=====⧼[ᥴ.ᖇ ᥉᥆υᖇᥴᥱ](https://t.me/S_EG_P)⧽=====⟢\n• ① اوامر الخاص\n• ② اوامر القنوات والمجموعات \n• ③ اوامر اليوتيوب \n• ④ اوامر الاذاعه\n• ⑤ اوامر الرفع \n• ⑥ اوامر النسب\n• ⑦ اوامر اضافية \n• ⑧ اوامر تسلية1 \n ⑨ اوامر تسلية2 \n⑩ اوامر الزخرفة \n• ⟣=====⧼ [ᥴ.ᖇ ᥉᥆υᖇᥴᥱ](https://t.me/S_EG_P)⧽=====⟢"
                ),
                url="https://t.me/S_EG_P",
                description="ςŕ • SOURCE",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
