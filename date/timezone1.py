from datetime import datetime
import pytz
#how to get the current timezone


#localtimezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
#print(localtimezone)

d = datetime

london_tz = pytz.timezone('Europe/London')
london_date =d.now(london_tz)
print("london date = ", london_date)
