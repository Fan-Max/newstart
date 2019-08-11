import pymysql
db = pymysql.connect(host = '192.168.40.11',user = 'root',passwd = 'root',port = 3306,db = 'pythondemo')
cur=db.cursor()
cur.execute("select version();")
res=cur.fetchall()
print(res)
cur.close()
db.close
