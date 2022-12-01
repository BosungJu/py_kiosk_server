import pymysql

insertQuery = 'insert into kiosk.{tableName} values({datas})'
selectQuery = 'select {params} from kiosk.{tableName} where id="{data}"'
selectQueryAll = 'select {params} from kiosk.{tableName}'
deleteQuery = 'delete from kiosk.{tableName} where id="{data}"'

conn = ''

def setup():
    global conn
    conn = pymysql.connect(host='localhost', user='root', passwd='root1234', charset='utf8', port=3307)

def insert(tableName, datas):
    cur = conn.cursor()
    sql = insertQuery.format(tableName=tableName, datas=datas)
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
    setup()

def select(params, tableName, data=''):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    if data != '':
        sql = selectQuery.format(params=params, tableName=tableName, data=data)
    else:
        sql = selectQueryAll.format(params=params, tableName=tableName)

    cur.execute(sql)

    datas = cur.fetchall()

    cur.close()
    return datas

def delete(tableName, data):
    cur = conn.cursor()
    sql = deleteQuery.format(tableName=tableName, data=data)
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
    setup()