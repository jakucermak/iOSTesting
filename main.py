import time
from typing import Union

from fastapi import FastAPI, Path, Query, Response, status, Request

from utils.utils import start_client, read_ip_from_log

app = FastAPI()

clients_processes = {}
clients_ip = {}


@app.get("/")
async def root(request: Request):
    print(request.client.host)
    return {"message": "server is running"}

@app.post("/start/{name}")
async def start(response: Response,
                name: str = Path(title="Name of iphone to start debugging on"),
                q: Union[str, None] = Query(default=None, alias="item-query"),
                ):
    clients_processes[name] = start_client(name)
    time.sleep(30)
    try:
        clients_ip[name] = read_ip_from_log(name)
        return {"message": name, "device_ip": clients_ip[name]}
    except:
        clients_processes[name].kill()
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"Service could not start"}


@app.post("/stop/{name}")
async def stop(name: str = Path(title="Name of iPhone to stop debugging on"),
               q: Union[str, None] = Query(default=None, alias="item-query"), ):
    clients_processes[name].kill()
    clients_processes.pop(name)
    if not name in clients_processes:
        return {"message": "successfully terminated testing service"}
