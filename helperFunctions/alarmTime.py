from datetime import datetime, timedelta

#Define input formats
FULL_FORMAT = "%Y-%m-%d %H:%M"
TIME_ONLY_FORMAT = "%H:%M"

#takes the user input and returns a valid date time
def parse_alarm_time(usr_txt, now):
    #try easy fix first:
    clean_txt = usr_txt.strip()

    #Full format parse
    try:
        full_datetime = datetime.strptime(clean_txt, FULL_FORMAT)

        if full_datetime <= now:
            return None
        return full_datetime
    except ValueError:
        pass

    #partail format parce:
    try:
        partail_datetime = datetime.strptime(clean_txt, TIME_ONLY_FORMAT)
    except ValueError:
        return None

    alarm_today = datetime.combine(now.date(), partail_datetime)

    #Is the alarm today?
    if alarm_today > now:
        return alarm_today
    
    #otherwise its other    
    alarm_tomorrow = alarm_today + timedelta(days=1)
    return alarm_tomorrow

def AskTimeInTerm ():
    print("Enter alarm time as HH:MM (24-hour) or YYYY-MM-DD HH:MM")

    while True:
        user_text = input("Alarm time: ")

    
        alarm_time = parse_alarm_time(user_text, datetime.now())

        if alarm_time is None:
            print("That time is invalid or already passed. Try again, e.g. 07:30")
            continue
        
        print("Alarm set for", alarm_time.strftime("%A %Y-%m-%d at %H:%M"))
        return alarm_time