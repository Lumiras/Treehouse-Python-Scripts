from datetime import datetime
import pytz

OTHER_TIMEZONES = [
pytz.timezone('US/Eastern'),
pytz.timezone('Pacific/Auckland'),
pytz.timezone('Asia/Calcutta'),
pytz.timezone('Europe/Paris'),
pytz.timezone('Africa/Khartoum'),
pytz.timezone('UTC')
]

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("When is your meeting? Please use MM/DD/YYYY HH:MM format. ")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem like a valid date and time".format(date_input))
    else:
        local_date = pytz.timezone('US/Eastern').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)

        output = []

        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break