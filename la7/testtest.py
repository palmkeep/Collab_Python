from calendar import *
from calendar_ADT import *

c1 = new_calendar("Viktor")
c2 = new_calendar("Andre")

book("Viktor", 12, "jan","12:30", "13:30", "Preform guard duties on yavin 4")
book("Viktor", 12, "jan","13:40", "13:50", "seperating ones from zeroes")
book("Viktor", 12, "jan","13:51", "13:55", "looking at all the lonely people")
book("Viktor", 17, "apr","15:30", "16:30", "Caluculating odds of sucssesfully navigating asteroid field")
book("Viktor", 17, "apr","13:40", "13:50", "Nerfing D.va")
book("Viktor", 20, "apr","11:59", "12:01", "it's high noon")


month = new_month("jan")
day = new_day(12)

day1 = (calendar_day(day,calendar_month(month,fetch_calendar("Viktor"))))


ts = new_time_spans()
ts = insert_all_spans_from_day(day1, ts)

print_time_spans(ts)

print("---------------------------------")

ts1= new_time_span(new_time(new_hour(1), new_minute(1)), new_time(new_hour(13), new_minute(50)))

#show_free("Viktor", 12, "jan","","" )
