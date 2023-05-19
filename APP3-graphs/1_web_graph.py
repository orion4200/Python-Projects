import justpy as jp
import pandas
from datetime import datetime

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])          #loading csv file

data['Day'] = data['Timestamp'].dt.date 
day_avg = data.groupby(["Day"]).mean()

#highcharts json file(copied from Highcharts website)
chart_def = """                                               
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x}: {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Average Rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""

def app():
    webp = jp.QuasarPage()                                                                       
    h1 = jp.QDiv(a=webp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-lg")                  
    p1 = jp.QDiv(a=webp, text="Graphs representing course reviews analysis", classes="text-weight-bold text-left q-px-md")  
    chart = jp.HighCharts(a=webp, options=chart_def)                #converts highcharts java script to a pyhton readable format(dict)
    #print(type(chart_def))
    #print(type(chart.options))
    #print(chart.options)
    chart.options.title.text = "Graph of Average Rating by Day"

    chart.options.xAxis.categories = list(day_avg.index)
    #chart.options.series[0].data = list(zip(x,y))                    #format for assigning x and y axis values
    chart.options.series[0].data = list(day_avg["Rating"])            #accessing series key in the dict
    return webp

jp.justpy(app) 