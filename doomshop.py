from telethon.types import Message
import asyncio
from urllib.request import urlopen
from datetime import datetime
from random import seed, randint
from .. import loader, utils
from os import system

running = False
lines = []
cooldown = .5

@loader.tds
class doomshop(loader.Module):
    """DOOMSHOP trolling by @lonecoreshit"""
    strings = { "name": "DOOMSHOP" }

    @loader.command(en_doc="<target_username/this> - start bot")
    async def doomkill(self, message: Message):
        """<target_username/this> - start bot"""
        global running
        global cooldown
        global lines
        # try loading lines from db
        try:
            with open("doom.txt") as file:
                lines = [line.rstrip() for line in file]
        except:
            await utils.answer(message, f"шаблоны не загружены! {self.get_prefix()}doomload <link>")
            return

        if len(message.message.split(" ")) < 2:
            await utils.answer(message, f"цель не указана!")
            return
        
        await message.delete()
        seed(datetime.now())

        running = True
        self.set("r", running)
        self.set("c", cooldown)

        while self.get("r"):
            await message.client.send_message(message.to_id, f"{message.message.split(' ')[1] if message.message.split(' ')[1].startswith('@') else ''} {lines[randint(0, len(lines)-1)]}")
            await asyncio.sleep(self.get("c"))

    @loader.command(en_doc="- stop bot")
    async def doomstop(self, message: Message):
        """- stop bot"""
        global running

        running = False

        self.set("r", running)

        await message.delete()

    @loader.command(en_doc="<number> - set cooldown between messsages")
    async def doomcd(self, message: Message):
        """<number> - set cooldown between messsages"""
        global cooldown

        if len(message.message.split(" ")) < 2:
            await utils.answer(message, f"нужно указать кулдаун!")
            return
        
        cooldown = float(message.message.split(" ")[1])
        await utils.answer(message, f"установлен кулдаун {cooldown}сек")
    
    @loader.command(en_doc="<link to raw text> - load")
    async def doomload(self, message: Message):
        """<link to raw text> - load"""
        global lines

        if len(message.message.split(" ")) < 2:
            await utils.answer(message, f"нужно указать ссылку!")
            return

        with open(r'doom.txt', 'w') as file:
            file.write(urlopen(message.message.split(" ")[1]).read().decode('utf-8'))
            await utils.answer(message, f"шаблоны успешно загружены!")