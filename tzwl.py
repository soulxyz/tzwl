##练手项目，帮别人写的小爬虫

import requests
import json
import time

ts = str(int(time.time())) #当前unix时间戳
txtname = ts + ".txt"
start_id = 2021020704515646309
stop_id = 2021020704515646311

## goodid处理模块
goodid_dist = {'20' : '1元试用',
          '22' : '25元/1个月',
          '21' : '70元/3个月',
          '5'  : '249元/12个月',
          '10' : 'IOS软件专用美区下载ID'}
def goodid_(goodid):
    try:
        #print (goodid_dist[goodid])
        return goodid_dist[goodid]
    except:
        #print ("UnknownID:"+goodid)
        return "UnknownID:"+goodid


##

##数据获取模块
def data_get(ddid):
    global data #定义全局变量data以便在函数体外也可引用
    url = "http://tzwl.xyz/index/kminfo.html?ddid="+str(ddid)
    r = requests.get(url) #get
    data = r.text
    if data.startswith(u'\ufeff'):
          data = data.encode('utf8')[3:].decode('utf8') #encode Utf8-BOM
    data = json.loads(data)  #type list
    try:
        data = data[0] #type dist
    except:
        data = {'mima': '####'}
##

for ddid in range(start_id,stop_id+1):
    data_get(ddid)
    if data['mima'] == '####':
        print (str(ddid)+' 无返回值')
    else:
        goodid_re = goodid_(str(data['goodid']))
        print (str(ddid),data['mima'],goodid_re)
        with open(txtname, mode='a') as file:#只写模式下追加写入
            file.write(str(data['id'])+'#'+goodid_re+'#'+data['mima']+'#'+str(ddid)+'#'+data['time'])
            file.write('\n') # 换行
