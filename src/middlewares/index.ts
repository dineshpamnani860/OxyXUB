/**
* OxyX-UB - UserBot
* Copyright (C) 2020 OxyNotOp
*
* This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.
**/

import { bot } from '../bot';

import Auth from './auth';
import Logger from './logger';

export const initMiddleWares = (): void => {
    bot.use(Logger);
    bot.use(Auth);
}