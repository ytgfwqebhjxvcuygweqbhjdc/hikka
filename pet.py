from .. import loader, utils
from telethon.types import Message
import random

@loader.tds
class PetMod(loader.Module):
    """Pet Module by tilted for моя любимая ритачян"""
    strings = { "name": "PetMod", "newpet": "создаю нового пета..."}


    @loader.command(ru_doc="<имя> - создает нового пиздюка (это удалит предыдущего пета)")
    async def newpet(self, message: Message):
        """Hello World"""
        self._pets = self.pointer("pets", [])
        try:
            await utils.answer(message, "создаю " + message.message.split(" ")[1] + "...")
        except IndexError:
            await utils.answer(message, "нужно указать имя!")
            return 1
        
        self.set("petname", message.message.split(" ")[1])
        self.set("petexp", 0)
        self.set("petlvl", 1)
        self.set("pethunger", 0)
        self.set("petthirst", 0)
        self.set("petenergy", 0)

        self.set("invfood", 0)
        self.set("invwater", 0)
        self.set("invexppotion", 0)

        random.seed(self.get("petname"))

        await utils.answer(message, self.get("petname") + " создан!")

    @loader.command(ru_doc="<количество> напоить пета, использует 🥤")
    async def petdrink(self, message: Message):
        if self.get("petthirst") < 100:
            if len(message.message.split(" ")) < 2:
                self.set("petthirst", self.get("petthirst")+1)
                await utils.answer(message, f"пет напоен! -1🥤")
            else:
                if not message.message.split(" ")[1].isnumeric():
                    await utils.answer(message, f"не")
                    return
                self.set("pethunger", self.get("petthirst")+int(message.message.split(' ')[1]))
                await utils.answer(message, f"пет напоен! -{message.message.split(' ')[1]}🥤")
        else:
            await utils.answer(message, f"""сейчас пет не хочет пить""")

        if self.get("petthirst") > 100:
            self.set("petthirst", 100)

    @loader.command(ru_doc="<количество> порокмить пета, использует 🍗")
    async def petfeed(self, message: Message):
        if self.get("pethunger") < 100:
            if len(message.message.split(" ")) < 2:
                self.set("pethunger", self.get("pethunger")+1)
                await utils.answer(message, f"пет покормлен! -1🍗")
            else:
                if not message.message.split(" ")[1].isnumeric():
                    await utils.answer(message, f"не")
                    return
                self.set("pethunger", self.get("pethunger")+int(message.message.split(' ')[1]))
                await utils.answer(message, f"пет покормлен! -{message.message.split(' ')[1]}🍗")
        else:
            await utils.answer(message, f"сейчас пет не голоден")

        if self.get("pethunger") > 100:
            self.set("pethunger", 100)

    @loader.command(ru_doc="сгонять за едой")
    async def getfood(self, message: Message):
        amount = random.randint(1, 20)
        self.set("invfood", self.get("invfood")+amount)
        await utils.answer(message, f"+{amount}🍗")
        
    @loader.command(ru_doc="сгонять за водой")
    async def getwater(self, message: Message):
        amount = random.randint(1, 20)
        self.set("invwater", self.get("invwater")+amount)
        await utils.answer(message, f"+{amount}🥤")

    @loader.command(ru_doc="инвентарь")
    async def petinv(self, message: Message):
        self.set("invwater", self.get("invwater")+1)
        await utils.answer(message, f"инвентарь:\n{self.get('invfood')} 🍗\n{self.get('invwater')} 🥤\n{self.get('invexppotion')} 🧪")

    @loader.command(ru_doc="состояние ублюдка")
    async def petstatus(self, message: Message):
        await utils.answer(message, f"""🪪 имя: {self.get('petname')}\n\n🧪 опыт: {self.get('petexp')}/50\n📊 уровень: {self.get('petlvl')}\n\n⚡ энергия: {self.get('petenergy')}\n🍗 голод: {self.get('pethunger')}/100\n💧 жажда: {self.get('petthirst')}/100""")