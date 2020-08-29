#from datetime package import date module
from datetime import date

#supply date(year, month, date) and calculate difference
d1= date(2014, 7, 2)
d2= date(2014, 7, 11)
diff = d2 - d1

print(diff.days)
