import pymysql
class DB():
    def __init__(self,host,user,passwd,db,port):
        conn = pymysql.connect(
            # 数据库信息
            host=host,
            user=user,
            passwd=passwd,
            db=db,
            port=port
        )
        # 获取数据库对象
        self.cursor = conn.cursor(pymysql.cursors.DictCursor)
    def step_class(self,sql):
        #获取事件总数
        self.cursor.execute(sql)
        return self.cursor.fetchall()
print(DB)