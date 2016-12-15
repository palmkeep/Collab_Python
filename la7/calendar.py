
# =========================================================================
#  The Calendar - Functional and imperative programming in Python
#
#  Module: calendar.py
#  Updated: 2004-11-10 by Peter Dalenius
#    Translated to Python in 2012 by Peter L-G
#    Translated to English in 2013 by Anders M.L.
#    Added typesignatures in 2016 by Henning N.
#  Dependencies:
#    calendar_ADT.py
#    booking.py
#    output.py
# =========================================================================

# This module ties the calendar together. It contains the functions 
# that users interact with, and the global dictionary where all 
# calendars are stored.

# Functions in this file never delve deeper into the representation of the 
# calendar objects, or the internal logic of actually booking an appointment,
# are available in separate modules. These are imported automatically upon the
# import of the calendar module.

# The files have the following dependencies:

#
#               calendar.py
#                   |
#           +_______+________+
#           |                |
#      booking.py      output.py
#           |                |
#           +_______+________+ 
#                   |
#              calendar_ADT.py


from calendar_ADT import *
from booking import *
from output import *
import pickle;

# =========================================================================
#  1. Storing and fetching calendars
# =========================================================================
calendars = dict();

def fetch_calendar(cal_name):
    "String -> calendar_year"
    if calendar_exists(cal_name):
        return calendars[cal_name]
    else:
        raise Exception("There is no calendar_year by the name {0}.".format(cal_name))


def insert_calendar(cal_name, cal_year):
    "String x calendar_year -> "
    calendars[cal_name] = cal_year


def calendar_exists(cal_name):
    "String -> Bool"
    return cal_name in calendars


def new_calendar(cal_name):
    "String ->"
    calendars[cal_name] = new_calendar_year()


# Saves all calendars to file. The data is wrapped in [*CALFILE2000*, ...] which is
# used as a tag for identifying calendar files.
def save_calendars(filename):
    "String ->"
    output = open(filename, 'wb')
    pickle.dump(['*CALFILE2000*', calendars], output)
    output.close()

# Loads calendar from a file. If the file does not exist, or is malformed,
# the calendars remain as they are.

# The file to be loaded is assumed to be non-hostile (cf the warning in the Pickle 
# module documentation http://docs.python.org/3/library/pickle.html ).

def load_calendars(filename):
    "String -> Bool"
    try:
        pkl_file = open(filename, 'rb')
        file_content = pickle.load(pkl_file)
        pkl_file.close()
        if isinstance(file_content, list) and\
         len(file_content) == 2 and\
         file_content[0] == '*CALFILE2000*':
            global calendars
            calendars = file_content[1]
            return True
        else:
            return False
    except IOError:
        return False


# =========================================================================
#  2. User interface
# =========================================================================

def create(cal_name):
    "String ->"
    if calendar_exists(cal_name):
        print("A calendar by the name {0} already exists.".format(cal_name))
    else:
        new_calendar(cal_name)
        print("A new calendar by the name {0} has been created.".format(cal_name))


def show_calendars():
    "->"
    if calendars:
        print("The following calendars exist:")
        for cal_name in calendars:
            print(cal_name)
    else:
        print("No calendars have been created.")


def book(cal_name, d, m, t1, t2, subject_text):
    "String x Integer x String x String x String x String ->"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    end = convert_time(t2)
    subject = new_subject(subject_text)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    
    new_date(day, mon) # Ensure that the date is proper
    
    if precedes(end, start):
        print("Invalid appointment time (wrong order of start and finish).")
    elif is_booked(cal_day, new_time_span(start, end)):
        print("The proposed time is already taken.")
    else:
        insert_calendar(cal_name, book_appointment(fetch_calendar(cal_name),
                                          day, mon, start, end, subject))
        print("The appointment has been booked.")

#
#
#
def remove(cal_name, d, m, start):
    if ():
        print("Appointment removed.")
    else:
        print("No appointment booked at that time.")
#
#
#

def show(cal_name, d, m):
    "String x Integer x String ->"
    day = new_day(d)
     mon = new_month(m)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    
    new_date(day, mon) 			# Ensure that the date is proper
    
    if is_empty_calendar_day(cal_day):
        print("No appointments this day.\n")
    else:
        show_day_heading(day, mon)
        show_calendar_day(cal_day)


def save(filename):
    "String ->"
    save_calendars(filename)
    print("The calendars have been saved to {0}.".format(filename))


def load(filename):
    "String ->"
    if load_calendars(filename):
        print("New calendars have been loaded.")
    else:
        print("The file does not exist, or it is devoid of saved calendars.")

        
def help():
    "->"
    print('The Calendar. \n\n')
    print('-'*50)
    print('A quick reminder of your options:')
    print('  create(name)')
    print('  book(name, day, month, time, subject)')
    print( ' show(name, day, month)')
    print( ' save(filename)')
    print( ' load(filename)')

def show_free(calendar_name, day, month, start_time, end_time):
    calendar = fetch_calendar(calendar_name)
    print(calendar)

