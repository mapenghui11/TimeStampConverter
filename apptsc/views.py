import time
import pytz
import datetime as dt
from django.shortcuts import render
from django.http import JsonResponse


def timestamp_to_time(request, timestamp, area, city):
    timestamp = int(timestamp)/1000 if len(timestamp) == 13 else int(timestamp)

    local_time = dt.datetime.fromtimestamp(timestamp, pytz.timezone(f'{area}/{city}'))
    formatted_date = local_time.strftime('%Y-%m-%d %H:%M:%S')

    return JsonResponse({'datetime': formatted_date})


def time_to_timestamp(request, datetime, area, city):
    tz = pytz.timezone(f'{area}/{city}')

    format_datetime = dt.datetime.strptime(datetime, "%Y-%m-%d %H:%M:%S")

    target_time = tz.localize(format_datetime)

    timestamp = target_time.timestamp()
    timestamp_ms = int(timestamp) * 1000

    return JsonResponse({'timestamp_ms': timestamp_ms})