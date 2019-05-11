from datetime import datetime, timedelta

dt1 = datetime(2018, 12, 10) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1

print("days:", duration.days)
print("sec:", duration.seconds)
print("tot sec: ", duration.total_seconds())
