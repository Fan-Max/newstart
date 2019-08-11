import pymysql
db = pymysql.connect(host = '192.168.40.11',user = 'root',passwd = 'root',port = 3306,db = 'zbldb',charset = 'utf8')
db.autocommit(True)

cursor=db.cursor()
count=0
sql="CREATE TABLE "\
    "IF NOT EXISTS tb_category("\
    "   ID INT auto_increment,"\
    "   title VARCHAR (100),"\
    "   url VARCHAR (100),"\
    "   PRIMARY KEY (ID)"\
    ")"
print(sql)
cursor.execute(sql)
fr=open('testdata.txt','r')
for line in fr:
    count +=1
    if count==1:
        continue
    line=line.strip().split('^')
    cursor.execute("insert into tb_category (title,url) values (%s,%s)",[line[0],line[1]])
print(count)
fr.close()
cursor.close()
db.close()

