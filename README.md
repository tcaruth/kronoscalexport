kronoscalexport
===============
Requires:
[lxml], [requests]

Rips dates from logged in user at https://kronos-wfc.trinity-health.org/wfc/ and exports them to csv, or gcal

does do some redundant downloading, but its because i dont want to mess with https in urllib2


Notes previously found in main.py
 reportindex chooses what we're grabbing
 1 = MY ACCRUAL BALANCES AND PROJECTIONS
 2 = SCHEDULE
 3 = TIME DETAIL

 timeframeindex chooses how far to look
 1 = Current Pay Period
 2 = Next Pay Period
 3 = Previous Schedule Period
 4 = Current Schedule Period
 5 = Next Schedule Period
 6 = Week to Date
 7 = Last Week
 8 = Yesterday
 9 = Range of Dates, requires bd and ed to be declared
 10 = lists as null. likely the seperator in the dropdown(-----). seems to replicate 9?
 11 = Specific Date. same as using same bd ed with time frame 9
 12 = same as 10. lists as null
 13 = Today
 14+ = all seem to be able to be used as 9