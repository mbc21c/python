import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시간은 오전 {}시입니다.".format(now.hour))

if now.hour >=12:
    print("현재 시간은 오후 {}시입니다.".format(now.hour))
