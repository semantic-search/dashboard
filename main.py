from fastapi import FastAPI, Depends, Form, WebSocket, WebSocketDisconnect
import json
from yaml_parser_service import parse
from task_invoker import invoke



app = FastAPI()
config_dict = parse("config.yaml")
invoke()
active_connections = []


def get_ws_clients():
    return active_connections


@app.get("/")
def config():
    return config_dict


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(client_id: int, websocket: WebSocket, clients=Depends(get_ws_clients)):
    await websocket.accept()
    connected_client = {
        "id": client_id,
        "websocket": websocket
    }
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
        topic_name: str = Form(...),
        value: str = Form(...),
        client_id: int = Form(...),
        clients=Depends(get_ws_clients)
):
    msg_to_send = {
        "container": topic_name,
        "file": value
    }
    for dic in clients:
        if dic["id"] == client_id:
            ws = dic["websocket"]
            await ws.send_text(
                   json.dumps(msg_to_send)
                )
            break
    return True


@app.post("/update_last_file/")
async def update(
        last_file: str = Form(...),
        value: str = Form(...),
        client_id: int = Form(...),
        clients=Depends(get_ws_clients)
):
    msg_to_send = {
        "last_file": last_file,
        "file": value
    }
    for dic in clients:
        if dic["id"] == client_id:
            ws = dic["websocket"]
            await ws.send_text(
                   json.dumps(msg_to_send)
                )
            break
    return True
