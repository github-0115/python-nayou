#!/user/bin/python
# -*- coding:utf-8 -*-

import MySQLdb


if __name__=='__main__':
    db=MySQLdb.connect('localhost','testuser','test123','TESTDB')
    cursor=db.cursor()
    cursor.execute('SELECT VERSION()')
    data=cursor.fetchone()
    print data
    db.close()