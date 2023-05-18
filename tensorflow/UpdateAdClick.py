import MySQLdb

host = "47.93.45.147"

user = 'root'

password = "lFT1AWoRNL0e6121"

dbname = 'car'


db = MySQLdb.connect(host, user, password, dbname, charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
for i in range(10000):
    cursor.execute("insert into car.user_click (click_time,click_ip) values('2021-1-1 00:00:00', '127.0.0.1')")
    print("executing %d"%i)

db.commit()

cursor.execute("select count(*) from car.user_click")

print("current click count:%d"%cursor.fetchone()[0])

db.close()

