import justpy as jp
import pandas
from datetime import datetime

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])

data['Month'] = data["Timestamp"].dt.strftime("%Y %m")
month_avg_crs = data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()

l = [{"name":v1, "data":[v2 for v2 in month_avg_crs[v1]]} for v1 in month_avg_crs.columns]
#print(l)
print(month_avg_crs['Interactive Data Visualization with Python and Bokeh'])
chart_def = """
{
  chart: {
    type: 'spline'
  },
  title: {
    text: 'Average Rating by Month And Course'
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    verticalAlign: 'top',
    x: 150,
    y: 50,
    floating: false,
    borderWidth: 1,
    backgroundColor:
        '#FFFFFF'
  },
  xAxis: {
    categories: [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday'
    ],
    plotBands: [{ // visualize the weekend
      from: 4.5,
      to: 6.5,
      color: 'rgba(68, 170, 213, .2)'
    }]
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    }
  },
  tooltip: {
    shared: true,
    valueSuffix: ' units'
  },
  credits: {
    enabled: false
  },
  plotOptions: {
    areaspline: {
      fillOpacity: 0.5
    }
  },
  series: [{
    name: 'John',
    data: [3, 4, 3, 5, 4, 10, 12]
  }, {
    name: 'Jane',
    data: [1, 3, 4, 3, 3, 5, 4]
  }]
}
"""

def app():
    webp = jp.QuasarPage()
    h1 = jp.QDiv(a=webp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-lg")                  
    p1 = jp.QDiv(a=webp, text="Graphs representing course reviews analysis", 
    classes="text-weight-bold text-left q-px-md")

    chart = jp.HighCharts(a=webp, options=chart_def)

    chart.options.xAxis.categories = list(month_avg_crs.index)
    chart.options.series = [{"name":v1, "data":[v2 for v2 in month_avg_crs[v1]]} for v1 in month_avg_crs.columns]
    
    return webp

jp.justpy(app)