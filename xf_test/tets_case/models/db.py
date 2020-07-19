import pymysql


def get_mysql(sql):
    db_conn = pymysql.connect(
        host='*******',
        port=3306,
        user='root',
        password='wxfmysql',
        db='learning_test',
        # charset='uth-8',
    )
    cursor = db_conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    db_conn.close()
    return data

# cur = conn.cursor()  # 创建游标对象, 用来给数据库发送sql语句并执行
# sqli = "select * from auth_user where id=1"
# result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数
# print(result)
# print(cur.fetchone())  # 获取下一个查询结果集
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchmany(2))  # 获取指定个数个查询结果集
# info = cur.fetchall()  # 获取所有的查询结果
# print(info)
# print(len(info))
# print(cur.rowcount)  # 返回执行sql语句影响的行数


class DBHandler(object):
    """数据库基础操作"""
    def __init__(self, host='*******', port=3306, user='root', password='wxfmysql', db='learning_test',):
        """初始化，这里默认使用我自己的数据库，使用时更换为自己的即可"""
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db
        )
        self.cursor = self.conn.cursor()

    def query_one(self, sql):
        """查询一条数据语句"""
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def query_all(self, sql, arg=None):
        """查询所有数据语句"""
        self.cursor.execute(sql, arg)
        return self.cursor.fetchall()

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    sq = "SELECT * FROM auth_user WHERE username='查询测试1'"
    lists = get_mysql(sq)
    print(lists)











