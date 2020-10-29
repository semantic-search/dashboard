from fastapi import FastAPI, Depends, Form, WebSocket, \
    WebSocketDisconnect, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from yaml_utils import update_state
import globals
from db_models.models.cache_model import Cache
import uuid
import os


app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

active_connections = []


def get_ws_clients():
    return active_connections


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(client_id: int, websocket: WebSocket, clients=Depends(get_ws_clients)):
    await websocket.accept()
    connected_client = {
        "id": client_id,
        "websocket": websocket
    }
    await websocket.send_text(
        json.dumps(globals.final_dict)
    )
    clients.append(connected_client)
    try:
        while True:
            _ = await websocket.receive_text()

    except WebSocketDisconnect:
        for dic in active_connections:
            dic["websocket"] = websocket
            active_connections.remove(dic)
            break


@app.post("/update_state/")
async def notify(
        parent_name: str = Form(...),
        group_name: str = Form(...),
        container_name: str = Form(...),
        file_name: str = Form(...),
        client_id: int = Form(...),
        clients=Depends(get_ws_clients)
):
    update_state(
        parent=parent_name,
        container=container_name,
        file=file_name,
        group=group_name
    )
    for dic in clients:
        if dic["id"] == client_id:
            ws = dic["websocket"]
            await ws.send_text(
                json.dumps(globals.final_dict)
            )
            break
    return True


@app.post("/update_last_file/")
async def update(
        last_file: str = Form(...),
        value: str = Form(...),
):
    if last_file == "last_doc_image":
        for cont in globals.image_containers:
            globals.container_dict[cont].append(value)
    elif last_file == "last_audio_file":
        for cont in globals.audio_container:
            globals.container_dict[cont].append(value)
    return True


@app.post("/remove_file/")
async def update(last_file: str = Form(...),
                 value: str = Form(...),
                 client_id: int = Form(...),
                 clients=Depends(get_ws_clients)
                 ):
    if last_file == "last_doc_image":
        for group in globals.image_groups_all:
            for container in globals.image_containers:
                update_state(
                    parent="Image",
                    group=group,
                    container=container,
                    file=value,
                    remove=True
                )


    elif last_file == "last_audio_file":
        for group in globals.audio_groups_all:
            for container in globals.audio_container:
                update_state(
                    parent="Image",
                    group=group,
                    container=container,
                    file=value,
                    remove=True
                )

    for dic in clients:
        if dic["id"] == client_id:
            ws = dic["websocket"]
            await ws.send_text(
                json.dumps(globals.final_dict)
            )
            break
    return True


@app.get("/all_cont_files/")
async def all_containers():
    return globals.container_dict


def remove_file(file):
    """Fast API Background task"""
    os.remove(file)


@app.get("/download/{file_id}")
def download(file_id: str, background_tasks: BackgroundTasks):
    cache_obj = Cache.objects.get(id=file_id)
    extension = cache_obj.mime_type
    new_file_to_download = str(uuid.uuid4()) + "." + extension
    with open(new_file_to_download, 'wb') as f:
        f.write(cache_obj.file.read())
    background_tasks.add_task(remove_file, new_file_to_download)
    return FileResponse(new_file_to_download)
