from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import av_cmd


@av_cmd(pattern='lepin(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku lepin`")
    sleep(3)
    await typew.edit("`5 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Jakarta, Salam Kenal:)`")
# Create by myself @localheart


@av_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@av_cmd(pattern='semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}lepin`\
    \n↳ : perkenalan lepin\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}semangat`\
    \n↳ : Jan Lupa Semangat."
})
