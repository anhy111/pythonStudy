from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from emp_dao import EmpDao

app = FastAPI()
 
app.mount("/static", StaticFiles(directory="static"), name="static") 
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
@app.get('/emp_list', response_class=HTMLResponse)
async def emp_list(request: Request):
    ed = EmpDao()
    emps = ed.selects()
    return templates.TemplateResponse("emp_list.html", {"request": request, "emps":emps})

@app.get('/emp_detail', response_class=HTMLResponse)
async def emp_detail(request: Request, e_id : str):
    ed = EmpDao()
    emp = ed.select(e_id)
    return templates.TemplateResponse("emp_detail.html", {"request": request, "emp":emp})

@app.get('/emp_mod', response_class=HTMLResponse)
async def emp_mod(request: Request, e_id : str):
    ed = EmpDao()
    emp = ed.select(e_id)
    return templates.TemplateResponse("emp_mod.html", {"request": request, "emp":emp})

@app.post("/emp_mod_act", response_class=HTMLResponse)
async def emp_mod_post(request: Request,e_id: str = Form('e_id'),e_name: str = Form('e_name')
                        ,sex: str = Form('sex'),addr: str = Form('addr')):
    ed = EmpDao()
    result = ed.update(e_id, e_name, sex, addr)
    return templates.TemplateResponse("emp_mod_act.html", {"request": request, "result":result})

@app.get('/emp_del_act', response_class=HTMLResponse)
async def emp_del_act(request: Request, e_id : str):
    ed = EmpDao()
    result = ed.delete(e_id)
    return templates.TemplateResponse("emp_del_act.html", {"request": request, "result":result})

@app.get('/emp_add', response_class=HTMLResponse)
async def emp_add(request: Request):
    return templates.TemplateResponse("emp_add.html", {"request": request})

@app.post("/emp_add_act", response_class=HTMLResponse)
async def emp_add_act(request: Request,e_id: str = Form('e_id'),e_name: str = Form('e_name')
                        ,sex: str = Form('sex'),addr: str = Form('addr')):
    ed = EmpDao()
    result = ed.insert(e_id, e_name, sex, addr)
    return templates.TemplateResponse("emp_add_act.html", {"request": request, "result":result})
# uvicorn myemp:app --reload