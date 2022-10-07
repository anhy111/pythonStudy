from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
import pymysql 

app = FastAPI()
 
app.mount("/static", StaticFiles(directory="static"), name="static") 

templates = Jinja2Templates(directory="templates")

@app.get('/hello', response_class=HTMLResponse)
async def hello(request: Request):
    conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")

    cur = conn.cursor()    # 커서생성
    conn.cursor()
    
    sql = "select * from emp"    # 실행할 sql문
    cur.execute(sql)
    emps = cur.fetchall()
    print(emps)
    # emps = [
    #     {'e_id':'1',"e_name":"1","sex":"1","addr":"1"},
    #     {"e_id":"1","e_name":"1","sex":"1","addr":"1"},
    #     {"e_id":"1","e_name":"1","sex":"1","addr":"1"}
    # ]
    
    cur.close()
    conn.close()    # 종료
    
    return templates.TemplateResponse("index.html", {"request": request, "emps":emps})