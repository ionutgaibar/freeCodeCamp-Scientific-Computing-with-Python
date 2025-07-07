def add_time(start, duration, day=''):

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day = day.lower().capitalize()

    clock_start = {
        'hour': int(start.split(' ')[0].split(':')[0]),
        'minute': int(start.split(' ')[0].split(':')[1]),
        'ampm': start.split(' ')[1]
    }
    clock_duration = {
        'hour': int(duration.split(':')[0]),
        'minute': int(duration.split(':')[1])
    }
    clock_final = {
        'day': '',
        'days': 0,
        'hour': 0,
        'minute': '',
        'ampm': ''
    }

    clock_final['minute'] = clock_start['minute'] + clock_duration['minute']

    if clock_start['ampm'] == 'PM':
        clock_final['hour'] += 12

    clock_final['hour'] += clock_start['hour'] + clock_duration['hour'] + clock_final['minute'] // 60

    clock_final['minute'] = clock_final['minute'] % 60

    clock_final['days'] = clock_final['hour'] // 24

    clock_final['hour'] = clock_final['hour'] % 24

    if clock_final['hour'] >= 12:
        clock_final['ampm'] = 'PM'
    else:
        clock_final['ampm'] = 'AM'

    if clock_final['hour'] >= 13:
        clock_final['hour'] = clock_final['hour'] - 12 

    if clock_final['hour'] == 0:
        clock_final['hour'] = 12

    clock_final['minute'] = str(clock_final['minute']).zfill(2)

    if (day in weekdays):
        clock_final['day'] = weekdays[(weekdays.index(day) + clock_final['days']) % 7]

    new_time = f"{clock_final['hour']}:{clock_final['minute']} {clock_final['ampm']}"

    if clock_final['day']:
        new_time += f", {clock_final['day']}"
        
    if clock_final["days"] == 1:
        new_time += " (next day)"
    elif clock_final["days"] > 1:
        new_time += f" ({clock_final['days']} days later)"
    
    return new_time
