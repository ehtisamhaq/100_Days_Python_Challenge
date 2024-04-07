year = int(input("Provide your favorite year: "));

""" Each day has 24 hours.
    Each hour has 60 minutes.
    Each minute has 60 seconds. """

one_day = 60*60*24

result = one_day*365
is_leap_year = 0

if (year % 400 == 0) and (year % 100 == 0):
    is_leap_year = "{0} is a leap year".format(year)
    result += one_day
elif (year % 4 == 0) and (year%100 != 0):
    is_leap_year = "{0} is a leap year".format(year)
    result += one_day


print({result, year, is_leap_year})