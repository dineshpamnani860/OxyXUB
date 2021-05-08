# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}save <reply message>`
    Save that replied msg to ur saved messages box.

"""
from . import *


@OxyX-UB_cmd(pattern="save$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(
            e, "Reply to Any Message to save it to ur saved messages", time=5
        )
    await OxyX-UB_bot.send_message("me", x)
    await eod(e, "Message saved at saved messages", time=5)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
