# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ShnC-tX3A6HNgLb9wiXy2D0cZnr-oP7H
"""

# variable vs. value: 1-on-1
lucky_num_0 = 7
lucky_num_1 = 24
lucky_num_2 = 5566

# variable vs. values: 1-on-multiple
lucky_numbers = [7, 24, 5566]

# variable vs. value: 1-on-1
sat = "Saturday"
sun = "Sunday"

# variable vs. values: 1-on-multiple
weekend = ["Saturday", "Sunday"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print(type(lucky_numbers))

print(type(weekend))

print(type(weekdays))

print(len(lucky_numbers))
print(len(weekend))
print(len(weekdays))

my_fav_weekday = "Friday"
print("My favorite weekday is {}.".format(my_fav_weekday))

# why not: format("My favorite weekday is {}.", my_fav_weekday) ?

help(append)

print(lucky_numbers)
lucky_numbers.append(87)
print(lucky_numbers)

print(lucky_numbers)
lucky_numbers.pop()
print(lucky_numbers)

my_fav_group = lucky_numbers.pop()
print(lucky_numbers)
print(my_fav_group)

print(weekdays)
print(weekend)

weekdays + weekend

weekend + weekdays

print(weekdays[0])
print(weekdays[1])
print(weekdays[2])
print(weekdays[3])
print(weekdays[4])

i = 0
while i < 5:
    print(weekdays[i])
    i += 1

i = 0
while i < 2:
    print(weekend[i])
    i += 1

i = 0
while i < len(weekend):
    print(weekend[i])
    i += 1

i = 0
while i < len(weekdays):
    print(weekdays[i])
    i += 1

print(weekdays[-1])
print(weekdays[-2])
print(weekdays[-3])
print(weekdays[-4])
print(weekdays[-5])

i = -1
while i >= -5:
    print(weekdays[i])
    i -= 1

weekdays

weekdays[0:3:1]

weekdays[0:5:2]

weekdays[::2]

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.imdb.com/title/tt4154796/')
soup = BeautifulSoup(response.text)

cast_list_a = soup.select("#titleCast .loadlate")
print(len(cast_list_a))

cast_list = []
print(cast_list)
print(type(cast_list))
print(len(cast_list))

actor_0 = cast_list_a[0].get('alt').strip()
cast_list.append(actor_0)
print(cast_list)

actor_1 = cast_list_a[1].get('alt').strip()
cast_list.append(actor_1)
print(cast_list)

cast = []
print(cast)
print(type(cast))
print(len(cast))

i = 0
while i < len(cast_list_a):
    actor = cast_list_a[i].get('alt').strip()
    cast.append(actor)
    i += 1

print(cast)

#cast = ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Don Cheadle', 'Paul Rudd', 'Benedict Cumberbatch', 'Chadwick Boseman', 'Brie Larson', 'Tom Holland', 'Karen Gillan', 'Zoe Saldana', 'Evangeline Lilly']

print(cast[8])
print(cast[-7])

print(len(cast))
print(cast[:6])

import pandas as pd

time_series_df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
cumulative_confirmed = list(time_series_df[time_series_df['Country/Region'] == 'Taiwan*'].values.ravel()[4:].astype(int))
cumulative_confirmed_lag = list(time_series_df[time_series_df['Country/Region'] == 'Taiwan*'].values.ravel()[4:].astype(int))
print(cumulative_confirmed)
print(cumulative_confirmed_lag)

print(len(cumulative_confirmed))
print(cumulative_confirmed[-1])

cumulative_confirmed_lag.insert(0, 0)
print(len(cumulative_confirmed_lag))
print(cumulative_confirmed_lag[0])

cumulative_confirmed_lag.pop()
print(len(cumulative_confirmed_lag))
print(cumulative_confirmed_lag[-1])

print(cumulative_confirmed)
print(cumulative_confirmed_lag)

daily_increase = []

#daily_increase = ?
day0_increase = cumulative_confirmed[0] - cumulative_confirmed_lag[0]
print(day0_increase)
daily_increase.append(day0_increase)

day1_increase = cumulative_confirmed[1] - cumulative_confirmed_lag[1]
print(day1_increase)
daily_increase.append(day1_increase)

day2_increase = cumulative_confirmed[2] - cumulative_confirmed_lag[2]
print(day2_increase)
daily_increase.append(day2_increase)

daily_increase

day106_increase = cumulative_confirmed[106] - cumulative_confirmed_lag[106]
print(day106_increase)

daily_increase = []
i = 0
while i < 107:
    dayn_increase = cumulative_confirmed[i] - cumulative_confirmed_lag[i]
    print("Day {}: 每日新增確診人數 {}".format(i, dayn_increase))
    daily_increase.append(dayn_increase)
    i += 1

print(len(daily_increase))
print(daily_increase[:10])
print(daily_increase[-10:])