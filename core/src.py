from interface import set_html
from interface import check
from lib import common

from conf import setting, sql_conf

mysql_logger = common.get_logger('instance')

def run():
    set_html.set_head()
    set_html.set_left()
    for k, v in setting.database_dic.items():
        mysql_logger.info('检查实例：%s中。。。' %k)
        set_html.set_instance_name(k)

        for l in sql_conf.sql_list:
            mysql_logger.info('当前检查项：%s.' %l['check_name'])
            res = check.select_db(v, l['sql'])
            if res:
                data = [l['table_head']]
                for i in res:
                    l1 = []
                    for k2, v2 in i.items():
                        l1.append(v2)
                    data.append(l1)
                set_html.set_table(l['check_name'], data)
            else:
                mysql_logger.error('未获取到值，请检查！')
                data = [l['table_head']]
                set_html.set_table(l['check_name'], data)

    set_html.set_tail()







