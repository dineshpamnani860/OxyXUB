/**
* OxyXUB - UserBot
* Copyright (C) 2020 OxyNotOp
*
* This file is a part of < https://github.com/OxyNotOp/OxyXUB/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/OxyNotOp/OxyXUB/blob/main/LICENSE/>.
**/

import { Telegraf } from 'telegraf';
import env from './env';

export const bot = new Telegraf(env.BOT_TOKEN);
export const logger = async (msg: string, parse: 'HTML' | 'Markdown' | 'MarkdownV2' = 'HTML') => await bot.telegram.sendMessage(env.LOG_CHANNEL, msg, { parse_mode: parse });
