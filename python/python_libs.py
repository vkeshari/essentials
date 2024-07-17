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
d.isoformat()
dt.isoformat()

dt = datetime.strptime('20240101', '%Y%m%d')
dt.strftime('%Y%m%d')
# Format: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# Date to datetime
dt = datetime.combine(d, datetime.min.time()) # combines date and time


### os ###
from os import listdir

# Iterate files in a directory
files = listdir('/home/vkeshari/super_secret_files') # returns only file names


### pathlib ###
from pathlib import Path

Path.cwd()

p = Path('/home/vkeshari')
q = p / 'work' / 'essentials'

q.parts
q.exists()
q.is_dir()

# Lazily iterate files in a directory
for path in q.iterdir(): # returns full paths
  filename = path.parts[-1]

# Create missing dirs on path
output_file = Path(filename)
output_file.parent.mkdir(exist_ok = True, parents = True)

# Write to a file
with output_file.open('w') as f:
  for d in data:
    f.write(d)


### urllib ###
from urllib import request

page = request.urlopen(url)
text = page.read().decode('utf-8')


### regexp ###


### xml ###


### pickle ###
with open(filename, 'wb+') as f:
  pickle.dump(data, f)

with open(filename, 'rb') as f:
  data = pickle.load(f)


### json ###
class ClassSerializer(json.JSONEncoder):
  def default(self, o):
    if type(o).__name__ == 'ContainerA':
      return o.field1
    if type(o).__name__ == 'ContainerB':
      return o.field2

json.dumps(data, cls = ClassSerializer, \
          indent = 2, sort_keys = True)
