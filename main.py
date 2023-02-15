
import uvicorn
from fastapi import FastAPI, BackgroundTasks 

from utils.utils import available_devices, start_wda_service

app = FastAPI()


@app.get("/")
async def root():
    return {"available_devices": available_devices()}


@app.post("/start/")
async def startDevice(udid: str, port: int,background_task: BackgroundTasks):
    background_task.add_task(start_wda_service, udid,port)
    return {"message" : "staring wdaservice in background" }


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)