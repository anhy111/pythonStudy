from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pymysql  # pymysql 임포트


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return """
        Hello World
    """

@app.get("/dan", response_class=HTMLResponse)
async def dan(dan: str = "9"):
    idan = int(dan)
    html = ""

    html += f"{idan}*{1}={idan*1}<br>"
    html += f"{idan}*{2}={idan*2}<br>"
    html += f"{idan}*{3}={idan*3}<br>"
    html += f"{idan}*{4}={idan*4}<br>"
    html += f"{idan}*{5}={idan*5}<br>"
    html += f"{idan}*{6}={idan*6}<br>"
    html += f"{idan}*{7}={idan*7}<br>"
    html += f"{idan}*{8}={idan*8}<br>"
    html += f"{idan}*{9}={idan*9}<br>"
    return f"""
    <html>
        <head>
            <title>구구단</title>
        </head>
        <body>
            {html}
        </body>
    </html>
    """
    
    


@app.post("/dan", response_class=HTMLResponse)
async def dan_post(dan: str = Form()):
    idan = int(dan)
    html = ""
    html += f"{idan}*{1}={idan*1}<br>"
    html += f"{idan}*{2}={idan*2}<br>"
    html += f"{idan}*{3}={idan*3}<br>"
    html += f"{idan}*{4}={idan*4}<br>"
    html += f"{idan}*{5}={idan*5}<br>"
    html += f"{idan}*{6}={idan*6}<br>"
    html += f"{idan}*{7}={idan*7}<br>"
    html += f"{idan}*{8}={idan*8}<br>"
    html += f"{idan}*{9}={idan*9}<br>"
    return f"""
    <html>
        <head>
            <title>구구단</title>
        </head>
        <body>
            {html}
        </body>
    </html>
    """
    
@app.get("/emp", response_class=HTMLResponse)   
async def emp():
    conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")

    cur = conn.cursor()    # 커서생성
    conn.cursor()
    
    sql = "select * from emp"    # 실행할 sql문
    cur.execute(sql)
    result = cur.fetchall()
    
    html = ""
    for rs in result:
        html += "<p>"
        for i in rs:
            html += i + ", "
        html += "</p>"
    cur.close()
    conn.close()    # 종료
    return f"""
    <html>
        <head>
            <title>emp</title>
        </head>
        <body>
            {html}
        </body>
    </html>
    """
# uvicorn main:app --reload