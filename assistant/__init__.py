# OxyX - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyXUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyXUB/blob/main/LICENSE/>.

from pyUltroid import *
from pyUltroid.dB.database import Var
from pyUltroid.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = OxyXUB_bot.me.first_name
OWNER_ID = OxyXUB_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
