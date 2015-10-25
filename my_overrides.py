import calendar
class SelectableCalendar(calendar.HTMLCalendar):
  this_year = None
  this_month = None
  def formatday(self, day, weekday):
    """
      Return a day as a table cell.
    """
    if day == 0:
        return '<td class="noday">&nbsp;</td>' # day outside month
    else:
        return '<td class="%s"><a href="/%s/%s/%s">%d</a></td>' % (self.cssclasses[weekday],self.this_year,self.this_month,day, day)

  def formatmonth(self, theyear, themonth, withyear=True):
    self.this_year = theyear
    self.this_month = themonth
    return super(SelectableCalendar, self).formatmonth(theyear, themonth, withyear)
