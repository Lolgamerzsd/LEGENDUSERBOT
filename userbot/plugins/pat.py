"""
HeadPat Module for Userbot (http://headp.at)
cmd:- .pat username or reply to msg
By:- git: jaskaranSM tg: @Zero_cool7870
"""

from os import remove
from random import choice
from urllib import parse

import requests

from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

BASE_URL = "https://headp.at/pats/{}"
PAT_IMAGE = "pat.jpg"


@bot.on(admin_cmd(pattern="pat ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="pat ?(.*)", allow_sudo=True))
async def lastfm(event):
    if event.fwd_from:
        return
    username = event.pattern_match.group(1)
    if not username and not event.reply_to_msg_id:
        await edit_or_reply(event, "`Reply to a message or provide username`")
        return

    resp = requests.get("http://headp.at/js/pats.json")
    pats = resp.json()
    pat = BASE_URL.format(parse.quote(choice(pats)))
    await event.delete()
    with open(PAT_IMAGE, "wb") as f:
        f.write(requests.get(pat).content)
    if username:
        await borg.send_file(event.chat_id, PAT_IMAGE, caption=username)
    else:
        await borg.send_file(event.chat_id, PAT_IMAGE, reply_to=event.reply_to_msg_id)
    remove(PAT_IMAGE)


CmdHelp("pat").add_command("pat", "<reply>", "Gives the replied user a pat").add()
