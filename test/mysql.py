import pymysql
from prettytable import PrettyTable
# 打开数据库连接
db = pymysql.connect("localhost","root","","cig",charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM video WHERE id < 10 "
pt = PrettyTable()
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
       pt.add_row(row)

except:
   print ("Error: unable to fecth data")
print (pt)
# 关闭数据库连接
db.close()
