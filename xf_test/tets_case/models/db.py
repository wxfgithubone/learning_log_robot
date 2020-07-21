import pymysql
from pymysql.err import MySQLError


class MyDB(object):
    def __init__(self, host='106.55.34.101', port=3306, user='root', password='wxfmysql', db='learning_test'):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
            self.cursor = self.conn.cursor()
        except MySQLError as e:
            print("数据库连接池异常：{0}".format(e))
        else:
            pass
        finally:
            pass

    def select_data(self, sql):
        """查询数据"""
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
        except MySQLError as e:
            print("无法获取数据，错误{0}".format(e))
        else:
            return data

    def delete_data(self, sql):
        """删除数据"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLError as e:
            self.conn.rollback()
            print("已回滚至开始前的状态！\n无法删除数据{0}".format(e))

    def update_date(self, sql):
        """更新数据"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLError as e:
            self.conn.rollback()
            print("已回滚至开始前的状态！\n无法更新数据{0}".format(e))

    def insert_data(self, sql):
        """插入数据"""
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLError as e:
            self.conn.rollback()
            print("已回滚至开始前的状态！\n无法插入数据{0}".format(e))

    def close_db(self):
        """关闭连接"""
        self.cursor.close()
        self.conn.close()


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


if __name__ == '__main__':
    db = MyDB()
    a = db.select_data("SELECT * FROM auth_user WHERE username='wxf'")
    print(a)
    b = db.delete_data("DELETE FROM auth_user WHERE username='werwewq'")
    if b not in db.select_data("SELECT * FROM auth_user WHERE username='wxf'"):
        print("已删除")
    else:
        print("未删除")
    c = db.update_date("UPDATE auth_user SET username='改名字了' WHERE id=3 ")
    if c:
        print("3333333333333")










