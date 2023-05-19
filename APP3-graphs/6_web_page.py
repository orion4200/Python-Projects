import justpy as jp 
import pandas

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

data["Week day"] = data["Timestamp"].dt.strftime("%A")                      
data["Day number"] = data["Timestamp"].dt.strftime("%w")                   

week_avg = data.groupby(["Week day", "Day number"]).mean()
week_avg = week_avg.sort_values("Day number") 

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'On which day people are the happiest?'
  },
  subtitle: {
    text: 'According to Ardit sir'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Day'
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
      text: 'Happiness'
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
    name: 'Happiness',
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
    
    chart.options.xAxis.categories = list(week_avg.index.get_level_values(0))
    chart.options.series[0].data = list(week_avg["Rating"])

    return webp

jp.justpy(app)