from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> hola {message.from_user.first_name}!</b>

iam a music bot to play music in your groups voice chat.

contact creator to created my clone or for any questions""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SUPPORT", url="https://t.me/kkArmy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "group", url="https://t.me/vakamarachottil1"
                    ),
                    InlineKeyboardButton(
                        "Contact owner", url="https://t.me/vaasukionfire7966"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close"
                    )
                ]
            ]
        )
    )
