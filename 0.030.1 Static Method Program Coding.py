#0.030 Class and Static Method Coding

from datetime import datetime, timezone, timedelta

class Timer:
    tz = timezone.utc

#for all instance of class timer the time must be
#the same time zone where program is running.
    @classmethod
    def set_tz(cls, offset , name):
        cls.tz = timezone(timedelta(hours=offset), name)

    def current_dt_utc(self):




Timer.set_tz(-7,'MST')
print(Timer.tz)

t1 = Timer()
t2 = Timer()

print(t1.tz)
print(t2.tz)