#This is only tested data of graphs
import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['40', '80', '30', '10'],
    mode='lines',
    line=dict(
        width=0.5
    ),
    fill='tonexty'
)
trace1 = go.Scatter(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['60', '90', '40', '20'],
    mode='lines',
    line=dict(
        width=0.5
    ),
    fill='tonexty'
)
trace2 = go.Scatter(
    x=['Winter', 'Spring', 'Summer', 'Fall'],
    y=['100', '100', '100', '100'],
    mode='lines',
    line=dict(
        width=0.5
    ),
    fill='tonexty'
)
data = [trace0, trace1, trace2]
layout = go.Layout(
    showlegend=True,
    xaxis=dict(
        type='category',
    ),
    yaxis=dict(
        type='linear',
        range=[1, 100],
        dtick=20,
        ticksuffix='%'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='stacked-area-plot')