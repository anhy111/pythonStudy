import pymysql
class EmpDao:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selects(self):
        sql = "select e_id, e_name, sex, addr from emp"    # 실행할 sql문
        self.curs.execute(sql)
        result = self.curs.fetchall()
        return result
    
    def select(self, e_id):
        sql = f"""
                select 
                    e_id
                    , e_name
                    , sex
                    , addr
                from
                    emp
                where 
                    e_id = '{e_id}'
            """    # 실행할 sql문
        self.curs.execute(sql)
        result = self.curs.fetchall()
        return result[0]
    
    def insert(self, e_id, e_name, sex, addr):
        sql = f"""
                insert into emp(
                e_id
                , e_name
                , sex
                , addr
                )
                 values(
                 '{e_id}'
                 , '{e_name}'
                 , '{sex}'
                 , '{addr}'
                 )
                 """    # 실행할 sql문
        result=self.curs.execute(sql)
        self.conn.commit()
        return result
    
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
                update emp
                set
                    e_name = '{e_name}'
                    , sex = '{sex}'
                    , addr = '{addr}'
                where
                    e_id = '{e_id}'
                
            """    # 실행할 sql문
        result=self.curs.execute(sql)
        self.conn.commit()
        return result
    
    def delete(self,e_id):
        sql = f"""
                delete from 
                    emp
                where
                    e_id = '{e_id}'
            """    # 실행할 sql문
        result=self.curs.execute(sql)
        self.conn.commit()
        return result
    
    def __del__(self):
        self.curs.close()
        self.conn.close()


if __name__ == '__main__':
    ed = EmpDao()
    rows = ed.selects()
    print(rows)
    rows = ed.select(1)
    print(rows)
    rs = ed.delete('3')
    print("성공" if rs else "실패")
    