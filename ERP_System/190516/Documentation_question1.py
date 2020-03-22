def readable_timedelta(days):
    ''' use integer division to get the number of weeks '''
    weeks = days // 7
    ''' use % to get the number of days that remain '''
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)
