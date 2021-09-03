import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import dropbox
from plotly.subplots import make_subplots
# Step 1. Launch the application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#C26000 ',
    'text': '#7FDBFF'
}
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server
dbx = dropbox.Dropbox("5uSdWA0gd2UAAAAAAAAAAauPVaO_t_nlwRgP3YzwZ8-2HlxYFWRLUrmTAgk4F4b7")
for entry in dbx.files_list_folder('').entries:
   aa=entry.name
   dd=entry.name
   if aa=='TrackTestDetail.csv':
       bb=entry.id
       resultresult =dbx.files_get_temporary_link(bb)
       cc=resultresult.link
   if aa=='Clinic Dasboard Table.csv':
       ee=entry.id
       resultresult =dbx.files_get_temporary_link(ee)
       ff=resultresult.link
st = pd.read_csv(cc)
df = pd.read_csv(ff)
features = ['Amount','Number Of Person']
opts = [{'label' : i, 'value' : i} for i in features]

# range slider options
st['Date'] = pd.to_datetime(st.Date,format='%d/%m/%Y')
# Step 3. Create a plotly figure
fig = make_subplots(
    rows=3, cols=2,
    column_widths=[1,1],
    row_heights=[1,1,1])
fig.add_trace(
    go.Bar(name='Navin Test Per Day',x=st.Date,y=st['Navin'], marker=dict(color="blue"), showlegend=True),
    row=1, col=1
)
fig.add_trace(
    go.Bar(name='Akbar Test Per day',x=st.Date,y=st['Akbar'], marker=dict(color="crimson"), showlegend=True),
    row=1, col=2
)
fig.add_trace(
    go.Bar(name='Fayaz Test Per day',x=st.Date,y=st['Fayaz'], marker=dict(color="Green"), showlegend=True),
    row=2, col=1
)
fig.add_trace(
    go.Bar(name='Sumaiya Test Per day',x=st.Date,y=st['Sumaiya'], marker=dict(color="orange"), showlegend=True),
    row=2, col=2
)
fig.add_trace(
    go.Bar(name='Obaidulah Test Per day',x=st.Date,y=st['Sumaiya'], marker=dict(color="darkcyan"), showlegend=True),
    row=3, col=1
)
fig.add_trace(
    go.Bar(name='Total Test Per day',x=st.Date,y=st['Total'], marker=dict(color="purple"), showlegend=True),
    row=3, col=2
)
fig.update_geos(
    projection_type="orthographic",
    landcolor="white",
    oceancolor="MidnightBlue",
    showocean=True,
    lakecolor="LightBlue"
)
fig.update_xaxes(tickangle=45)
fig.update_layout(
    template="plotly_dark",
    margin=dict(r=10, t=25, b=140, l=60),
    annotations=[
        dict(
            showarrow=False,
            xref="paper",
            yref="paper",
            x=0,
            y=0)
    ]
)
fig.update_layout(title_text="Lyfas Clinic Test Dashboard")
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
                # adding a header and a paragraph
                html.Div([
                    html.H1("Acculi Labs Pvt. Ltd.",style={'font-size': '50px','font-family':'Times New Roman','color':'black'}),
                    html.P(" Lyfas Clinic Test Dashboard Data Analytics",style={'font-size': '30px','font-family':'Times New Roman','color':'black'}),
                         ], 
                    style = {'padding' : '20px' , 
                             'backgroundColor' : 'orange',
                             'textAlign': 'center'}),
# adding a plot        
                dcc.Graph(id = 'plot', figure = fig),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=st.Date.min().date(),
                            max_date_allowed=st.Date.max().date(),
                            start_date=st.Date.min().date(),
                            end_date=st.Date.max().date(),
                            style={'margin-bottom': '20px', 'width': '100%','color':'white'},
                        ),
                        dash_table.DataTable(
                           id='table',
                           columns=[{"name":i,"id":i} for i in df.columns],
                           data=df.to_dict('records'),
                           style_header={'backgroundColor': '#00308F','font-size': '20px','textAlign': 'center','font-family':'Times New Roman'},
                           style_cell={
                               'backgroundColor': 'rgb(50, 50, 50)',
                                'color': 'white',
                                 'textAlign': 'left','font-size': '15px','textAlign': 'center','font-family':'Times New Roman'},
                           )
                     
                    ]
                ),
                html.Hr(style={'color':'black','width':'99%','height':'2px','backgroundColor': 'black'}),
                html.Div('Acculi Labs, #1156,Office Berth, BEML Layout, RR Nagar, Bangalore 560098',style={'font-size': '30px','font-family':'Times New Roman','color':'black','textAlign':'center'}),
                html.Br(),
                html.A([html.Button(html.Img(src='https://www.lyfas.com/wp-content/uploads/2017/06/cropped-Logo.png',width="120",height ="70"),
                                    style={'width':'10%', 'border':'1px orange','height': '70px','textalign':'center', 'marginLeft': '230px'})],href="https://www.lyfas.com/",target="_blank"),
                html.A([html.Button(html.Img(src='data:image/jpeg;base64,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',
                                             width="120",height ="70"),
                                    style={'width':'10%', 'border':'1px orange','height': '70px','textalign':'center', 'marginLeft': '10px'})],
                       href="https://www.facebook.com/TelemedicineLyfas/",target="_blank"),
                html.A([html.Button(html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrXZ_-gucFhbENdnYI-AfDih2aP-q98IUQH2FLotxJZkLKw5bXr3Dg2qjFDtJEim2ZmqU&usqp=CAU',width="120",height ="70"),
                                    style={'width':'10%', 'border':'1px orange','height': '70px','textalign':'center', 'marginLeft': '10px'})],href="https://www.linkedin.com/company/acculi-labs/mycompany/",target="_blank"),

                 html.A([html.Button(html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBgk04oTuyMhBVhxDz671AQceOvMfO0sMDWQ&usqp=CAU',width="120",height ="70"),
                                    style={'width':'10%', 'border':'1px orange','height': '70px','textalign':'center', 'marginLeft': '10px'})],href="https://www.instagram.com/acculilabs_lyfas247/",target="_blank"),
                html.A([html.Button(html.Img(src='https://tse2.mm.bing.net/th?id=OIP.b4rDh_UyOn2bf3285hmOngHaFi&pid=Api&P=0&w=209&h=157',width="120",height ="70"),
                                    style={'width':'10%', 'border':'1px orange','height': '70px','textalign':'center', 'marginLeft': '10px'})],href="https://twitter.com/acculilabs",target="_blank"),
                html.A([html.Button(html.Img(src='data:image/png;base64,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',
                                             width="120",height ="70"),
                                    style={'width':'10%', 'border':'1px orange','height': '70px','textalign':'center', 'marginLeft': '10px'})],href="https://www.youtube.com/channel/UCT-AeDjLikJexnSSQB79B5w",target="_blank"),
                html.Br(),
                      ])
@app.callback(Output('plot', 'figure'),
             [ Input("date-range", "start_date"),
        Input("date-range", "end_date"),])
def update_charts(start_date, end_date):
    mask = (
        (st.Date >= start_date)
        & (st.Date <= end_date)
    )
    filtered_data = st.loc[mask, :]
    fig = make_subplots(
    rows=3, cols=2,
    column_widths=[1,1],
    row_heights=[1,1,1])
    fig.add_trace(
    go.Bar(name='Navin Test Per Day',x=filtered_data['Date'],y=filtered_data['Navin'], marker=dict(color="blue"), showlegend=True,text=filtered_data['Navin'],textposition='auto'),
    row=1, col=1
    )
    fig.add_trace(
    go.Bar(name='Akbar Test Per day',x=filtered_data['Date'],y=filtered_data['Akbar'], marker=dict(color="crimson"), showlegend=True,text=filtered_data['Akbar'],textposition='auto'),
    row=1, col=2
    )
    fig.add_trace(
    go.Bar(name='Fayaz Test Per day',x=filtered_data['Date'],y=filtered_data['Fayaz'], marker=dict(color="Green"), showlegend=True,text=filtered_data['Fayaz'],textposition='auto'),
    row=2, col=1)
    fig.add_trace(
    go.Bar(name='Sumaiya Test Per day',x=filtered_data['Date'],y=filtered_data['Sumaiya'], marker=dict(color="orange"), showlegend=True,text=filtered_data['Sumaiya'],textposition='auto'),
    row=2, col=2)
    fig.add_trace(
    go.Bar(name='Obaidulah Test Per day',x=filtered_data['Date'],y=filtered_data['Obaidulah'], marker=dict(color="darkcyan"), showlegend=True,text=filtered_data['Obaidulah'],textposition='auto'),
    row=3, col=1)
    fig.add_trace(
    go.Bar(name='Total Test Per day',x=filtered_data['Date'],y=filtered_data['Total'],marker=dict(color="purple"), showlegend=True,text=filtered_data['Total'],textposition='auto'),
    row=3, col=2)
    fig.update_geos(
    projection_type="orthographic",
    landcolor="white",
    oceancolor="MidnightBlue",
    showocean=True,
    lakecolor="LightBlue"
    )
    fig.update_xaxes(tickangle=45)
    fig.update_layout(
    template="plotly_dark",
    margin=dict(r=10, t=25, b=40, l=60),
    annotations=[
        dict(
            showarrow=False,
            xref="paper",
            yref="paper",
            x=0,
            y=0)
    ]
    )
    fig.update_layout(height=700,title_text="Lyfas Clinic Test Dashboard")
    return fig
    # updating the plot
  
# Step 6. Add the server clause
if __name__ == "__main__":
        app.run_server(debug=False)
