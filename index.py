import requests
import json
import time
from quesionlist import Q
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  
global contents
contents = ''
t = time.localtime(time.time())
a = str(t[1])+'/'+str(t[2])

def sign():
    for i in Q.keys():
        if a == i:
            d1 = Q[a]
    #?msg前和/send/后填qmsg的key,qq=后填接受消息的QQ号
    qqtalk = 'https://qmsg.zendee.cn/send/b56722459be0fe9f1f5caf1e39ec97de?msg=' + d1 + '&qq=1127434344'
    requests.get(qqtalk)
 
def main():
    sign()
  
def main_handler(event, context):
    return main()
  
if __name__ == '__main__':
    main()