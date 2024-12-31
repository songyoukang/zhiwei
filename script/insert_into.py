# --*-- conding:utf-8 --*--
# @Time : 2024/9/21 13:38
# @Author : sonyoukang
# @Email : syk@163.com
# @File : insert_into.py
# @Software : PyCharm
import pymysql

def DB():
    # 数据库连接信息1111
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'password',
        'db': 'your_database',
        'port': 3306
    }
    # 连接数据库
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
    except pymysql.MySQLError as e:
        print(f"数据库连接失败，错误信息：{e}")
        return

    try:
        # 开始事务
        conn.begin()
        # 批量插入用户信息到 sys_user 表
        user_values = []
        for i in range(1, 10001):
            username = f"user_{i}"
            email = f"user_{i}@example.com"
            password = "default_password"  # 密码需要加密存储，这里仅作示例
            user_values.append((username, email, password))
        sql_user = """
        INSERT INTO sys_user (username, email, password)
        VALUES (%s, %s, %s)
        """
        cursor.executemany(sql_user, user_values)

        # 获取最后插入的 user_id
        last_user_id = cursor.lastrowid
        if last_user_id == 0:
            last_user_id = 1
        role_id = 1  # 假设角色 ID 为 1
        # 批量插入用户角色信息到 sys_user_role 表
        user_role_values = []
        for i in range(last_user_id, last_user_id + 10000):
            user_role_values.append((i, role_id))
        sql_user_role = """
        INSERT INTO sys_user_role (user_id, role_id)
        VALUES (%s, %s)
        """
        cursor.executemany(sql_user_role, user_role_values)
        # 提交事务
        conn.commit()
        print("成功插入 10000 个用户及其角色信息")
    except pymysql.MySQLError as e:
        print(f"插入数据失败，错误信息：{e}")
        # 回滚事务
        conn.rollback()
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()