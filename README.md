
```

```
# check_tool

使用说明：
下载到本地，脚本根目录执行：
pip install -r requirements.txt
安装所需依赖包。

配置示例

conf/setting.py

```
配置用来访问mysql的用户、密码、端口
user_dict = {
    'username':'root',
    'passwd':'123456',
    'port':3306,

}

配置需要检查的数据库名字与地址
database_dic = {
    'test1': '192.168.1.110',
    'test2': 'mysql.test2.com'
}
```

conf/sql_conf.py

```
按照格式配置sql检查项,参数或者状态这种只返回一个结果值的设置is_variables为1, table_head为输出表格的表头，check_name为表格名称。
sql_list = [
    {
        'sql':"SELECT object_schema, object_name, index_name FROM performance_schema.table_io_waits_summary_by_index_usage WHERE index_name IS NOT NULL AND count_star = 0 AND object_schema NOT IN ('mysql' ,'performance_schema') AND index_name <> 'PRIMARY' ORDER BY object_schema , object_name limit 100;",
        'table_head': ['库名', '表名', '索引名'],
        'check_name': '未使用过的索引',
        'is_variables':0
    },
    {
        'sql':"SELECT a.TABLE_SCHEMA AS '数据库名', a.TABLE_NAME AS '表名', concat(a.INDEX_NAME,',',b.INDEX_NAME) AS '重复索引', a.COLUMN_NAME AS '重复列名'   FROM information_schema.STATISTICS a JOIN information_schema.STATISTICS b ON a.TABLE_SCHEMA = b.TABLE_SCHEMA AND a.TABLE_NAME = b.TABLE_NAME AND a.SEQ_IN_INDEX = b.SEQ_IN_INDEX AND a.COLUMN_NAME = b.COLUMN_NAME WHERE a.SEQ_IN_INDEX = 1 AND a.INDEX_NAME <> b.INDEX_NAME group by a.TABLE_SCHEMA,a.TABLE_NAME,a.COLUMN_NAME limit 100;",
        'table_head': ['库名','表名','重复索引','重复列名'],
        'check_name': '重复索引',
        'is_variables': 0
    },
    {
        'sql': "select version();",
        'table_head': ['MySQl version'],
        'is_variables': 1
    },
    {
        'sql': "SHOW GLOBAL STATUS LIKE 'UPTIME';",
        'table_head': ['uptime(s)'],
        'is_variables': 1
    },


]

```

# 运行

脚本根目录执行：

```
python3 start.py
```

输出报告文件在html_file目录下，根据年/月划分。



