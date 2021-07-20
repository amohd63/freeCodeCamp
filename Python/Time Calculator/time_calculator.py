def add_time(start, duration, day=''):
    days_by_name = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7
    }

    days_by_number = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    start_time, am_pm = start.split(' ')
    start_hours, start_minutes = start_time.split(':')
    duration_hours, duration_minutes = duration.split(':')
    new_hours = int(start_hours) + (12 if am_pm == 'PM' else 0) + int(duration_hours)
    new_minutes = int(start_minutes) + int(duration_minutes)
    num_of_days = 0

    while new_minutes > 60:
        new_minutes -= 60
        new_hours += 1
        if am_pm == 'PM':
            num_of_days += 1

    while new_hours > 24:
        num_of_days += 1
        new_hours -= 24

    if new_hours == 24:
        new_hours -= 12
        am_pm = 'AM'
    elif new_hours > 12:
        new_hours -= 12
        am_pm = 'PM'
    elif am_pm == 'AM' and new_hours == 12:
        am_pm = 'PM'
    else:
        am_pm = 'AM'
    days = num_of_days + days_by_name.get(day.lower(), 0)
    while days > 7:
        days -= 7
    new_time = f'{new_hours}:' + ('0' if new_minutes < 10 else '') + f'{new_minutes}' + f' {am_pm}'
    new_time += (f", {days_by_number.get(days)}" if day != '' else '') + (f" ({num_of_days} days later)" if num_of_days > 1 else ('' if num_of_days == 0 else ' (next day)'))
    return new_time