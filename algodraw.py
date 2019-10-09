#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import drange, SUNDAY
from algolist import getPracticeNumber
import datetime
import numpy as np

###################### 
### Initialize
######################
FILE_PREFIX     = "statistics"
FILE_STATISTICS = FILE_PREFIX + ".log"
FILE_IMAGE      = FILE_PREFIX + ".png"
DATE_FORMATTER = "%Y-%m-%d"
dates = []
values = []
latest_date = ""

###################### 
### Write to file  
######################
def write(today_date, today_value):
    f = open(FILE_STATISTICS, "a+")
    f.write(str(today_date) + "   " + str(today_value) + "\n")
    f.close()

###################### 
### Draw the graph   
######################
def draw(dates, values):
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics")

    xfmt = mdates.DateFormatter("%m/%d")
    #xloc = mdates.WeekdayLocator(SUNDAY)
    xloc = mdates.DayLocator()
    ax.xaxis.set_major_formatter(xfmt)
    ax.xaxis.set_major_locator(xloc)
    ax.grid(True)
    ax.set_xlim(datetime.datetime(2019,10,1), datetime.datetime(2019,10,31)) 
    ax.set_ylim(50,100) 

    plt.plot_date(dates, values, '-', marker='o')
    plt.yticks(np.arange(50, 100, step=5))
    plt.gcf().autofmt_xdate()  
    #plt.show()
    plt.savefig(FILE_IMAGE)

###################### 
### Read from file  
######################
def read(dates, values):
    f = open(FILE_STATISTICS, "r")
    line = f.readline()
    while line != '':  # The EOF char is an empty string
        split_line = line.split()
        date_str, val_str = split_line[0], split_line[1]
        #print(date_str, " -- ", val_str)
        dates.append(datetime.datetime.strptime(date_str, DATE_FORMATTER)) 
        values.append(int(val_str))
        line = f.readline()
    f.close()

# print("Today  date: ", today_date, "")
# print("Latest date: ", latest_date, "")

###################### 
### Read today info 
######################
print(">> App algodraw.py starts")
today_date = datetime.date.today()
today_value = getPracticeNumber()
print(">> Read today info: (date =", today_date, ", value =", today_value, ")")

print(">> Read from files:", FILE_STATISTICS)
read(dates, values)
latest_date = dates[-1].strftime(DATE_FORMATTER)


if str(today_date) != str(latest_date): 
    print(">> Status : Not updated yet (latest = ", latest_date, ", today = " ,today_date, ")") 
    print(">> Write the following today's data into log.")
    print(">> New log: \"" + str(today_date) + "   " + str(today_value), "\"")
    write(today_date, today_value)
    dates.append(today_date) 
    values.append(today_value)
else:
    print(">> Status: Already updated.")

print(">> Save the image:", FILE_IMAGE)
draw(dates, values)