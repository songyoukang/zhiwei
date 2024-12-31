import pytest
from Dbapi import DB
from Api import MyApi
from common import *
# 创建数据库连接实例
db = DB(**db_link_info_zhiwei)
#获取接口对象数据
api_data1 = MyApi().get_task()
#测试用例执行
class TestGetTask():
    try:
        # 测试用例执行前置步骤
        def setup_method(self):
            print('+++++++++++++++++++开始执行测试用例+++++++++++++++++++++++++')
        # 调用API事件待办总数并获取数据
        def test_get_task_wait_count(self):
            myTaskWaitCount=api_data1['data']['myTaskWaitCount']
            # 执行数据库查询获取待办事件数量
            sql = 'select * from sys_message where id=1697440833750430141'
            data= db.step_class(sql=sql)
            print(data)
            #数据验证
            assert myTaskWaitCount == data[0]['id']
        # 调用API事件待办总数并获取数据
        def test_get_task_business_formcount(self):
            myBusinessFormCount = api_data1['data']['myBusinessFormCount']
            # 执行数据库查询获取待办事件数量
            sql = 'select id from sys_message where id=1697440833750430149'
            data = db.step_class(sql=sql)
            # 数据验证
            assert myBusinessFormCount == data[0]['id']
        # 调用API事件待办总数并获取数据
        def test_get_task_myTaskWaitCount(self):
            myBusinessFormCount = api_data1['data']['myBusinessFormCount']
            # 执行数据库查询获取待办事件数量
            sql = 'select id from sys_message where id=1697440833750430145'
            data = db.step_class(sql=sql)
            # 数据验证
            assert myBusinessFormCount == 164
        def teardown_method(self):
            print('+++++++++++++++++++执行测试用例结束+++++++++++++++++++++++++')
    except EOFError as e:
        # 处理 FileNotFoundError 异常
        print(f"捕获到 SqlError: {e}")
    finally:
        pass
if __name__ == '__main__':
    pytest.main(['-vs','testgettask.py'])

