import justpy as jp 
import pandas

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Month'] = data["Timestamp"].dt.strftime("%Y %m")
month_avg = data.groupby(data["Month"]).mean()

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Average Rating by Month'
  },
  subtitle: {
    text: 'According to Ardit sir'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Month'
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
    p1 = jp.QDiv(a=webp, text="Graphs representing course reviews analysis", 
    classes="text-weight-bold text-left q-px-md")

    chart = jp.HighCharts(a=webp, options=chart_def)
    chart.options.title.text = "Graph of Average Rating by Month"
    chart.options.xAxis.categories = list(month_avg.index)
    chart.options.series[0].data = list(month_avg["Rating"])

    return webp

jp.justpy(app)