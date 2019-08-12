import pymysql
host_ip='35.234.25.100'
host_port=3306
user_name='neskwoe'
user_pwd='nesk1234'
db_name='newsMySQLDatabase'

def connect_db():
    db = pymysql.connect(host=host_ip, user=user_name, passwd=user_pwd, port=host_port, db=db_name)
    return db

def execute_sql(fileName):
    db=connect_db()
    cur = db.cursor()

    with open("sql_file/"+ fileName +".sql") as file_object:
        contents=file_object.read()
    # print(contents)
    cur.execute(contents)
    cur.close()
    db.close()
    return 0
