/**
* OxyX-UB - UserBot
* Copyright (C) 2020 OxyNotOp
*
* This file is a part of < https://github.com/OxyNotOp/OxyX-UB/ >
* PLease read the GNU Affero General Public License in
* <https://www.github.com/OxyNotOp/OxyX-UB/blob/main/LICENSE/>.
**/

import { Context, MiddlewareFn } from 'telegraf';
import client from '../redis';
import { promisify } from 'util';

const getAsync = promisify(client.get).bind(client);

const Auth: MiddlewareFn<Context> = async (ctx, next) => {
    let sudos: string | string[] | null;
    let vc_sudos: string | string[] | null;

    sudos = await getAsync('SUDOS');
    vc_sudos = await getAsync('VC_SUDOS');

    if (sudos && (typeof (sudos) === 'string')) {
        sudos = sudos.split(" ");
        if (vc_sudos && (typeof (vc_sudos) === 'string')) {
            sudos = sudos.concat(vc_sudos.split(" "))
        }
    }

    let owner = await getAsync('OWNER_ID');
    let id = ctx.from?.id.toString();

    if ((id && sudos && (typeof (sudos) === 'object') && sudos.includes(id)) || (id === owner)) {
        return next();
    } else {
        if (ctx.callbackQuery) {
            return ctx.answerCbQuery("You aren't authorized ...", {
                show_alert: true
            })
        } else {
            return;
        }
    }
}

export default Auth;
