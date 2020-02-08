#0.036 Project TimeZone Class Solution

import numbers
from datetime import timedelta

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name)) == 0 :
            raise ValueError('TimeZone name can not be empty.')

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an Integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minute offset must be an Integer.')

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError('Minutes offset must be between -59 and 59')

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00')

        self._offset_hours = offset_hours
        self._offset_minuts = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
        self.name == other.name and
        self._offset_hours == other._offset_hours and
        self._offset_minuts == other._offset_minuts)


    def __repr__(self):
        return(f"TimeZone(name='{self.name}',"
               f"offset_hours='{self._offset_hours}',"
               f"offset_minuts='{self._offset_minuts})'")


#Unit Test:-

tz1 = TimeZone('ABC', -2, -15)

print(tz1.name)
#ABC

print(tz1.__dict__)

from datetime import datetime

dt = datetime.utcnow()
print(dt)
#2020-02-08 21:09:00.180463

print(dt + tz1.offset)
#Output will decrease it by -2 and -15

try:
    tz = TimeZone('',0,0)
except Exception as e:
    print(e)

#TimeZone name can not be empty.