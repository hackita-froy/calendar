import bottle
import calendar
import os
import datetime
import my_history
import my_overrides


__author__ = 'David Fradis'

PORT = int(os.environ.get("PORT", 5000))

cal = my_overrides.SelectableCalendar()

def navigate(year, month):
  return {
    'past_month': month % 13 -1 or 12,
    'past_year': year - (1 if month == 1 else 0),
    'next_month': month % 12 + 1,
    'next_year': year + month // 12,
    'current_year': year,
    'curent_month': month
  }

def render_history(month, day):
  selected_death = my_history.get_historic_death(month, day)
  return selected_death

@bottle.route('/static/<filename>')
def server_static(filename):
  return bottle.static_file(filename, root='./static')

@bottle.route('/')
@bottle.route('/<year:int>/<month:int>')
@bottle.route('/<year:int>/<month:int>/<day:int>')
def render_calendar(year=None, month=None, day=None ):
  now = datetime.datetime.now()
  if year is None:
    year = now.yer
  if month is None:
    month = now.month
  if day is None:
    day = now.day

  return bottle.template('monthly_calendar', calendar=cal.formatmonth(year, month),
    **navigate(year,month), **render_history(month, day))

@bottle.route('/<year>')
def render_yearly_calendar(year=now.year):
  year = int(year)
  return bottle.template('yearly_calendar', calendar=cal.formatyear(year, 3))

bottle.run(host='0.0.0.0', port=PORT, debug=True)
