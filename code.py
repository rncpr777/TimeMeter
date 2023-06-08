import time 

seconds = '00'
minutes = '00'
hours = '00'
days = '00'
while True:
    seconds = str(int(seconds) + 1)
    if int(seconds) < 10:
        seconds =  '0' + seconds
    if seconds == '60':
        minutes = str(int(minutes) + 1)
        if int(minutes) < 10:
            minutes =  '0' + minutes
        seconds = '00'
    if minutes == '60':
        minutes = '00'
        hours = str(int(hours) + 1)
        if int(hours) < 10:
            hours = '0' + hours
    if hours == '24':
        hours = '00'
        days = str(int(days) + 1)
    print(days + ':' + hours + ':' + minutes + ':' + seconds)
    time.sleep(1)
