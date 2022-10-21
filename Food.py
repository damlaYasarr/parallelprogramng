import logging
import time
import asyncio

class Food:
    def __init__(self, minute: float = 1.0):
        self._minute = minute
        self._start_time = time.time()
        self._end_Time = None
        self._chef_is_busy = False
        self._cut_all_ingredients = False
        self._wait_eggplant_in_the_salty_water = False
        self._frying_onion = False
        self._add_pepper_to_fryingonion = False
        self._add_tomato_sauce_spice_mince = False
        self._add_tomatoes = False
        self._frying_eggplant = False
        self._mix_eggplant_and_mincesauce = False
        self._service_ready = False

    async def __aenter__(self):
        logging.basicConfig(format='%(levelname)s @ %(asctime)s : %(message)s',
                            datefmt='%d.%m.%Y %H:%M:%S',
                            level=logging.INFO,
                            force=True,
                            handlers=[
                                logging.FileHandler("eggplantmusakka.log", mode='w'),
                                logging.StreamHandler()
                            ])
        logging.getLogger("asyncio").setLevel(logging.WARNING)
        logging.info("[START] patlıcan musakka")
        await asyncio.sleep(0)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._end_Time = time.time()
        await asyncio.sleep(0)
        logging.info("[END] patlıcan musakka")
        if self._service_ready:
            logging.error("patlıcan musakka hazır değil")
        logging.info(f"it took {((self._end_Time - self._start_time) / self._minute):.2f})"
                     f"minutes to complete ths reicipe")
        return True

    async def cuttheingredients(self) -> None:
        '''
         cut the onions, pepper, tometoes
         time:5 minute
        '''
        if self._chef_is_busy:
            logging.error("the chef is busy")
            return None
        self._chef_is_busy = True
        await asyncio.sleep(5 * self._minute)
        logging.info("[END] cut the ingredients")
        self._chef_is_busy = False
        self._cut_all_ingredients = True
        return None

    async def eggplantwaitinthesaltywater(self) -> None:
        '''
        eggplants wait in the salty water
        time: 10 minute
        no need to chef
        '''
        logging.info("[START] patlıcanlar acısını saldu mi?")
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] patlıcanlar acısuni saldi")
        self._wait_eggplant_in_the_salty_water = True
        return None

    async def fryngonions(self) -> None:
        '''
        soğan kızartılır
        chef yes
        time : 3 minute
        '''
        if self._chef_is_busy:
            logging.error('chef is bussy')
            return None
        if not self._cut_all_ingredients:
            logging.error('malzemeler doğranmamışşş')
            return None
        self._chef_is_busy = True
        logging.info('[START] soğanlar kızgın yağa atılır')
        await asyncio.sleep(3 * self._minute)
        logging.info("[END] soğan pembeleştiiiii")
        self._chef_is_busy = False
        self._frying_onion = True
        return None

    async def adddpepper(self) -> None:
        '''
        pembeleşen soğanın üstüne biber atılır
        3 dk daha kavrulur
        time: 3 minute
        chef yes
        '''
        if self._chef_is_busy:
            logging.error('chef is bussy')
            return None
        if not self._cut_all_ingredients:
            logging.error('malzemeler doğranmamışşş')
            return None
        self._chef_is_busy = True
        logging.info('[START] sağonın üstüne biber atılır')
        await asyncio.sleep(3 * self._minute)
        logging.info("[END] soğan ve biberler tam kıvaında")
        self._chef_is_busy = False
        self._add_pepper_to_fryingonion = True
        return None

    async def mixmincespicytomatosauce(self) -> None:
        '''
        kıyma baharat salça sos sarımsak eklenir
        time : 10 minute
        chef yes
        '''
        if self._chef_is_busy:
            logging.error('chef is bussy')
            return None
        if not self._cut_all_ingredients:
            logging.error('malzemeler doğranmamışşş')
            return None
        self._chef_is_busy = True
        logging.info('[START] kıyma baharat salça sos sarımsak kızaran biber ve soğanın üstüne atılır')
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] kıymalı sos hazır")
        self._chef_is_busy = False
        self._add_tomato_sauce_spice_mince = True
        return None

    async def addtomatoessliceintosouce(self) -> None:
        '''
         kıymalı sosa tomates eklenir
        time : 5 minute
        chef yes
        '''
        if self._chef_is_busy:
            logging.error('chef is bussy')
            return None
        if not self._cut_all_ingredients:
            logging.error('malzemeler doğranmamışşş')
            return None
        self._chef_is_busy = True
        logging.info('[START] kıyma baharat salça sos sarımsak kızaran biber ve soğanın üstüne atılır')
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] kıymalı sos hazır")
        self._chef_is_busy = False
        self._add_tomatoes = True
        return None

    async def eggplantFrying(self) -> None:
        '''
        patlıcanlar ayrı tavada kızartılır
        time : 10 minute
        chef yes
        '''
        if self._chef_is_busy:
            logging.error('chef is bussy')
            return None
        if not self._cut_all_ingredients:
            logging.error('malzemeler doğranmamışşş')
            return None
        if not self._wait_eggplant_in_the_salty_water:
            logging.error('patlıcanlar acısını salmamışşşşş')
            return None
        self._chef_is_busy = True
        logging.info('[START] patlıcanlar kısgın yağa atılır')
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] patlıcanlar jazır")
        self._chef_is_busy = False
        self._frying_eggplant = True
        return None

    async def mixfriedeggplantandmincesauce(self) -> None:
        '''
        kızarmış patlıcan ve salçalı kıymalı sosu karıştır
        chef yes
        time 10minute

        '''
        if self._chef_is_busy:
            logging.error('chef is bussy')
            return None
        self._chef_is_busy = True
        logging.info('[START] patlıcan ve kıyma sos birleştirilir 10dk daha pişir')
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] patlıcan hazır")
        self._chef_is_busy = False
        self._mix_eggplant_and_mincesauce = True
        return None

    @property
    def minute(self):
        return self._minute

async def main_run() -> None:
        async with Food(0.1) as eggplant:
            await eggplant.cuttheingredients()
            await eggplant.eggplantwaitinthesaltywater()
            await eggplant.fryngonions()
            await eggplant.adddpepper()
            await eggplant.mixmincespicytomatosauce()
            await eggplant.addtomatoessliceintosouce()
            await eggplant.eggplantFrying()
            await eggplant.mixfriedeggplantandmincesauce()
        return None

async def main_wait_for() -> None:
        async with Food(0.1) as eggplant:
            await asyncio.wait_for(eggplant.cuttheingredients(), None)
            await asyncio.wait_for(eggplant.eggplantwaitinthesaltywater(), None)
            await asyncio.wait_for(eggplant.fryngonions(), None)
            await asyncio.wait_for(eggplant.adddpepper(), None)
            await asyncio.wait_for(eggplant.mixmincespicytomatosauce(), None)
            await asyncio.wait_for(eggplant.addtomatoessliceintosouce(), None)
            await asyncio.wait_for(eggplant.eggplantFrying(), None)
            await asyncio.wait_for(eggplant.mixfriedeggplantandmincesauce(), None)
        return None

async def main_gather() -> None:
        async with Food(0.1) as eggplant:
            await asyncio.gather(
                eggplant.cuttheingredients(),
                eggplant.eggplantwaitinthesaltywater(),
                eggplant.fryngonions(),
                eggplant.adddpepper(),
                eggplant.mixmincespicytomatosauce(),
                eggplant.addtomatoessliceintosouce(),
                eggplant.eggplantFrying(),
                eggplant.mixfriedeggplantandmincesauce(),
            )
        return None

async def main() -> None:
        async with Food(0.1) as eggplant:
            await eggplant.cuttheingredients()
            await eggplant.eggplantwaitinthesaltywater()
            await eggplant.fryngonions()
            await eggplant.adddpepper()
            await eggplant.mixmincespicytomatosauce()
            await eggplant.addtomatoessliceintosouce()
            await eggplant.eggplantFrying()
            await eggplant.mixfriedeggplantandmincesauce()

        return None
if __name__ == '__main__':
        asyncio.run(main())