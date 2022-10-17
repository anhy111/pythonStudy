import pymysql
class MemDao:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",port=3305, user="root", password='python', db='python',charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selects(self):
        sql = """select m_seq, m_name, tel, army_yn from member
                    order by 1"""    # 실행할 sql문
        self.curs.execute(sql)
        result = self.curs.fetchall()
        return result
    
    def select(self, m_seq):
        sql = f"""
                select 
                    m_seq
                    , m_name
                    , tel
                    , army_yn
                from
                    member
                where 
                    m_seq = '{m_seq}'
            """    # 실행할 sql문
        self.curs.execute(sql)
        result = self.curs.fetchall()
        return result[0]
    
    def insert(self, m_name, tel, army_yn):
        sql = f"""
                insert into member(
                 m_name
                , tel
                , army_yn
                )
                 values(
                  '{m_name}'
                 , '{tel}'
                 , '{army_yn}'
                 )
                 """    # 실행할 sql문
        result=self.curs.execute(sql)
        self.conn.commit()
        return result
    
    def update(self, m_seq, m_name, tel, army_yn):
        sql = f"""
                update member
                set
                    m_name = '{m_name}'
                    , tel = '{tel}'
                    , army_yn = '{army_yn}'
                where
                    m_seq = '{m_seq}'
                
            """    # 실행할 sql문
        result=self.curs.execute(sql)
        self.conn.commit()
        return result
    
    def delete(self, m_seq):
        sql = f"""
                delete from 
                    member
                where
                    m_seq = '{m_seq}'
            """    # 실행할 sql문
        result=self.curs.execute(sql)
        self.conn.commit()
        return result
    
    def __del__(self):
        self.curs.close()
        self.conn.close()


if __name__ == '__main__':
    md = MemDao()
    # rows = md.selects()
    # print(rows)
    # rows = md.select(1)
    # print(rows)
    # md.insert("2", '2', '2', '2')
    # print("성공" if md else "실패")
    md.update("2", '3', '3', '3')
    print("성공" if md else "실패")
    # rs = md.delete('58')
    # print("성공" if rs else "실패")