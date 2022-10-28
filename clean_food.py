import asyncio
import time
import logging

class CompletedTaskError(Exception):
    pass
class RequiredTaskError(Exception):
    pass
class ChepOcupedError(Exception):
    pass
class Food:
    def __init__(self, minute:float=1.0):
        self._minute=minute
        self._start_time=time.time()
        self._end_time=None
        self._chef_is_available=False
        self._tasks={
            "cut_all_ingredients":{
                "name": "cut_all_ingredients",
                "time":2,
                "occupies_chef":True,
                "requires":[],
                "completed":False
            },
            "_wait_eggplant_in_the_salty_water": {
                "name": "_wait_eggplant_in_the_salty_water",
                "time": 2,
                "occupies_chef": False,
                "requires": ["cut_all_ingredients"],
                "completed": False
            },
            "_frying_onion": {
                "name": "_frying_onion",
                "time": 2,
                "occupies_chef": True,
                "requires": ["cut_all_ingredients"],
                "completed": False
            },
            "_add_pepper_to_fryingonion": {
                "name": "_add_pepper_to_fryingonion",
                "time": 2,
                "occupies_chef": True,
                "requires": [],
                "completed": False
            },
            "_add_tomato_sauce_spice_mince": {
                "name": "_add_tomato_sauce_spice_mince",
                "time": 2,
                "occupies_chef": True,
                "requires": ["_frying_onion"],
                "completed": False
            },
            "_add_tomatoes": {
                "name": "_add_tomatoes",
                "time": 2,
                "occupies_chef": True,
                "requires": ["_add_tomato_sauce_spice_mince"],
                "completed": False
            },
            "_frying_eggplant": {
                "name": "_frying_eggplant",
                "time": 2,
                "occupies_chef": True,
                "requires": ["_wait_eggplant_in_the_salty_water"],
                "completed": False
            },
            "_mix_eggplant_and_mincesauce": {
                "name": "_mix_eggplant_and_mincesauce",
                "time": 2,
                "occupies_chef": True,
                "requires": [],
                "completed": False
            },
            "_service_ready": {
                "name": "_service_ready",
                "time": 2,
                "occupies_chef": True,
                "requires": [],
                "completed": False
            },
        }

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
            if self._tasks["_service_ready"]["completed"]:
                logging.error("patlıcan musakka hazır değil")
            logging.info(f"it took {((self._end_Time - self._start_time) / self._minute):.2f}"
                         f"  minutes to complete ths recipe")
            return True
    async def __call__(self,task:str)->None:
        try:
            if self._tasks[task]["completed"]:
                raise CompletedTaskError

            if self._tasks[task]["occupies_chef"]:
                if not self._chef_is_available:
                    raise ChepOcupedError
                self._chef_is_available = False
            logging.info(f"[START] {task}")
            await asyncio.sleep(self._tasks[task]["time"] * self._minute)
            self._tasks[task]["completed"] = True
            logging.info(f"[END] {task}")
        except CompletedTaskError:
            logging.warning(f"Task {task} is already completed")
            await asyncio.sleep(0)
            return None
        except RequiredTaskError:
            logging.warning(f"Task {task} is not ready to be completed")
            await asyncio.sleep(0)
            return None
        except ChepOcupedError:
            logging.warning(f"The chef is not available for {task}")
            await asyncio.sleep(0)
            return None
        finally:
            if self._tasks[task]["occupies_chef"]:
                self._chef_is_available = True
            return None
async  def main() ->None:
    async with Food(0.1) as food:
        tasks=[
            ["cut_all_ingredients"],
            ["_wait_eggplant_in_the_salty_water"],
            ["_frying_onion"],
            ["_add_pepper_to_fryingonion"],
            ["_add_tomato_sauce_spice_mince"],
            ["_add_tomatoes"],
            ["_mix_eggplant_and_mincesauce"],
            ["_frying_eggplant" ],
            ["_service_ready"]

        ]
        for task in tasks:
            await asyncio.gather(*[food(t) for t in tasks])
    return None
if __name__=='__main__':
    asyncio.run(main())
