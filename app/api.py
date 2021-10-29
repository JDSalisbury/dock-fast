from app.middlewares.analytics import LogRequests
from fastapi import FastAPI
import logging


app = FastAPI()

app.add_middleware(LogRequests)


logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.INFO)

# setup loggers
# logging.config.fileConfig(
#     'logging.conf', disable_existing_loggers=False, defaults='echi_export.log')

# get root logger
# the __name__ resolve to "main" since we are at the root of the project.
logger = logging.getLogger(__name__)
# This will get the root logger since no logger in the configuration has this name.


class Truck():

    def __init__(self, color: str, wheels: int) -> None:
        self.color = color
        self.wheels = wheels

    def get_details(self) -> str:
        return f'A {self.color} {self.wheels} wheeler'


@app.get("/", tags=["root"])
async def read_root() -> dict:

    details = {
        'color': 'blue',
        'wheels': 18
    }

    carl = Truck(**details)
    return {"message": f"Welcome to your blog!. {carl.get_details()}"}
