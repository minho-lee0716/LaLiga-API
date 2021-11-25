from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from datetime import datetime, date
import time
from threading import Thread
import os
import sys

import uvicorn

###############
app = FastAPI()
###############

class SendTimeTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            print(datetime.now().time())
            time.sleep(1)

s = SendTimeTask()
t = Thread(target=s.run, daemon=True)

@app.get('/start')
async def start():
    t.start()
    return {'message': "operation started..."}

@app.get('/middle')
async def middle():
    print('waiting...')
    time.sleep(5)
    print('done waiting!')

    return {'message': "still executing operation..."}

@app.get('/end')
async def end():
    s.terminate()
    t.join()
    return {'message': "operation terminated..."}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
