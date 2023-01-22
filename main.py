import plotly.graph_objs as go
labels = ['Breakfast','Lunch','Dinner','Snacks']
values = [6,12,18,4]
data = go.Pie(labels=labels, values=values, hole=.3)
fig = go.Figure([data])

fig.write_html("piechart.html")

fig.show()