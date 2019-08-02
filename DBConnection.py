import pymysql.cursors
import io
import os
from bs4 import BeautifulSoup

class SqlConn():

    def __init__(self, database):

        module_path = os.path.dirname(__file__)

        path = module_path + '/config.xml'

        configfile = io.open(path, encoding='utf-8')

        connectioninf = BeautifulSoup(configfile, 'xml')

        server = connectioninf.find('Server').text.strip()

        profile = connectioninf.find('Profile').text.strip()

        pwd = connectioninf.find('Pwd').text.strip()

        self.conn = pymysql.connect(host = server,
                                     user = profile,
                                     password = pwd,
                                     db = database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        self.cur = self.conn.cursor()

    def cur(self):

        return self.cur()

    def commit(self):

        self.conn.commit()

    def execute(self,sql,fetchone=0):

        self.cur.execute(sql)

        return self.cur.fetchone() if fetchone else self.cur.fetchall()

    def last_id(self,table):

        sql='SELECT LAST_INSERT_ID() from %s'%table

        return self.execute(sql,1)[0]

    def close(self):

        self.cur.close()

        self.conn.close()

    def safe(self, s):

        return pymysql.escape_string(s)

    def get_i_sql(self, table, dict):
        '''
        create insert sql statement
        @table，insert table name
        @dict, insert data，dict
        '''
        sql = 'insert into %s set ' % table
        sql += self.dict_2_str(dict)
        return sql

    def get_s_sql(self, table, keys, conditions, isdistinct=0):
        '''create select sql statement
        @table，enquiry table name
        @key，select fields
        @conditions, where condition，dict
        @isdistinct, distinct or not
        '''
        if isdistinct:

            sql = 'select distinct %s ' % ",".join(keys)
        else:

            sql = 'select  %s ' % ",".join(keys)

        sql += ' from %s ' % table

        if conditions:

            sql += ' where %s ' % self.dict_2_str_and(conditions)

        return sql

    def get_u_sql(self, table, value, conditions):
        '''create update sql statement
        @table，update table name
        @value，fields to be update, dict
        @conditions,where condition，dict
        '''
        sql = 'update %s set ' % table
        sql += self.dict_2_str(value)
        if conditions:
            sql += ' where %s ' % self.dict_2_str_and(conditions)
        return sql

    def get_d_sql(self,table, conditions):
        '''
            create detele sql statement
        @table，

        @conditions, where condiction，dict
        '''
        sql = 'delete from  %s  ' % table
        if conditions:
            sql += ' where %s ' % self.dict_2_str_and(conditions)
        return sql

    def dict_2_str(self, dictin):
        '''
        convert dict to key='value' and key='value'
        '''
        tmplist = []
        for k, v in dictin.items():
            tmp = "%s='%s'" % (str(k), self.safe(str(v)))
            tmplist.append(' ' + tmp + ' ')
        return ','.join(tmplist)

    def dict_2_str_and(self, dictin):
        '''
        convert dict to key='value' and key='value'
        '''
        tmplist = []
        for k, v in dictin.items():
            tmp = "%s='%s'" % (str(k), self.safe(str(v)))
            tmplist.append(' ' + tmp + ' ')
        return ' and '.join(tmplist)

    def field_retrieve(self, table_name):

        '''
        Return fields of table
        '''
        print('retrieving field name of table' + table_name)

        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + table_name + "';"

        self.cursor.execute(sql)

        resultlist = []

        for row in self.cursor.fetchall():
            resultlist.append(row)

        return resultlist

