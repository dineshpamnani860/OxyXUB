# OxyX-UB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.

from datetime import datetime

from pyOxyX-UB.functions.asst_fns import *
from pyOxyX-UB.misc._decorators import sed
from telethon import Button, events
from telethon.utils import get_display_name

from plugins import *

from . import *


@asst_cmd("start")
async def assistant(event):
    if event.is_group and event.sender_id in sed:
        bnn = (await asst.get_me()).username
        return await event.reply(
            "`I dont work in groups`",
            buttons=[Button.url("⚙️Sᴛᴀʀᴛ⚙️", url=f"https://t.me/{bnn}?start=set")],
        )
    else:
        if not is_added(event.sender_id) and event.sender_id not in sed:
            add_user(event.sender_id)
        ok = ""
        if event.is_private and event.sender_id in sed:
            return
        if not udB.get("STARTMSG"):
            if udB.get("PMBOT") == "True":
                ok = "➼ You can contact my master using this bot!!\n\n➼ Send your Message, I will Deliver it To Master\n\n➼ Contact My Owner :- @FallenAngel_xD"
            await event.reply(
                f"➼ Helloww there, this is OxyX-UB Assistant of {OWNER_NAME}!\n\n{ok}",
                buttons=[Button.url("Know More", url="https://t.me/OxyXsupport")],
            )
        else:
            u = await event.client.get_entity(event.chat_id)
            me = f"[{OxyX-UB_bot.me.first_name}](tg://user?id={OxyX-UB_bot.uid})"
            mention = f"[{get_display_name(u)}](tg://user?id={u.id})"
            await event.reply(
                Redis("STARTMSG").format(me=me, mention=mention),
                buttons=[Button.url("Know More", url="https://t.me/OxyXsupport")],
            )


@asst_cmd("start ?(.*)")
@owner
async def OxyX-UB(event):
    if event.pattern_match.group(1):
        return
    if event.is_group:
        return
    name = event.sender.first_name
    if event.sender.last_name:
        name += f" {event.sender.last_name}"
    await asst.send_message(
        event.chat_id,
        get_string("ast_3").format(name),
        buttons=[
            [
                Button.inline("Language 🌐", data="lang"),
                Button.inline("Sᴇᴛᴛɪɴɢs ⚙️", data="setter"),
            ],
            [
                Button.inline("Sᴛᴀᴛs ✨", data="stat"),
                Button.inline("Bʀᴏᴀᴅᴄᴀsᴛ 📻", data="bcast"),
            ],
        ],
    )


# aah, repeat the codes..
@callback("mainmenu")
@owner
async def OxyX-UB(event):
    if event.is_group:
        return
    await event.edit(
        get_string("ast_3").format(OWNER_NAME),
        buttons=[
            [
                Button.inline("Language 🌐", data="lang"),
                Button.inline("Sᴇᴛᴛɪɴɢs ⚙️", data="setter"),
            ],
            [
                Button.inline("Sᴛᴀᴛs ✨", data="stat"),
                Button.inline("Bʀᴏᴀᴅᴄᴀsᴛ 📻", data="bcast"),
            ],
        ],
    )


@callback("stat")
@owner
async def botstat(event):
    ok = len(get_all_users())
    msg = """OxyX-UB Assistant - Stats
Total Users - {}""".format(
        ok,
    )
    await event.answer(msg, cache_time=0, alert=True)


@callback("bcast")
@owner
async def bdcast(event):
    ok = get_all_users()
    await event.edit(f"Broadcast to {len(ok)} users.")
    async with event.client.conversation(OWNER_ID) as conv:
        await conv.send_message(
            "Enter your broadcast message.\nUse /cancel to stop the broadcast.",
        )
        response = conv.wait_event(events.NewMessage(chats=OWNER_ID))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message("Cancelled!!")
        else:
            success = 0
            fail = 0
            await conv.send_message(f"Starting a broadcast to {len(ok)} users...")
            start = datetime.now()
            for i in ok:
                try:
                    await asst.send_message(int(i), f"{themssg}")
                    success += 1
                except BaseException:
                    fail += 1
            end = datetime.now()
            time_taken = (end - start).seconds
            await conv.send_message(
                f"""
Broadcast completed in {time_taken} seconds.
Total Users in Bot - {len(ok)}
Sent to {success} users.
Failed for {fail} user(s).""",
            )


@callback("setter")
@owner
async def setting(event):
    await event.edit(
        "Choose from the below options -",
        buttons=[
            [
                Button.inline("API Kᴇʏs", data="apiset"),
                Button.inline("Pᴍ Bᴏᴛ", data="chatbot"),
            ],
            [
                Button.inline("Aʟɪᴠᴇ", data="alvcstm"),
                Button.inline("PᴍPᴇʀᴍɪᴛ", data="ppmset"),
            ],
            [Button.inline("Fᴇᴀᴛᴜʀᴇs", data="otvars")],
            [Button.inline("VC Sᴏɴɢ Bᴏᴛ", data="vcb")],
            [Button.inline("« Bᴀᴄᴋ", data="mainmenu")],
        ],
    )


@asst_cmd("start set")
@owner
async def set(event):
    await event.reply(
        "Choose from the below options -",
        buttons=[
            [
                Button.inline("API Kᴇʏs", data="apiset"),
                Button.inline("Pᴍ Bᴏᴛ", data="chatbot"),
            ],
            [
                Button.inline("Aʟɪᴠᴇ", data="alvcstm"),
                Button.inline("PᴍPᴇʀᴍɪᴛ", data="ppmset"),
            ],
            [Button.inline("Fᴇᴀᴛᴜʀᴇs", data="otvars")],
            [Button.inline("VC Sᴏɴɢ Bᴏᴛ", data="vcb")],
            [Button.inline("« Bᴀᴄᴋ", data="mainmenu")],
        ],
    )