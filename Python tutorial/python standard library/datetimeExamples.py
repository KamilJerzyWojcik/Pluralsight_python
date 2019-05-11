from datetime import datetime
import time


def root():
    pass


dt = datetime(2018, 1, 1)
dt_now = datetime.now()
dt_string = datetime.strptime("2018/02/21", "%Y/%m/%d")
dt_timestamp = datetime.fromtimestamp(time.time())
dt_strftime = dt.strftime("%Y/%m")

print(dt)
print(dt_now)
print(dt_string)
print(dt_timestamp)
print(dt_strftime)
print(dt > dt_now)
