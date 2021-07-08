from datetime import *

def add_time(start, duration, day="Monday"):
    start = datetime.strptime(start, '%I:%M %p')
    duration = timedelta(minutes=(int(duration.split(":")[0]) * 60) + int(duration.split(":")[1]))
    new_time = (start + duration).strftime("%-I:%M %p")
    
    return new_time