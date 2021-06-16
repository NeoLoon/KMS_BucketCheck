import requests
import time
import pytz
from datetime import datetime

kst = pytz.timezone('Asia/Seoul')

while 1:
    t = datetime.now(tz=kst).strftime('%m%d')
    for i in range(0,49):
        url = "http://origin.ssl.nx.com/s3/Game/Maplestory/event/2021/{}".format(t)
        r = requests.get(url)
        
        if r.ok:
            print ('File bucket created')
        else:
            print ('No bueno')
        time.sleep(1800)
            
