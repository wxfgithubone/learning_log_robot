# sum = 0
# for i in range(1, 101):
#     sum = sum+i
# print(sum)
#
# """1-100的和"""
# a = 0
# for s in range(1, 101):
#     a += s
# print("和为：%s" % a)
#
# """1-100偶数和奇数的和"""
# b = 0
# c = 0
# for f in range(1, 101):
#     if f % 2 == 0:
#         b += f
#     else:
#         c += f
# print("偶数和：{0}".format(b))
# print("奇数和：{0}".format(c))

import xlrd


# def get_data():
#     dir_case = 'F:\\xf_py\\conner\\learning_log\\xf_test\\data\\login.xlsx'
#     data = xlrd.open_workbook(dir_case)
#     table = data.sheets()[0]
#     nor = table.nrows
#     nol = table.ncols
#     dict = {}
#     for i in range(1, nor):
#         for j in range(nol):
#             title = table.cell_value(0, j)
#             value = table.cell_value(i, j)
#             dict[title] = value
#         yield dict


def excel_by_index(file, by_index):  # 按表的索引读取
    data = xlrd.open_workbook(file)  # 打开excel文件
    tab = data.sheets()[by_index]  # 选择excel里面的Sheet
    nrows = tab.nrows  # 行数
    ncols = tab.ncols  # 列数
    colName = tab.row_values(0)  # 第0行的值，标题行
    lists = []  # 创建一个空列表
    for x in range(1, nrows):      # 第一行为标题（第一行为0），所以从第二行开始
        row = tab.row_values(x)
        print("\033[31m外层行循环：\033[0m %s" % x)
        if row:
            app = {}  # 创建空字典
            for y in range(ncols):
                print("\033[33m内存列循环：\033[0m %s" % y)
                app[colName[y]] = row[y]
                print("标题行：%s" % colName[y])
                print("参数值：%s" % row[y])
                # print(app)
            lists.append(app)
    return lists
    # print(lists)


if __name__ == '__main__':
    # a = excel_by_index('F:\\xf_py\\conner\\learning_log\\xf_test\\data\\login.xlsx', 0)
    # # print(a)
    # for i in range(0, len(a)):
    #     print(a[i]["用户名"], a[i]["密码"], a[i]["验证码"])
    from xf_test.tets_case.models.function import DoExcel
    list_data = DoExcel().read_data("F:/xf_py/conner/learning_log/xf_test/data/register.xlsx", 0)
    print(list_data)
    f = excel_by_index("F:/xf_py/conner/learning_log/xf_test/data/register.xlsx", 0)
    print(f)
