import time
import datetime
from datetime import datetime

d1 = '07/29/2022 13:55:26'
d1 = datetime.strptime(d1, '%m/%d/%Y %H:%M:%S')
unixtime = datetime.timestamp(d1)*1000

d2 = datetime.now()
unixtime2 = datetime.timestamp(d2)*1000

print(int(unixtime))
print(int(unixtime2))
