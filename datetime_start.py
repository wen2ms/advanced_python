import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

now = datetime.datetime.now()
print(now)

day = datetime.datetime(2026, 8, 31, 21, 52)
print(day)

day = datetime.datetime.strptime("2026-10-05", "%Y-%m-%d")
print(day)
print(day.year)
print(day.month)
print(day.day)
print(day.hour)
print(day.minute)
print(day.second)
print(day.microsecond)
print(day.weekday())

print(day.strftime("%YYear%mMonth%dDay %H:%M:%S"))

day1 = datetime.datetime(2000, 1, 1)
day2 = datetime.datetime(2026, 9, 1)

delta = day2 - day1

print(delta.days)
print(delta.seconds)
print(delta.microseconds)
print(delta.total_seconds() / 60 / 60 / 24)

delta = datetime.timedelta(10, 0)
print(day1 + delta)

print(now.tzinfo)
now = datetime.datetime.now(datetime.UTC)
print(now)
print(now.tzinfo)

timezone = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now(timezone)
print(now)
print(now.tzinfo)

now = datetime.datetime.now(ZoneInfo("Asia/Shanghai"))
print(now)

time = datetime.datetime.now()
local_time = time.astimezone()
print(local_time)
print(local_time.strftime("%Y%m%d"))

last_access_timestamp = Path(__file__).stat().st_atime
print(datetime.datetime.fromtimestamp(last_access_timestamp, datetime.UTC))
