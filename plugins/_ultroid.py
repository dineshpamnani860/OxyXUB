# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.


from telethon.errors import ChatSendInlineForbiddenError

from . import *

REPOMSG = (
    "• **OXYX USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/OxyNotOp/OxyX-UB)\n",
    "• Support - @OxyXsupport",
)


@OxyX-UB_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await OxyX-UB_bot.inline_query(Var.BOT_USERNAME, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == OxyX-UB_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError:
        await eor(e, REPOMSG)
