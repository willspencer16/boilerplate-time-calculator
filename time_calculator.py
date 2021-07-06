def add_time(start, duration):
    start_input = start.split()
    start_meridiem = start_input[1]
    start_time = start_input[0].split(':')
    start_hours = start_time[0]
    start_minutes = start_time[1]

    duration_input = duration.split()
    duration_time = duration_input[0].split(':')
    duration_hours = duration_time[0]
    duration_minutes = duration_time[1]

    if start_meridiem == 'PM':
        start_hours = int(start_hours) + 12
    
    new_hours = int(start_hours) + int(duration_hours)

    if new_hours > 24:
        new_hours = int(new_hours) - 24
        new_meridiem = 'AM'
    else:
        new_hours = int(new_hours) - 12
        new_meridiem = start_meridiem
    

    new_minutes = int(start_minutes) + int(duration_minutes)

    new_time = f"{new_hours}:{new_minutes:02d} {new_meridiem}"
    
    return new_time