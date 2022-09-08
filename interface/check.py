from lib import common

mysql_logger = common.get_logger('mysql')


def select_db(instance, sql):
    try:
        cursor = common.mysql_conn(instance, 'mysql')
        cursor.execute("set sql_mode='';")
        res = cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        mysql_logger.error(e)
