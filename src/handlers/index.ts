/**
* OxyX-UB - UserBot
* Copyright (C) 2020 OxyNotOp
*
* This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.
**/

import { bot } from '../bot';

import { playHandler } from './play';
import { queueHandler } from './queue';
import { pauseCBHandler } from './pause-resume';
import { skipCBHandler, skipCommand } from './skip';
import { songHandler } from './current';

export const initHandlers = (): void => {
    bot.use(playHandler);
    bot.use(queueHandler);
    bot.use(pauseCBHandler);
    bot.use(skipCBHandler);
    bot.use(skipCommand);
    bot.use(songHandler);
};