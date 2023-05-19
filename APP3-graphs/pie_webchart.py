import justpy as jp 
import pandas

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

num = data.groupby(["Course Name"])["Rating"].count()
#print(dict(num))
chart_def = """
{
  chart: {
    plotBackgroundColor: null,
    plotBorderWidth: null,
    plotShadow: false,
    type: 'pie'
  },
  title: {
    text: 'Browser market shares in January, 2018'
  },
  tooltip: {
    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
  },
  accessibility: {
    point: {
      valueSuffix: '%'
    }
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
      }
    }
  },
  series: [{
    name: 'Brands',
    colorByPoint: true,
    data: [{
      name: 'Chrome',
      y: 61.41,
      sliced: true,
      selected: true
    }, {
      name: 'Internet Explorer',
      y: 11.84
    }, {
      name: 'Firefox',
      y: 10.85
    }, {
      name: 'Edge',
      y: 4.67
    }, {
      name: 'Safari',
      y: 4.18
    }, {
      name: 'Sogou Explorer',
      y: 1.64
    }, {
      name: 'Opera',
      y: 1.6
    }, {
      name: 'QQ',
      y: 1.2
    }, {
      name: 'Other',
      y: 2.61
    }]
  }]
}
"""

def app():
    webp = jp.QuasarPage()
    h1 = jp.QDiv(a=webp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-lg")                  
    p1 = jp.QDiv(a=webp, text="Graphs representing course reviews analysis", 
    classes="text-weight-bold text-left q-px-md")

    chart = jp.HighCharts(a=webp, options=chart_def)
    chart.options.title.text = "Graph of Number of Ratings by Course"
  
    #chart.options.series[0].data = [{"name":v1, "y":v2} for v1,v2 in zip(num.index,list(num))]

    return webp

jp.justpy(app)