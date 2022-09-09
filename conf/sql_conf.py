
# 按照格式配置sql检查项,参数或者状态这种只返回一个结果值的设置is_variables为1
sql_list = [
    {
        'sql':"SELECT object_schema, object_name, index_name FROM performance_schema.table_io_waits_summary_by_index_usage WHERE index_name IS NOT NULL AND count_star = 0\
            AND object_schema NOT IN ('mysql' ,'performance_schema') AND index_name <> 'PRIMARY' ORDER BY object_schema , object_name ;",
        'table_head': ['库名', '表名', '索引名'],
        'check_name': '未使用过的索引',
        'is_variables':0
    },
    {
        'sql':"SELECT a.TABLE_SCHEMA AS '数据库名', a.TABLE_NAME AS '表名', concat(a.INDEX_NAME,',',b.INDEX_NAME) AS '重复索引', a.COLUMN_NAME AS '重复列名' \
    FROM information_schema.STATISTICS a JOIN information_schema.STATISTICS b ON a.TABLE_SCHEMA = b.TABLE_SCHEMA AND a.TABLE_NAME = b.TABLE_NAME \
    AND a.SEQ_IN_INDEX = b.SEQ_IN_INDEX AND a.COLUMN_NAME = b.COLUMN_NAME WHERE a.SEQ_IN_INDEX = 1 AND a.INDEX_NAME <> b.INDEX_NAME \
    group by a.TABLE_SCHEMA,a.TABLE_NAME,a.COLUMN_NAME ;",
        'table_head': ['库名','表名','重复索引','重复列名'],
        'check_name': '重复索引',
        'is_variables': 0
    },
    {
        'sql':"select c.*, pk from (select table_schema, table_name, index_name, concat('|', group_concat(column_name order by seq_in_index separator '|'), '|') cols from INFORMATION_SCHEMA.STATISTICS where index_name != 'PRIMARY' \
        and table_schema != 'mysql' group by table_schema, table_name, index_name) c, (select table_schema, table_name, concat('|', group_concat(column_name order by seq_in_index separator '|'), '|') pk from INFORMATION_SCHEMA.STATISTICS where \
        index_name = 'PRIMARY' and table_schema != 'mysql' group by table_schema, table_name) p where c.table_name = p.table_name and c.table_schema = p.table_schema and c.cols like concat('%', pk, '%') ;",
        'table_head': ['库名','表名','索引名','索引字段', '主键字段'],
        'check_name': '包含主键的索引',
        'is_variables': 0
    },
    {
        'sql': "select table_schema,table_name from information_schema.tables where (table_schema,table_name) not in(     select distinct table_schema,table_name from information_schema.columns where \
        COLUMN_KEY='PRI'  ) and  table_schema not in ('mysql','performance_schema','information_schema','test') and table_type='BASE TABLE';",
        'table_head': ['库名', '表名'],
        'check_name': '无主键的表',
        'is_variables': 0
    },
    {
        'sql': "SELECT object_schema AS table_schema, object_name AS table_name, count_star AS rows_io_total, count_read AS rows_read, count_write AS rows_write, count_fetch AS rows_fetchs, count_insert AS \
        rows_inserts, count_update AS rows_updates, count_delete AS rows_deletes FROM performance_schema.table_io_waits_summary_by_table ORDER BY sum_timer_wait DESC LIMIT 10;",
        'table_head': ['库名', '表名', '事件总数', 'read次数', 'write次数', 'fetch次数','insert次数', 'update次数' ,'delete次数'],
        'check_name': '热点表TOP10',
        'is_variables': 0
    },
    {
        'sql': "SELECT table_schema, table_name, (index_length + data_length) total_length, table_rows, data_length, index_length, data_free, ROUND(data_free / (index_length + data_length), 2) \
        rate_data_free FROM information_schema.tables WHERE table_schema NOT IN ('information_schema' , 'mysql', 'performance_schema', 'sys') and ROUND(data_free / (index_length + data_length), 2) > 30 \
        ORDER BY rate_data_free desc;",
        'table_head': ['库名', '表名', '总数据量', '表行数', '数据空间（Bytes）', '索引空间（Bytes）', '空闲空间（Bytes）', '表碎片率（%）'],
        'check_name': '碎片超过30%的表',
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
    {
        'sql': "show global variables like 'autocommit';",
        'table_head': ['autocommit'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'binlog_cache_size';",
        'table_head': ['binlog_cache_size(Byte)'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'binlog_format';",
        'table_head': ['binlog_format'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'binlog_row_image';",
        'table_head': ['binlog_row_image'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'max_binlog_cache_size';",
        'table_head': ['max_binlog_cache_size(Byte)'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'max_binlog_size';",
        'table_head': ['max_binlog_size(Byte)'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'sync_binlog';",
        'table_head': ['sync_binlog'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'innodb_flush_log_at_trx_commit';",
        'table_head': ['innodb_flush_log_at_trx_commit'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'innodb_buffer_pool_size';",
        'table_head': ['innodb_buffer_pool_size(Byte)'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'max_connections';",
        'table_head': ['max_connections'],
        'is_variables': 1
    },
    {
        'sql': "show global variables like 'innodb_log_file_size';",
        'table_head': ['innodb_log_file_size(Byte)'],
        'is_variables': 1
    },


]

