from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
           
        ),
        InlineKeyboardButton(
            text="OWNER",
            url=f"t.me/bitexalt",
        ),
        InlineKeyboardButton(
            text="𝙽𝚎𝚡𝚝 ➥", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Auth",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="Block",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Broadcast",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="Userban",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Lyrics",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Song Playlist",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="Voice Chat",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="Play",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="Co Admin",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Start",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="𝙽𝚎𝚡𝚝 ➥", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="【𝙷𝚎𝚕𝚙】",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
