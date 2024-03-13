from .. import loader, utils
from telethon.types import Message

@loader.tds
class PetMod(loader.Module):
    """Pet Module by tilted for моя любимая ритачян"""
    strings = { "name": "PetMod", "newpet": "создаю нового пета...", "petname": self.get("petname", False)}

    @loader.command(ru_doc="создает нового случайного питомца")
    async def newpet(self, message: Message):
        """Hello World"""
        await utils.answer(message, self.strings("newpet"))
        self.set("petname", message.message)