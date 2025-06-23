import sys
sys.exit("Reference material. Do not execute.")


### datetime and dateutil ###
from datetime import date, datetime, timedelta
from dateutil import tz, relativedelta as rd

d = date.today()
d = date.fromisoformat('2024-01-01')
d.day # year, month, day

d.weekday() # Monday is 0, Sunday is 6
d.isoweekday() # Monday is 1, Sunday is 7

d1 - d2 # --> timedelta

dt = datetime.now()
dt.day # hour, minute, second

dt.date() # --> date

td = timedelta(days = 1) # weeks, days, hours, minutes, seconds, ...
td = -timedelta(days = 1)

td.days
td.seconds
td.microseconds
td.total_seconds()

# Relative date and time (handles day of month and leap year conflicts)
d = date.today()
d + rd.relativedelta(years = 1)
d + rd.relativedelta(months = 1)
d + rd.relativedelta(days = 1)

# date and datetime to/from string
d.isoformat()
dt.isoformat()

# custom string format for date and datetime
dt = datetime.strptime('20240101_095555', '%Y%m%d_%H%M%S')
dt.strftime('%Y-%m-%d %H:%M:%S %z') # --> 2024-01-01 09:55:55 +0530
# Format: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# Date to datetime
dt = datetime.combine(d, datetime.min.time()) # combines date and time

# Timezones
from datetime import timezone

# Custom timezones
TZ_IST = timezone(timedelta(hours = 5, minutes = 30), name = 'IST custom')
TZ_PDT = timezone(-timedelta(hours = 7), name = 'PDT')

# Include timezone in datetime (by default, timezone is included but not timezone name)
dt = datetime.now(TZ_IST)
dt.tzname() # --> 'IST custom'

dt1 = dt.astimezone(TZ_PDT)

# Timezones with dateutil
dt = datetime.now(tz.UTC)
dt = datetime.now(tz.tzlocal())


### time ###
from time import sleep

sleep(5) # in seconds


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
data = [['hello'], ['bye']]
with output_file.open('w') as f:
  for d in data:
    f.write(d)


### concurrent ###
from concurrent.futures import ThreadPoolExecutor, as_completed, wait # also ProcessPoolExecutor

def process_data(a, b):
  return a + b

def finished(fut):
  print("Done!")

# Single future
with ThreadPoolExecutor() as executor:
  fut = executor.submit(process_data, 1, 2)
  fut.add_done_callback(finished) # callback won't bother with exceptions if result is not read

  fut.cancel() # returns attempted cancellation result
  fut.done() # True if completed or cancelled

  res = fut.result(timeout = 3) # optional timeout in seconds, default None

  fut.exception(timeout = 3) # returns None if no exception

# Multiple futures
with ThreadPoolExecutor(max_workers = 5) as executor: # max_workers NUM_CPU * 5 by default
  futs = [executor.submit(process_data, i, 1) for i in range(10)]

  # Get results as they are completed (not in order, already completed first)
  results = [f.result() for f in as_completed(futs, timeout = 3)]

  # Wait for all/any tasks to finish first
  # return_when in ['FIRST_COMPLETED', 'FIRST_EXCEPTION', 'ALL_COMPLETED'], default ALL_COMPLETED
  wait(futs, timeout = 3, return_when = 'ALL_COMPLETED')
  results = [f.result() for f in futs]


### urllib ###
from urllib import request

url = "https://doesnotexist.com"
page = request.urlopen(url)
text = page.read().decode('utf-8')


### regexp ###
import re

pat = r'^[HA].+\.xls.*' # always use raw strings

# These return re.Match or None
m = re.match(pat, "Hello.xls") # Prefix match (only match with beginning of string)
s = re.search(pat, "Hello.xls") # Search for any match in string
fm = re.fullmatch(pat, "Hello.xls") # Search for a full string match

# Working with re.Match
# TODO

# Compilation
rpat = re.compile(pat) # returns re.Pattern, compilation not necessary for performance
rpat.search("Hello.xls") # same as re.search(pat, "Hello.xls")

# Utility methods
pat = r'[XY12]+'

# These return lists
fa = re.findall(pat, "YAXBYXC21") # --> ['Y', 'X', 'YX', '21']
parts = re.split(pat, "YAXBYXC21") # --> ['', 'A', 'B', 'C', '']

# These return a string
sub = re.sub(pat, r'A', "X1B3YXA") # --> "ABAA"

# Escaping a string for match
re.escape(".*\n.*") # escaped version of pattern with \\ \. \* etc


### csv ###
from csv import DictReader, DictWriter

# Read a CSV
csv_data = []
with open('in_file.csv', newline = '') as csv_file:
  reader = DictReader(csv_file, fieldnames = ['date', 'count'], restval = 'NA', dialect = 'excel')
  # fieldnames is optional and will ignore first row (read it as data)
  # restval is optional and will be filled for missing values (if fieldnames is provided)
  # dialect can be 'excel': \n for end-of-line and field names in quotes (e.g. "date")

  for row in reader:
    csv_data.append(row) # row is a dict of fields to values

# Write a CSV
fieldnames = ['date', 'count']
with open('out_file.csv', 'w', newline = '') as csv_file:
  writer = DictWriter(csv_file, fieldnames = fieldnames, restval = 'NA', dialect = 'excel')

  writer.writeheader()
  for row in csv_data:
    writer.writerow(row)


### xml ###
from xml.etree import ElementTree as ET

# Read and parse an XML file
xml_file = 'my_data.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

for node in root:
  node.tag
  node.attrib # returns a dict of attributes
  node.text
  node.get('ATTR1') # read an attribute

root.find('TAG1') # returns first child with tag TAG1

for node in root.findall('TAG1'):
  pass

# Edit and write an XML file

node = ET.Element('TAG2')
child = ET.SubElement(node, 'TAG3')
node.remove(child)

# all written values and attributes must be text
node.text = '100'
node.set('ATTR1', 'attr_val')

# Print a node
ET.dump(node)

# Write a tree
tree.write('out_data.xml')

new_tree = ET.ElementTree(root)
new_tree.write('out_data.xml')


### pickle ###
import pickle

with open(filename, 'wb+') as f:
  pickle.dump(data, f)

with open(filename, 'rb') as f:
  data = pickle.load(f)


### json ###
import json

class ClassSerializer(json.JSONEncoder):
  def default(self, o):
    if type(o).__name__ == 'ContainerA':
      return o.field1
    if type(o).__name__ == 'ContainerB':
      return o.field2

json.dumps(data, cls = ClassSerializer, \
          indent = 2, sort_keys = True)
