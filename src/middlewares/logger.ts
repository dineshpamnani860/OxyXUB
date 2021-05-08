/**
* OxyXUB - UserBot
* Copyright (C) 2020 OxyNotOp
*
* This file is a part of < https://github.com/OxyNotOp/OxyXUB/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/OxyNotOp/OxyXUB/blob/main/LICENSE/>.
**/

import { Context, MiddlewareFn } from 'telegraf';
import { logger as log } from '../bot';
import escapeHtml from '@youtwitface/escape-html';

const Logger: MiddlewareFn<Context> = async (_, next) => {
    try {
        await next();
    } catch (err) {
        await log(`<b>Error :</b>\n <code>${escapeHtml(err.toString())}</code>`, "HTML");
    }
}

export default Logger;