import datetime
date = '18/05/2020 - 18:05:12'

# convert string to datetimeformat
date = datetime.datetime.strptime(date, "%d %m %Y - %H:%M:%S"")

# convert datetime to timestamp
date = datetime.datetime.timestamp(date)