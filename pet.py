from .. import loader, utils
from telethon.types import Message

@loader.tds
class PetMod(loader.Module):
    """Pet Module by tilted"""
    strings = { "name": "PetMod", "hello": "Hello World!"}

    @loader.command(
        ru_doc="Привет мир!"
    )
    async def helloworld(self, message: Message):
        """Hello World"""
        await utils.answer(message, self.strings("hello"))