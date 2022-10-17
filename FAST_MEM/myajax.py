from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from pydantic.main import BaseModel
from mem_dao import MemDao


class Mem(BaseModel):
    m_seq: str = None
    m_name: str = None
    tel: str = None
    army_yn: str = None


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static") 
templates = Jinja2Templates(directory="templates")

@app.get('/mem', response_class=HTMLResponse)
@app.get('/', response_class=HTMLResponse)
async def mem(request: Request):
    return templates.TemplateResponse("mem.html", {"request": request})

@app.get('/mem_selects')
def mem_selects():
    md = MemDao()
    mems = md.selects()
    return JSONResponse(mems)

@app.post('/mem_select')
def mem_select(mem:Mem):
    md = MemDao()
    mems = md.select(mem.m_seq)
    return JSONResponse(mems)

@app.post('/mem_insert')
def mem_insert(mem:Mem):
    md = MemDao()
    mems = md.insert(mem.m_name, mem.tel, mem.army_yn)
    return JSONResponse(mems)

@app.post('/mem_update')
def mem_update(mem:Mem):
    md = MemDao()
    mems = md.update(mem.m_seq, mem.m_name, mem.tel, mem.army_yn)
    return JSONResponse(mems)

@app.post('/mem_delete')
def mem_delete(mem:Mem):
    md = MemDao()
    mems = md.delete(mem.m_seq)
    return JSONResponse(mems)

# uvicorn myajax:app --reload