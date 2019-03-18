import datetime
now = datetime.datetime.now()

print(now)
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print("오늘은 {}년 {}월 {}일 시간은 {}시 {}분 입니다.".format(now.year, now.month, now.day, now.hour, now.minute))


