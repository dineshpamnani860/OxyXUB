# OxyXUB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyXUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyXUB/blob/main/LICENSE/>.


from telethon.errors import ChatSendInlineForbiddenError

from . import *

REPOMSG = (
    "• **OXYX USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/OxyNotOp/OxyXUB)\n",
    "• Support - @OxyXsupport",
)


@OxyXUB_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await OxyXUB_bot.inline_query(Var.BOT_USERNAME, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == OxyXUB_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError:
        await eor(e, REPOMSG)
