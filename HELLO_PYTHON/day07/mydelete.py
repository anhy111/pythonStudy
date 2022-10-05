import pymysql  # pymysql 임포트
conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")

e_id="3"

cur = conn.cursor()    # 커서생성

# sql = """update emp
#              set e_name = %s,
#              sex = %s,
#              addr = %s
#          where e_id = %s"""    # 실행할 sql문
# result=cur.execute(sql,('4','4','4','3'))
sql = f"""
    delete from emp
    where
        e_id = '{e_id}'
    """
result = cur.execute(sql)
print(result)


conn.commit()
cur.close()
conn.close()    # 종료