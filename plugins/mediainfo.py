# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}mediainfo <reply to media>`
   To get info about it.
"""

import os

from . import *



@OxyX-UB_cmd(pattern="mediainfo$")
async def mi(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eod(e, "`Reply to any media`")
    xx = mediainfo(r.media)
    murl = r.media.stringify()
    url = make_html_telegraph("Mediainfo", "OxyX-UB", f"<code>{murl}</code>")
    ee = await eor(e, f"**[{xx}]({url})**\n\n`Loading More...`", link_preview=False)
    dl = await OxyX-UB_bot.download_media(r.media)
    out, er = await bash(f"mediainfo {dl}")
    os.remove(dl)
    if er:
        return await ee.edit(f"**[{xx}]({url})**", link_preview=False)
    await ee.edit(f"**[{xx}]({url})**\n\n{out}")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
