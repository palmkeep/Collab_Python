# =========================================================================
#  The Calendar - Functional and imperative programming in Python
#
#  Modul: booking.py
#  Updated: 2004-07-30 av Peter Dalenius
#  	Translated to Python 2012 by Peter L-G
#	Translated to English 2013 by Anders M.L.
#
#  Dependencies:
#    calendar_ADT.py
# =========================================================================

# This module contains lower-level calculations and functions for booking 
# appointments, finding unallocated time etc. Functions here never
# operate directly on Python objects, but rather go through the primitives
# and functions provided in calendar_ADT.

from calendar_ADT import *

# =========================================================================
#  1. Identifying calendar contents
# =========================================================================

# Check if any meeting in the provided calendar day collides with the 
# proposed time span.
def is_booked(cal_day, ts):
    "calendar_day x time span -> Bool"
    return some_meeting_satisfies(
        cal_day,
        lambda app: are_overlapping(ts, get_span(app))) 


# Does any appointment that given day start at a specific time?
def is_booked_from(cal_day, t):
    "calendar_day x time -> Bool"
    return some_meeting_satisfies(
       cal_day,
       lambda app: is_same_time(t, start_time(get_span(app))))

# -----
# TODO: Komplettering 3 & 4
# -----
def free_spans(cal_day, start, end):
    "time span x times spans -> timespans"
    time_spans = new_time_spans()
    time_spans= insert_all_spans_from_day(cal_day, time_spans)
    ts_range = new_time_span(start, end)
    final_spans = new_time_spans()

    """
    def free_span(ts):
        if not ts[1:]:#is_empty(rest_spans(ts))
            return [] #new_ts
        elif not are_overlapping(ts[0], ts[1]) and are_overlapping(ts[0], ts_range) and are_overlapping(ts[1], ts_range):
            return [new_time_span(end_time(ts[0]), start_time(ts[1]))] + free_span(ts[1:])
        else:
            return free_span(ts[1:])
    """
    
    def free_span(ts, fts):
        "Comment goes here"
        if is_empty_time_spans(rest_spans(ts)):
            return fts
        elif not are_overlapping(first_span(ts), first_span(rest_spans(ts))) and are_overlapping(first_span(ts), ts_range) and are_overlapping(first_span(rest_spans(ts)), ts_range):
            st = end_time(first_span(ts))
            et = start_time(first_span(rest_spans(ts)))
            timespan = new_time_span(st, et)
            print(timespan)
            ensure(timespan, is_time_span)
            fts = insert_span(timespan, fts)
            return free_span(rest_spans(ts), fts)
        else:
            return free_span(rest_spans(ts), fts)

    #!#!#   Vet inte om vi tillåts att strip'a bort tagen i booking.py :/
    #       Kommer du på något bra sätt att komma runt detta
    #       Koden ovanför är i princip din kod men istället för att direkt
    #       skapa en lista med spans så använder den sig av tim_spans grejerna
    for span in strip_tag(free_span(time_spans, final_spans)):
        final_spans = insert_span(span, final_spans)
        
    
    if precedes(start_time(ts_range),start_time(first_span(time_spans))):
        final_spans = insert_span(new_time_span(start_time(ts_range), start_time(first_span(time_spans))), final_spans)

    if not precedes(end_time(ts_range),end_time(last_span(time_spans))):
        final_spans = insert_span(new_time_span(end_time(last_span(time_spans)), end_time(ts_range)), final_spans)

    if not are_overlapping(first_span(time_spans), ts_range) and is_empty_time_spans(final_spans):
        final_spans = insert_span(ts_range, final_spans)
   
    return final_spans


# =========================================================================
#  2. Making and removing appointments
# =========================================================================
# Adds a new appointment by taking apart a calendar year, inserting the
# appointment into the correct calendar day, and then putting it back together.

# This function does not modify any structures, but rather builds a new one.
# The new calendar year generated by book_appointment is used to replace the 
# old one. This replacement is done by the function book (calendar.py) which 
# invokes book_appointment.

def book_appointment(cal_year, day, mon, start, end, subject):
    "calendar_year x day x month x time x time x subject -> calendar_year"
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    app = new_appointment(new_time_span(start, end), subject)
    return insert_calendar_month(
               mon,
               insert_calendar_day(
                   day,
                   insert_appointment(app, cal_day),
                   calendar_month(mon, cal_year)),
               cal_year)


# #!#
#
#
# -----
# TODO: Komplettering 4
# Comment:  Believe this might be a leftover from previous komp. since the
#           longest row here is at 62 characters.
# -----
def unbook_appointment(cal_year, day, mon, start):
    "calendar_year x day x month x time -> calendar_year"
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    cal_mon = calendar_month(mon, cal_year)
    # get the hour and minute of $start and increment to create $end
    return insert_calendar_month(
                mon,
                insert_calendar_day(
                    day,
                    remove_appointment(start, cal_day),
                    calendar_month(mon, cal_year)),
                cal_year)
#
#
#


