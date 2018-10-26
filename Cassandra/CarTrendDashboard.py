import dash
import dash_core_components as dcc
import dash_html_components as html 
import plotly.graph_objs as go  
from dash.dependencies import Input,Output 
from datetime import datetime as dt
import json
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from datetime import date, datetime
import pandas as pd
from collections import OrderedDict
from datetime import date, timedelta

app=dash.Dash()
app.config['suppress_callback_exceptions']=True

final_list=[]
car_list=[]

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

#Connecting to Cassandra cluster
cluster = Cluster(['52.210.115.54'])
cassandra_session = cluster.connect()
cassandra_session.set_keyspace('majestic')

results = cassandra_session.execute("select s_model_code from model_code")
car_models=set()

for row in results:
    car_models.add(row[0])
    
app.layout=html.Div(children=[
    html.Div([dcc.Dropdown(
        id='car-model',
        options=[{'label':car,'value':car} for car in car_models],
        value='Select a Car Model'
    ),
    
    html.H4(id='segment')
    ],style={'width': '48%', 'display': 'inline-block'}),
    
    html.Div([dcc.DatePickerRange(
        id='date-picker', 
        start_date=dt(2017, 3, 3),
        end_date=dt(2018,3,7),
        end_date_placeholder_text='Select a date!'
    )],style={'width': '48%','float': 'right','display': 'inline-block'}),
    
    dcc.Graph(id='trend-graphic')        
],style={'padding':10})

@app.callback(Output('segment','children'),[Input('car-model','value')])
def update_segment(car_model):
    print(car_model)
    seg = cassandra_session.execute("select s_segment_atmt from model_code where s_model_code='"+car_model+"'")
    car_list=cassandra_session.execute("select s_model_code from brand_and_model_atmt where s_segment_atmt='"+seg[0][0]+"' ALLOW FILTERING")
    return "Segment:"+seg[0][0]+" List:"+str([car[0] for car in car_list])

@app.callback(
    Output('trend-graphic', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('car_model', 'value')])
def update_graph(start_date, end_date,car_model):
    # d1 = start_date  # start date
    # d2 = end_date  # end date

    # delta = d2 - d1         # timedelta
    seg = cassandra_session.execute("select s_segment_atmt from model_code where s_model_code='"+car_model+"'")
    car_list=cassandra_session.execute("select s_model_code from brand_and_model_atmt where s_segment_atmt='"+seg[0][0]+"' ALLOW FILTERING")
    # for i in range(delta.days + 1):
    #     date=d1 + timedelta(i)

    #     for car in car_list:
    #         x={} 
    #         results = cassandra_session.execute("select d_utc_date,s_model_code,m_prospect_count from shoppers_day_model_natonal where s_model_code='"+car+"' and d_utc_date='"+date+"'")             
    #         x['Date']=results[0]
    #         x['Model']=results[1]
    #         x['Prospect']=results[2]
    #         final_list.append(x)

    # dff = pd.DataFrame(final_list)        
    # return {
    #     'data': [go.Scatter(
    #         #date and prospect of a car
    #         # df=dff[dff['Model']==car]
    #         x=dff[dff['Model']==car]['Date'],
    #         y=dff[dff['Model']==car]['Prospect'],
    #         mode='lines',
    #         name=car
    #     )for car in car_list],
    #     'layout': go.Layout(
    #         xaxis={
    #             'title': 'Date Range'
    #         },
    #         yaxis={
    #             'title': 'Prospect Count'
    #         },
    #         margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
    #         hovermode='closest'
    #     )
    return 'X'
    # }

if __name__=="__main__":
    app.run_server()
