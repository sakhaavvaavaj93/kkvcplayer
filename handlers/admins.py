from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
import kkmusic
from cache.admins import set
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command(["pause","ps"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("ഒന്ന് കളഞ്ഞിട്ട് പോടെയ്")


@Client.on_message(
    filters.command(["resume","rsm"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("resumed.")


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    try:
        kkmusic.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("ഞാൻ കളി നിർത്തി.ഈ കളിക്ക് ഞാൻ ഇല്ല.")


@Client.on_message(
    filters.command(["skip", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    chat_id = message.chat.id

    kkmusic.task_done(chat_id)

    if kkmusic.is_empty(chat_id):
        tgcalls.pytgcalls.leave_group_call(chat_id)
    else:
        tgcalls.pytgcalls.change_stream(
            chat_id, kkmusic.get(chat_id)["file_path"]
        )

    await message.reply_text("ചെല്ലം ചാടി നടക്കണ പുൽ ചാടി.")


@Client.on_message(
    filters.command("admincache")
)
@errors
@admins_only
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("bot restarted")
