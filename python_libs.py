import sys
sys.exit("Reference material. Do not execute.")

### datetime ###
from datetime import date, datetime, timedelta

d = date.today()
d.day # year, month, day

d1 - d2 # --> timedelta

dt = datetime.now()
dt.day # hour, minute, second

td = timedelta(days = 1) # weeks, days, hours, minutes, seconds, ...
td.days

# datetime to/from string
# Format: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
dt = datetime.strptime('20240101', '%Y%m%d')
dt.strftime('%Y%m%d')


### pathlib ###
from pathlib import Path

Path.cwd()

p = Path('/home/vkeshari')
q = p / 'work' / 'essentials'

q.parts
q.exists()
q.is_dir()
q.iterdir()

output_file = Path(filename)
output_file.parent.mkdir(exist_ok = True, parents = True) # create missing dirs on path

with output_file.open('w') as f: # no need to close file if opened in scope
  for d in data:
    f.write(d)


### urllib ###
from urllib import request

page = request.urlopen(url)
text = page.read().decode('utf-8')
