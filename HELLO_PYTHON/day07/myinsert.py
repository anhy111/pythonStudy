import pymysql  # pymysql 임포트
conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")

cur = conn.cursor()    # 커서생성
conn.cursor()

sql = "insert into emp(e_id, e_name, sex, addr) values(%s, %s, %s, %s)"    # 실행할 sql문
result=cur.execute(sql,('4','4','4','4'))
print(result)

conn.commit()

cur.close()
conn.close()    # 종료