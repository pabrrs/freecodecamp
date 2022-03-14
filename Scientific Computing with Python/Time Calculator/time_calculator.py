import calendar
from datetime import datetime, timedelta

def days_referece_format(days_diff):
  cases = {
    0: '', # same day
    1: ' (next day)', # next day
  }
  return cases.get(days_diff, f' ({days_diff} days later)')


def sum_week(weekday, add_days):
  weeksize = 7
  weekday_no = list(calendar.day_name).index(weekday.capitalize())
  week_sum = weekday_no + add_days
  if week_sum <= 6:
    return calendar.day_name[week_sum]
  else:
    return calendar.day_name[week_sum % weeksize]

def add_time(start, duration, weekday: str = None):  
  hour_start = datetime.strptime(start, '%I:%M %p')
  duration_hour, duration_min = duration.split(':')
  duration_dt = timedelta(
    hours=int(duration_hour),
    minutes=int(duration_min)
  )

  time_added = hour_start + duration_dt
  diff_days = time_added.day - hour_start.day
  
  days_reference = days_referece_format(diff_days)
  
  time_added_str = time_added.strftime('%-I:%M %p')
  
  if weekday:
    new_weekday = sum_week(weekday.capitalize(), diff_days)
    return f'{time_added_str}, {new_weekday}{days_reference}'
  else:
    return f'{time_added_str}{days_reference}' 