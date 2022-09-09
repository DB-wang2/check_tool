from HTMLTable import (
  HTMLTable,
)
import os, datetime, time
from conf import setting


c_path = os.getcwd()
file_path = c_path + '/html_file'
if not os.path.exists(file_path):
    os.mkdir(file_path)

# 今天日期
today = datetime.date.today()
# 昨天时间
yesterday = today - datetime.timedelta(days=1)
## dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')

# 获得当前系统时间的字符串
localtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print('localtime=' + localtime)
# 系统当前时间年份
year = time.strftime('%Y', time.localtime(time.time()))
# 月份
month = time.strftime('%m', time.localtime(time.time()))
# 日期
day = time.strftime('%d', time.localtime(time.time()))
# 具体时间 小时分钟秒
mdhms = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

fileYear = file_path + '/' + year
fileMonth = fileYear + '/' + month
# fileDay = fileMonth + '/' + day

if not os.path.exists(fileYear):
    os.mkdir(fileYear)
    os.mkdir(fileMonth)
    # os.mkdir(fileDay)
else:
    if not os.path.exists(fileMonth):
        os.mkdir(fileMonth)
        # os.mkdir(fileDay)
    # else:
    #     if not os.path.exists(fileDay):
    #         os.mkdir(fileDay


file_name = fileMonth + '/%s数据库巡检报告.html' % localtime
print(file_name)
file = open(file_name, 'w')

def set_head():
  file_head = '''<html>
  <head>
      <meta charset="UTF-8">
      <title>Bootstrap引入</title>
      <!-- 新 Bootstrap 核心 CSS 文件 -->
      <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css">
      <!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
      <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script>
      <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
      <script src="http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
  
  </head>
          <body>
  '''
  file.write(file_head)
  file.write('<h1  style="text-align:center;font-size:30px">数据库巡检报告</h1>\n<p  style="text-align:center;font-size:14px">%s</p>' %mdhms)


def set_left():
  f = '''
  <div class="row">
    <div class="col-md-2" >
        <ul class="list-group" style="position: fixed; overflow-y:auto; height:85%;overflow-x:auto; width:15%;">
        <li class="list-group-item">实例列表</li>
  '''
  for k, v in setting.database_dic.items():
    f2 = '<li class="list-group-item"> <a href="#%s">%s</a> </li>' %(k,k)
    f +=f2

  f += '''
  </ul>
    </div>
    <div class="col-md-10 " style="overflow-x:auto; width:-85%;">
  '''
  file.write(f)

def set_instance_name(instabce_name):
  file.write('<p>	 <a name="%s"></a>   </p> <br> <span class="glyphicon glyphicon-align-justify" aria-hidden="true" ></span> <span style="font-family:arial;font-size:25px;color:#3376cc" > 实例名：%s </span>' %(instabce_name,instabce_name))


def set_table(name, data):
  file.write('<br>\n<p  style="font-size:20px;">%s</p>' %name)
  if len(data) == 1:
    file.write('<span class="glyphicon glyphicon-ok-sign" aria-hidden="true" ></span> <span style="font-size:14px" > 无异常，继续保持！ </span> <br>')
    return True
  # 标题
  table = HTMLTable()

  # 标题样式
  table.caption.set_style({
    'font-size': '20px',
  })


  # 表头行
  table.append_header_rows([data.pop(0)])

  # 表头样式
  table.set_header_row_style({
    'color': '#fff',
    'background-color': '#48a6fb',
    'font-size': '18px',
  })

  # 数据行
  table.append_data_rows(data)



  # 表格样式，即<table>标签样式
  table.set_style({
    'border-collapse': 'collapse',
    'word-break': 'keep-all',
    'white-space': 'nowrap',
    'font-size': '14px',
  })

  # 统一设置所有单元格样式，<td>或<th>
  table.set_cell_style({
    'border-color': '#000',
    'border-width': '1px',
    'border-style': 'solid',
    'padding': '2px',
  })


  table.colname2index
  # 覆盖表头单元格字体样式
  table.set_header_cell_style({
    'padding': '15px',
  })

  html = table.to_html()
  html = html.replace('<table','<table class="table-striped table-hover"')
  file.write(html)


def set_vt(variables_dict):
  t_t = '''
  <br>
        <p style="font-size:20px;">实例参数</p>
        <table class="table-striped table-hover"
               style="border-collapse:collapse;word-break:keep-all;white-space:nowrap;font-size:14px;"  cellspacing="0" cellpadding="0">
  '''

  for k,v in variables_dict.items():

    t = '''
    <tr>
            <td class="column" style="border-color:#000;border-width:1px;border-style:solid;padding:2px;  color:#fff;background-color:#48a6fb; ">%s</td>
            <td style="border-color:#000;border-width:1px;border-style:solid;padding:2px;">%s</td>
        </tr>
    ''' %(k, v)
    t_t += t

  t_t += '</table>'
  file.write(t_t)


def set_tail():
  file_tail = '''
      </div>
  </div>
  <br>
  <br>
  </body>
  </html>
  '''
  file.write(file_tail)


