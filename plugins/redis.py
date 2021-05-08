# OxyXUB - UserBot
# Copyright (C) 2020 OxyNotOp
#
# This file is a part of < https://github.com/OxyNotOp/OxyXUB/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/OxyNotOp/OxyXUB/blob/main/LICENSE/>.

"""
✘ Commands Available -

**DataBase Commands, do not use if you don't know what it is.**

• `{i}redisusage`
    Check Storaged Data Capacity.

• `{i}setredis key | value`
    Redis Set Value.
    e.g :
    `{i}setredis hi there`
    `{i}setredis hi there | OxyXUB here`

• `{i}getredis key`
    Redis Get Value

• `{i}delredis key`
    Delete Key from Redis DB

• `{i}renredis old keyname | new keyname`
    Update Key Name

• `{i}getkeys`
    Get the list of keys stored in Redis
"""

import re

from . import *


@OxyXUB_cmd(
    pattern="setredis ?(.*)",
)
async def _(ult):
    ok = await eor(ult, "`...`")
    try:
        delim = " " if re.search("[|]", ult.pattern_match.group(1)) is None else " | "
        data = ult.pattern_match.group(1).split(delim, maxsplit=1)
        udB.set(data[0], data[1])
        redisdata = Redis(data[0])
        await ok.edit(
            "Redis Key Value Pair Updated\nKey : `{}`\nValue : `{}`".format(
                data[0],
                redisdata,
            ),
        )
    except BaseException:
        await ok.edit("`Something Went Wrong`")


@OxyXUB_cmd(
    pattern="getredis ?(.*)",
)
async def _(ult):
    ok = await eor(ult, "`Fetching data from Redis`")
    val = ult.pattern_match.group(1)
    if val == "":
        return await ult.edit(f"Please use `{hndlr}getkeys <keyname>`")
    try:
        value = Redis(val)
        await ok.edit(f"Key: `{val}`\nValue: `{value}`")
    except BaseException:
        await ok.edit("`Something Went Wrong`")


@OxyXUB_cmd(
    pattern="delredis ?(.*)",
)
async def _(ult):
    ok = await eor(ult, "`Deleting data from Redis ...`")
    try:
        key = ult.pattern_match.group(1)
        udB.delete(key)
        await ok.edit(f"`Successfully deleted key {key}`")
    except BaseException:
        await ok.edit("`Something Went Wrong`")


@OxyXUB_cmd(
    pattern="renredis ?(.*)",
)
async def _(ult):
    ok = await eor(ult, "`...`")
    delim = " " if re.search("[|]", ult.pattern_match.group(1)) is None else " | "
    data = ult.pattern_match.group(1).split(delim)
    if Redis(data[0]):
        try:
            udB.rename(data[0], data[1])
            await ok.edit(
                "Redis Key Rename Successful\nOld Key : `{}`\nNew Key : `{}`".format(
                    data[0],
                    data[1],
                ),
            )
        except BaseException:
            await ok.edit("Something went wrong ...")
    else:
        await ok.edit("Key not found")


@OxyXUB_cmd(
    pattern="getkeys$",
)
async def _(ult):
    ok = await eor(ult, "`Fetching Keys ...`")
    keys = sorted(udB.keys())
    msg = ""
    for x in keys:
        if x.isdigit() or x.startswith("-"):
            pass
        else:
            msg += f"• `{x}`" + "\n"
    await ok.edit(f"**List of Redis Keys :**\n{msg}")


@OxyXUB_cmd(
    pattern="redisusage$",
)
async def _(ult):
    ok = await eor(ult, "`Calculating ...`")
    x = 30 * 1024 * 1024
    z = 0
    for n in udB.keys():
        z += udB.memory_usage(n)
    a = humanbytes(z) + "/" + humanbytes(x)
    b = str(round(z / x * 100, 3)) + "%" + "  Used"
    await ok.edit(f"{a}\n{b}")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
