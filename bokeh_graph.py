"""
#plotting basic bokeh graph

from bokeh.plotting import figure
from bokeh.io import show, output_file
import pandas

#output file
output_file("first_graph.html")

#data
data = pandas.read_excel("verlegenhuken.xlsx", sheet_name="Ark1")
x = data["Temperature"]/10
y = data["Pressure"]/10

#object of figure class
f = figure()
f.title.text = "Temperature and Air Pressure"
f.xaxis.axis_label = "Temperature(C)"
f.yaxis.axis_label = "Pressure(hPa)"

#plot
f.diamond_dot(x,y)

show(f)
"""

from bokeh.plotting import figure
from bokeh.io import show, output_file
import pandas

data = pandas.read_csv("adbe.csv", parse_dates=["Date"])                    #to read csv file column in date format

x_axis = data["Date"]
y_axis = data["Close"]

f = figure(height=500, width=1500, x_axis_type = "datetime")

f.xaxis.axis_label = "Date"
f.yaxis.axis_label = "Close"

f.line(x_axis, y_axis, color = "blue", alpha = 0.2)
output_file("Bokeh_date.html")
show(f)