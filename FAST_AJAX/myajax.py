from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from emp_dao import EmpDao
from starlette.responses import JSONResponse
from pydantic.main import BaseModel


class Emp(BaseModel):
    e_id: str = None
    e_name: str = None
    sex: str = None
    addr: str = None


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static") 
templates = Jinja2Templates(directory="templates")

@app.get('/emp', response_class=HTMLResponse)
@app.get('/', response_class=HTMLResponse)
async def emp(request: Request):
    return templates.TemplateResponse("emp.html", {"request": request})

@app.get('/emp_selects')
def emp_selects():
    ed = EmpDao()
    emps = ed.selects()
    return JSONResponse(emps)

@app.post('/emp_select')
def emp_select(emp:Emp):
    ed = EmpDao()
    emps = ed.select(emp.e_id)
    return JSONResponse(emps)

@app.post('/emp_insert')
def emp_insert(emp:Emp):
    ed = EmpDao()
    emps = ed.insert(emp.e_id, emp.e_name, emp.sex, emp.addr)
    return JSONResponse(emps)

@app.post('/emp_update')
def emp_update(emp:Emp):
    ed = EmpDao()
    emps = ed.update(emp.e_id, emp.e_name, emp.sex, emp.addr)
    return JSONResponse(emps)

@app.post('/emp_delete')
def emp_delete(emp:Emp):
    ed = EmpDao()
    emps = ed.delete(emp.e_id)
    return JSONResponse(emps)

# uvicorn myajax:app --reload