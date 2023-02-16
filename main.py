import uvicorn
from fastapi import FastAPI, BackgroundTasks

from utils.utils import available_devices, start_wda_service

from client import IOSCLient
app = FastAPI()

devices = []
clients = {}


@app.get("/")
async def root():
    global devices
    devices = available_devices()
    return {"available_devices": devices}


@app.post("/start/")
async def start_device(udid: str, port: int, background_task: BackgroundTasks):
    background_task.add_task(start_wda_service, udid, port)

    return {"message": "starting wda service in background"}


@app.post("/start/client/")
async def start_client(udid: str, port: int):
    client = IOSCLient(port)

    clients[udid] = client
    print(clients)
    return clients[port].client.status()


@app.post("/client/")
async def client_script(port: int, background_task: BackgroundTasks):

    background_task.add_task(clients[udid].script)
    return "script is running..."


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
