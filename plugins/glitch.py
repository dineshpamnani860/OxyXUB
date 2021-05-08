# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

"""

✘ Commands Available -

•`{i}glitch <replt to media>`
    gives a glitchy gif.

"""

import os

from . import *


@OxyX-UB_cmd(pattern="glitch$")
async def _(e):
    reply = await e.get_reply_message()
    if not (reply and reply.media):
        return await eor(e, "Reply to any media")
    wut = mediainfo(reply.media)
    if not wut.startswith(("pic", "sticker")):
        return await eor(e, "`Unsupported Media`")
    xx = await eor(e, "`Gliching...`")
    ok = await bot.download_media(reply.media)
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{ok}' ult.gif"
    stdout, stderr = await bash(cmd)
    await OxyX-UB_bot.send_file(
        e.chat_id, "ult.gif", force_document=False, reply_to=reply
    )
    await xx.delete()
    os.remove(ok)
    os.remove("ult.gif")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
