# OxyX - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

from pyOxyX-UB import *
from pyOxyX-UB.dB.database import Var
from pyOxyX-UB.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = OxyX-UB_bot.me.first_name
OWNER_ID = OxyX-UB_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
