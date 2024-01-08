from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5405dd39ceed4ed24bba6.jpg",
        caption=f"""🍁CLICK BELOW BUTTON TO DM LEVI ACKERMAN🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Levi Ackerman", url=f"https://t.me/LeviAckerman1709")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5405dd39ceed4ed24bba6.jpg",
        caption=f"""🍁CLICK BELOW BUTTON TO DM LEVI ACKERMAN🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Levi Ackerman ", url=f"https://t.me/LeviAckerman1709")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5405dd39ceed4ed24bba6.jpg",
        caption=f"""𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐑𝐄𝐏𝐎""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source", url=f"https://telegra.ph/file/cc5de64fd247a28f71d30.mp4")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5405dd39ceed4ed24bba6.jpg",
        caption=f"""𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐑𝐄𝐏𝐎""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source", url=f"https://telegra.ph/file/cc5de64fd247a28f71d30.mp4")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c45ae897746dee0491236.jpg",
        caption=f"""𝐂𝐋𝐈𝐂𝐊 𝐁𝐄𝐋𝐎𝐖 𝐁𝐔𝐓𝐓𝐎𝐍 𝐓𝐎 𝐆𝐄𝐓 𝐑𝐄𝐏𝐎""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source", url=f"https://telegra.ph/file/cc5de64fd247a28f71d30.mp4")
                ]
            ]
        ),
              )
