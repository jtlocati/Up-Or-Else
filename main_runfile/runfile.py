from model import WebcamRun
from helperFunctions import alarmTime
from datetime import datetime, timedelta
import time

#ask the user when to wake up (returns a datetime)
alarm_time = alarmTime.AskTimeInTerm()
end_time = alarm_time + timedelta(minutes=40)

while datetime.now() < alarm_time:
    time.sleep(1)

WebcamRun.main(end_time)
print("Alarm window over.")