from pyrogram import Client
from pytgcalls import PyTgCalls

import kkmusic
import config


client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client, 1512, False)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    kkmusic.task_done(chat_id)

    if kkmusic.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id, kkmusic.get(chat_id)["file_path"]

        )

run = pytgcalls.run
