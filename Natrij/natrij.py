a_time = [int(x) for x in input().split(":")]
b_time = [int(x) for x in input().split(":")]

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
HOURS_IN_DAY = 24

a_secs = a_time[0] * SECONDS_IN_HOUR + a_time[1] * SECONDS_IN_MINUTE + a_time[2]
b_secs = b_time[0] * SECONDS_IN_HOUR + b_time[1] * SECONDS_IN_MINUTE + b_time[2]

if b_secs <= a_secs:
    a_secs -= SECONDS_IN_HOUR * HOURS_IN_DAY

timediff = abs(b_secs - a_secs)

hours_and_seconds = divmod(timediff, SECONDS_IN_HOUR)
minutes_and_seconds = divmod(hours_and_seconds[1], SECONDS_IN_MINUTE)

print("{:02d}:{:02d}:{:02d}".format(hours_and_seconds[0],
                                    minutes_and_seconds[0],
                                    minutes_and_seconds[1]))
