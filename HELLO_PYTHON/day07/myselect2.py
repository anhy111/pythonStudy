import pymysql  # pymysql 임포트
conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")

cur = conn.cursor(pymysql.cursors.DictCursor)    # 커서생성

sql = "select * from emp"    # 실행할 sql문
cur.execute(sql)

result = cur.fetchall()
print(result)

cur.close()
conn.close()    # 종료