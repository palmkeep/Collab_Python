# =========================================================================
#  The Calendar - Functional and imperative programming in Python
#
#  Module: output.py
#  Updated: 2004-07-30 by Peter Dalenius
#   Translated to Python in 2012 by Peter L-G
#   Translated to English in 2013 by Anders M.L.
#  Dependencies:
#   calendar_ADT.py
# =========================================================================

from calendar_ADT import *

## =========================================================================
##  1. Printing simple datatypes
## =========================================================================

def show_hour(h):
    "hour ->"
    print(get_integer(h), end='')


def show_minute(m):
    "minute ->"
    print(get_integer(m), end='')


def show_day(d):
    "day ->"
    print(day_number(d), end='')


def show_month(m):
    "month ->"
    print(month_name(m), end='')


def show_subject(s):
    "subject ->"
    print(subject_text(s), end='')


## =========================================================================
##  2. Printing compound datatypes
## =========================================================================

def show_duration(tr):
    "duration ->"
    print('{0} hours, {1} minutes'.format(get_integer(get_hour(tr)), get_integer(get_minute(tr))))


def show_time(t):
    "time ->"
    print('{0}:{1}'.format(str(get_integer(get_hour(t))).zfill(2),
                           str(get_integer(get_minute(t))).zfill(2)), end='')

def show_span(ts):
    "time span ->"
    show_time(start_time(ts))
    print('-', end='')
    show_time(end_time(ts))


def show_date(d):
    "date ->"
    show_day(get_day(d))
    print(' ', end='')
    show_month(get_month(d))


def show_appointment(app):
    "appointment ->"
    show_span(get_span(app))
    print(' ', end='')
    show_subject(get_subject(app))


def show_calendar_day(cal_day):
    "calendar_day ->"
    
    def show_cal_day_internal(mt):
        show_appointment(mt)
        print()
    
    for_each_appointment(cal_day, show_cal_day_internal)


## =========================================================================
##  3. Miscellaneous output functions
## =========================================================================

def show_day_heading(d, m):
    "day x month ->"
    s = '{0} {1}'.format(day_number(d), month_name(m))
    print(s)
    print('='*len(s))
