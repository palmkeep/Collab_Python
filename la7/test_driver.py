# =========================================================================
#  Calendar - Functional and imperative programming in Python
#
#  Module: calendar_ADT.py
#  Created: 2008-10-07 by Peter Dalenius
#    Updated 2009-09-25 by Anders Haraldsson
#    Translated to Python in 2012 by Peter L-G
#    Translated to English in 2013 by Anders M.L.
#  Dependencies:
#    calendar_ADT.py
#    booking.py
#    output.py
# =========================================================================

from calendar import *

# The goal is to see if the free_spans function produces correct results.
# In order to automate the process of testing this, we provide a set of 
# functions that convert human-readable descriptions of appointments and 
# search spans during a day, into testable data.

# In the code below, we assume that the function that generates the set of 
# free time spans (a multiple time spans object) is called free_spans. It
# is also assumed to be invoked by free_spans(cal_day, start_time, end_time),
# in that order. You may need to modify your code to conform to this standard.

# You will also have to create additional test cases, and add to new_cases().
# No functions besides new_cases should be modified. You may need to check
# the names of functions concerning time_spans (in plural), so that your
# solution conforms to the given names.

# Note: technically, you only need to modify new_cases. You can scroll down
# to this function now.

# =========================================================================
#  1. Additional components
# =========================================================================

# The test suite takes human-readable descriptions of appointments and 
# free time spans, and converts them into data that is of use when testing
# free_spans (ie data of typ calendar day, and multiple time span).

# The calendar day is created by detour to spans.

# This function converts from the human-readable form ["13:15-15:00", ...] to 
# corresponding time span objects.
def convert_to_spans(seq):
    "[String] -> multiple time spans"
    if not seq:
        return new_time_spans()
    else:
        times = seq[0].split("-")
        return insert_span(new_time_span(
                       convert_time(times[0]),
                       convert_time(times[1])),
                   convert_to_spans(seq[1:]))


# To test the free_spans function, we need a calendar day. This function generates
# a day full of appointments corresponding to a given multiple time spans object.
def time_spans_to_calendar_day(mts):
    "multiple time spans -> calendar_day"
    ensure(mts, is_time_spans)
    if is_empty_time_spans(mts):
        return new_calendar_day()
    else:
        return insert_appointment(
                   new_appointment(first_span(mts), new_subject("Test")),
                   time_spans_to_calendar_day(rest_spans(mts)))


# Compare if two ordered sets of time spans (multiple time spans) are equal.
def is_same_time_spans(mts1, mts2):
    "multiple time spans x multiple time spans -> Bool"
    if is_empty_time_spans(mts1) and is_empty_time_spans(mts2):
        return True
    elif is_empty_time_spans(mts1) or is_empty_time_spans(mts2):
        return False
    elif is_same_span(first_span(mts1), first_span(mts2)):
        return is_same_time_spans(
                   rest_spans(mts1),
                   rest_spans(mts2))
    else:
        return False


# Compare if two spans are equal
def is_same_span(ts1, ts2):    
    "span x span -> Bool"
    ensure(ts1, is_time_span)
    ensure(ts2, is_time_span)
    return is_same_time(start_time(ts1), start_time(ts2)) and\
           is_same_time(end_time(ts1), end_time(ts2))


# =========================================================================
#  2. Building and using test cases
# =========================================================================

# Contains all test cases (the keys are the test case numbers).
test_cases = {}

# This function generates a single test case. 
# Input: case number, when the search interval starts and ends, a list of 
# appointment spans in text format (in the form "HH:MM-HH:MM"), and a similar
# list of expected results.

# The data generated is a test case (with a calendar day and a set of 
# expected time spans) that is added to the set of test cases.

def new_test_case(test_nr, start_str, end_str, booking_data, exp_result):
    "Integer x String x String x [String] x [String] ->" 
    start = convert_time(start_str)
    end = convert_time(end_str)
    cal_day = time_spans_to_calendar_day(
              convert_to_spans(booking_data))
    res_mts = convert_to_spans(exp_result)
    
    global test_cases
    
    test_cases[test_nr] = [start, end, cal_day, res_mts]


# This function goes through the added test cases and compares actual and expected output.
def run_tests():    
    all_ok = True
    cases = 0    
    for test_nr in test_cases:                
        cases += 1        
        current_case = test_cases[test_nr]        
        start = current_case[0]
        end = current_case[1]
        cal_day = current_case[2]
        expected_results = current_case[3]
        
        if not is_same_time_spans(
                free_spans(cal_day, start, end),
                expected_results):
            
            all_ok = False
            
            print("----")
            print("Test case {0} generates unexpected output.".format(test_nr))
            print("Free time spans:")
            show_time_spans(free_spans(cal_day, start, end))
            print()
            print("Expected:")
            show_time_spans(expected_results)
            print("----")
            print()
    
    if all_ok:
        print("All ({0}) test cases OK.".format(cases))


# Create test cases, and run tests.
def test_free_spans():
    new_cases()
    run_tests()


# =========================================================================
#  3. Building the list of test cases
# =========================================================================

# new_cases contains all human-readable test case specifications. When run, 
# it uses new_test_case to generate and insert the data converted for automated
# checking.

def new_cases():
    global test_cases
    
    test_cases = {}
    
    new_test_case(
        1,
        "08:00",                        # Search interval starts
        "21:00",                        # Search interval ends
        ["07:00-09:00", "13:00-18:00"], # This day's appointments
        ["09:00-13:00", "18:00-21:00"]) # Expected free time
    

    # -------- YOUR TEST CASES GO HERE -----------------------   
    # For each case, add a brief description of what you want to test.

    # if you have a couple, non-overlaping appointments scattered whitin the search interval.
    new_test_case(
        2, 
        "00:00",
        "23:59",
        ["06:30-09:00", "13:12-18:12"], 
        ["00:00-06:30", "09:00-13:12", "18:12-23:59"])
    
    #if you only have appointments that are outside the search intervall
    new_test_case(
        3, 
        "13:00",
        "16:00",
        ["06:30-09:00", "16:12-18:12"], 
        ["13:00-16:00"])

    #if you only have appointments that are partially outside the search intervall
    new_test_case(
        4, 
        "13:00",
        "16:00",
        ["06:30-13:30", "15:24-17:00"], 
        ["13:30-15:24"])

    #if you have overlapping appointments
    new_test_case(
        5, 
        "09:00",
        "18:00",
        ["10:00-15:00", "15:30-17:00"], 
        ["09:00-10:00", "17:00-18:00"])


# -----
# TODO: Komplettering 6
# -----
    
    
    print("Test cases generated.")

# Run the test cases by calling test_free_spans().
test_free_spans()
