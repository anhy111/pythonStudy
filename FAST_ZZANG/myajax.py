from fastapi import FastAPI, Request, Form, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates



app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static") 
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def zzang(request: Request):
    return templates.TemplateResponse("zzang.html", {"request": request})

@app.get('/zzang2', response_class=HTMLResponse)
async def zzang2(request: Request):
    return templates.TemplateResponse("zzang2.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print(f"client connected : {websocket.client}")
    await websocket.accept() # client의 websocket접속 허용
    await websocket.send_text(f"Welcome client : {websocket.client}")
    while True:
        data = await websocket.receive_text()  # client 메시지 수신대기
        print(f"message received : {data} from : {websocket.client}")
        await websocket.send_text(f"Message text was: {data}") # client에 메시지 전달

# uvicorn myajax:app --reload