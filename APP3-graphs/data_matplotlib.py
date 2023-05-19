import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])                    #parsing datetime column so that data under that column is considered as dates and times and not ordinary strings

#print(data.shape)                               #no. of rows and columns in data
#print(data['Comment'])                          #to print/access a single column
#print(data[['Comment', 'Rating']])                #to print/access multiple columns
#print(data.iloc[1:4])                           #to print/access multiple rows
#print(data.iloc[2])                             #to print/access single row
#print(data[['Rating', 'Comment']].iloc[1:4])                  #to print/access a section of data
#print(data.at[2, 'Rating'])                          #to print/access a cell


d1 = data[data['Rating'] >= 4.5]                    #filtering data as per 1 condition
print(d1)
d2 = data[(data['Rating'] >= 4.5) & (data['Comment'] != 'None')]            #filtering as per multpile conditions
#print(d2)

d3 = data[(data['Timestamp'] > datetime(2020, 7, 1, tzinfo=utc)) & (data['Timestamp'] < datetime(2020, 12, 31, tzinfo=utc))]        #tzinfo for declaring date time format and zone
#print(d3)

data['Day'] = data['Timestamp'].dt.date                     #creating column(or rather index) and storing date(extracted from Timestamp column) in it
day_avg = data.groupby(["Day"]).mean()                      #grouping ratings by day
#print(day_avg)                                             #Day is not column but an index

plt.figure(figsize=(25,3))                                  #setting plot dimensions(length, height)
plt.plot(day_avg.index, day_avg['Rating'])                  #making plot(x axis, y axis)


#downscaling to week and month

data['Week'] = data["Timestamp"].dt.strftime("%Y %U")           #strftime - string from time, %Y for year, %m for month, %U for week, %A for day
week_avg = data.groupby(["Week"]).mean()

data['Month'] = data["Timestamp"].dt.strftime("%Y %m")
month_avg = data.groupby(["Month"]).mean()

plt.figure(figsize=(25,3))                                  
plt.plot(week_avg.index, week_avg['Rating'])

plt.figure(figsize=(25,3))                                
plt.plot(month_avg.index, month_avg['Rating'])

#averaging by two data columns

data['Month'] = data["Timestamp"].dt.strftime("%Y %m")
month_avg_courses = data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()           #if we remove rating then other column will be included
month_avg_courses.plot(figsize=(25,8))
#print(month_avg_courses)

#on which day people are the happiest?(day with highest rating)

data["Week day"] = data["Timestamp"].dt.strftime("%A")                      #extracting days
data["Day number"] = data["Timestamp"].dt.strftime("%w")                    #%w for extracting day numbers(Sunday - 0, etc) 

week_avg = data.groupby(["Week day", "Day number"]).mean()
week_avg = week_avg.sort_values("Day number")                               #sorting as per day number so that we get days in order

plt.figure(figsize=(15,3))
plt.plot(week_avg.index.get_level_values(0), week_avg["Rating"])                                #since week_avg has 2 indexes-Day number and Week day, so we use get_levels_values to get only the week days(Week day index)
#print(week_avg.index)                                                               #to check the indexes and their position
#print(week_avg)