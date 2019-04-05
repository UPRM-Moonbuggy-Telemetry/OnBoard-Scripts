import time as t
from datetime import date as d

date = d.today()
time = t.ctime().split()[3]

print(date)
print(time)
