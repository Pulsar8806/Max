from pyrogram import Client, filters, types
from base.bot_base import bot_client as bot
from base.player import player


@Client.on_message(filters.command("pause"))
async def pause(_, message: types.Message):
    chat_id = message.chat.id
    await player.change_streaming_status("pause", chat_id)
    return await bot.send_message(
        message,
        "track_paused",
        reply_message=True
    )


@Client.on_message(filters.command("resume"))
async def resume_(_, message: types.Message):
    chat_id = message.chat.id
    await player.change_streaming_status("resume", chat_id)
    return await bot.send_message(
        message,
        "track_resumed",
        reply_message=True
    )


@Client.on_message(filters.command("skip"))
async def skip_(_, message: types.Message):
    chat_id = message.chat.id
    toxt = await player.change_stream(chat_id)
    return await bot.send_message(
        message,
        toxt,
        reply_message=True
    )


@Client.on_message(filters.command("vol"))
async def change_vol_(_, message: types.Message):
    chat_id = message.chat.id
    vol = int(message.command[1])
    await player.change_vol(chat_id, vol)
    await bot.send_message(
        message,
        "vol_changed",
        str(vol),
        True
    )


@Client.on_message(filters.command("end"))
async def end_stream_(_, message: types.Message):
    chat_id = message.chat.id
    await player.end_stream(chat_id)
    await bot.send_message(
        message,
        "track_ended",
        reply_message=True
    )