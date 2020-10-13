from fastapi import FastAPI, Depends, Form, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json
from yaml_utils import get_dict, update_state


last_doc_image_file = str()
last_audio_file = str()

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
    config_dict = get_dict()
    await websocket.send_text(
        json.dumps(config_dict)
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
    state_dict = update_state(
        parent=parent_name,
        container=container_name,
        file=file_name,
        group=group_name,
        last_image_file=last_doc_image_file,
        last_audio_file=last_audio_file
    )
    for dic in clients:
        if dic["id"] == client_id:
            ws = dic["websocket"]
            await ws.send_text(
                   json.dumps(state_dict)
                )
            break
    return True


@app.post("/update_last_file/")
async def update(
        last_file: str = Form(...),
        value: str = Form(...),
):
    if last_file == "last_doc_image":
        global last_doc_image_file
        last_doc_image_file = value
    elif last_file == "last_audio_file":
        global last_audio_file
        last_audio_file = value
    return True
