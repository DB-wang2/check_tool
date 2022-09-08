# 公共方法
import pymysql
import logging.config
from conf import setting


def mysql_conn(host, db):
    conn = pymysql.connect(
        host=host,
        port=setting.user_dict['port'],
        user=setting.user_dict['username'],
        password=setting.user_dict['passwd'],
        db=db,
        charset='utf8',
        autocommit=True
    )
    return conn.cursor(pymysql.cursors.DictCursor)


# 添加日志功能
def get_logger(log_type):
    # 加载配置
    logging.config.dictConfig(
        setting.LOGGING_DIC
    )

    # 获取日志对象
    logger = logging.getLogger(log_type)

    return logger