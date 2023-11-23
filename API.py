import validators
from fastapi import APIRouter
from model2 import *

apps = APIRouter(prefix="/get-objects-by-image")


@apps.get("")
async def get_image(url):
    if validators.url(url) is True:
        res = prediction(url)

        return res
    else:
        return {"url": "This is not url"}
