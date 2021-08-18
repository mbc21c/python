import datetime

now = datetime.datetime.now()
print(now)  # 2015-04-19 12:11:32.669083

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)  # 2015-04-19

nowTime = now.strftime('%H:%M:%S')
print(nowTime)  # 12:11:32

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2015-04-19 12:11:32

yesterday = now - datetime.timedelta(days=1)
yesterdayDate = yesterday.strftime('%Y-%m-%d')
print(yesterdayDate) # 2015-04-20 12:40:00.320686