from model import WebcamRun
from helperFunctions import alarmTime
import datetime

alarm_time = alarmTime.AskTimeInTerm()
alarm_active = False
while alarm_active == False:
    alarm_active = datetime.now() >= alarm_time
WebcamRun.main()