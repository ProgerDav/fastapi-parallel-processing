import asyncio
import time

from random import randrange
from fastapi import APIRouter


router = APIRouter(
    prefix="/sleeper",
    tags=["Sleeper"],
)


class Context:
    """
    A class to hold job active flag amoung the application context
    """

    active = True
    index = 0


@router.get("/rotate")
def rotate():
    print("REQUEST CAME IN: ", Context.index)
    Context.active = True
    Context.index += 1
    n = 0
    while Context.active:
        n = randrange(10)
    return f"Your lucky number is {n}!"


@router.get("/stop")
def stop():
    Context.active = False
    return "Wheel running job stopped. See the rotate request output now to see the lucky number."


@router.get("/sleep")
def sleep():
    print("Sleep Request Came: ", time.time())
    time.sleep(5)
    return "WAKE UP!"


@router.get("/async-sleep")
async def sleep():
    print("ASYNC Sleep Request Came: ", time.time())
    await asyncio.sleep(5)

    return "AYNC WAKE UP"
