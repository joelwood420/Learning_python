def count_days(year, month, whichday):
    import calendar

    # Generate a matrix representing a month's calendar.
    # Each row is a week, days are numbers (0 means no day in that month/week).
    cal = calendar.monthcalendar(year, month)
    
    # Count how many weeks have the specified weekday (non-zero value in the correct position).
    count = sum(1 for week in cal if week[whichday] != 0)
    return count
c
