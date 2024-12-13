"""Imports"""

import pandas as pd
from dash import Dash, html, dcc, Input, Output 
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.figure_factory as ff

""" Variables"""

dataset_url = "https://raw.githubusercontent.com/markusreynoso/dashboard-datasets/refs/heads/main/Life%20Expectancy/Life%20Expectancy%20Data.csv"
light = "#E6FDFF"
dark = "#1D2829"
dark2 = "#121717"
mint = "#36BA9B"
emerald = "#4EDFA0"
red_bright = "#F8333C"
red_dark = "#960200"

country_coords = {
    'Afghanistan': (33.93911, 67.709953),
    'Albania': (41.153332, 20.168331),
    'Algeria': (28.033886, 1.659626),
    'Angola': (-11.202692, 17.873887),
    'Argentina': (-38.416097, -63.616672),
    'Armenia': (40.069099, 45.038189),
    'Australia': (-25.274398, 133.775136),
    'Austria': (47.516231, 14.550072),
    'Azerbaijan': (40.143105, 47.576927),
    'Bangladesh': (23.684994, 90.356331),
    'Belarus': (53.709807, 27.953389),
    'Belgium': (50.503887, 4.469936),
    'Belize': (17.189877, -88.49765),
    'Benin': (9.30769, 2.315834),
    'Bhutan': (27.514162, 90.433601),
    'Bosnia and Herzegovina': (43.915886, 17.679076),
    'Botswana': (-22.328474, 24.684866),
    'Brazil': (-14.235004, -51.92528),
    'Bulgaria': (42.733883, 25.48583),
    'Burkina Faso': (12.238333, -1.561593),
    'Burundi': (-3.373056, 29.918886),
    'Cabo Verde': (16.002082, -24.013197),
    'Cambodia': (12.565679, 104.990963),
    'Cameroon': (7.369722, 12.354722),
    'Canada': (56.130366, -106.346771),
    'Central African Republic': (6.611111, 20.939444),
    'Chad': (15.454166, 18.732207),
    'Chile': (-35.675147, -71.542969),
    'China': (35.86166, 104.195397),
    'Colombia': (4.570868, -74.297333),
    'Comoros': (-11.875001, 43.872219),
    'Costa Rica': (9.748917, -83.753428),
    'Croatia': (45.1, 15.2),
    'Cyprus': (35.126413, 33.429859),
    'Djibouti': (11.825138, 42.590275),
    'Dominican Republic': (18.735693, -70.162651),
    'Ecuador': (-1.831239, -78.183406),
    'El Salvador': (13.794185, -88.89653),
    'Equatorial Guinea': (1.650801, 10.267895),
    'Eritrea': (15.179384, 39.782334),
    'Estonia': (58.595272, 25.013607),
    'Ethiopia': (9.145, 40.489673),
    'Fiji': (-17.713371, 178.065032),
    'France': (46.603354, 1.888334),
    'Gabon': (-0.803689, 11.609444),
    'Georgia': (42.315407, 43.356892),
    'Germany': (51.165691, 10.451526),
    'Ghana': (7.946527, -1.023194),
    'Greece': (39.074208, 21.824312),
    'Guatemala': (15.783471, -90.230759),
    'Guinea': (9.945587, -9.696645),
    'Guinea-Bissau': (11.803749, -15.180413),
    'Guyana': (4.860416, -58.93018),
    'Haiti': (18.971187, -72.285215),
    'Honduras': (15.199999, -86.241905),
    'India': (20.593684, 78.96288),
    'Indonesia': (-0.789275, 113.921327),
    'Iraq': (33.223191, 43.679291),
    'Ireland': (53.41291, -8.24389),
    'Israel': (31.046051, 34.851612),
    'Italy': (41.87194, 12.56738),
    'Jamaica': (18.109581, -77.297508),
    'Jordan': (30.585164, 36.238414),
    'Kazakhstan': (48.019573, 66.923684),
    'Kenya': (-0.023559, 37.906193),
    'Kiribati': (-3.370417, -168.734039),
    'Latvia': (56.879635, 24.603189),
    'Lebanon': (33.854721, 35.862285),
    'Lesotho': (-29.609988, 28.233608),
    'Liberia': (6.428055, -9.429499),
    'Lithuania': (55.169438, 23.881275),
    'Luxembourg': (49.815273, 6.129583),
    'Madagascar': (-18.766947, 46.869107),
    'Malawi': (-13.254308, 34.301525),
    'Malaysia': (4.210484, 101.975766),
    'Maldives': (3.202778, 73.22068),
    'Mali': (17.570692, -3.996166),
    'Malta': (35.937496, 14.375416),
    'Mauritania': (21.00789, -10.940835),
    'Mauritius': (-20.348404, 57.552152),
    'Mexico': (23.634501, -102.552784),
    'Mongolia': (46.862496, 103.846656),
    'Montenegro': (42.708678, 19.37439),
    'Morocco': (31.791702, -7.09262),
    'Mozambique': (-18.665695, 35.529562),
    'Myanmar': (21.913965, 95.956223),
    'Namibia': (-22.95764, 18.49041),
    'Nepal': (28.394857, 84.124008),
    'Netherlands': (52.132633, 5.291266),
    'Nicaragua': (12.865416, -85.207229),
    'Niger': (17.607789, 8.081666),
    'Nigeria': (9.081999, 8.675277),
    'Pakistan': (30.375321, 69.345116),
    'Panama': (8.537981, -80.782127),
    'Papua New Guinea': (-6.314993, 143.95555),
    'Paraguay': (-23.442503, -58.443832),
    'Peru': (-9.189967, -75.015152),
    'Philippines': (12.879721, 121.774017),
    'Poland': (51.919438, 19.145136),
    'Portugal': (39.399872, -8.224454),
    'Romania': (45.943161, 24.96676),
    'Russian Federation': (61.52401, 105.318756),
    'Rwanda': (-1.940278, 29.873888),
    'Samoa': (-13.759029, -172.104629),
    'Sao Tome and Principe': (0.18636, 6.613081),
    'Senegal': (14.497401, -14.452362),
    'Serbia': (44.016521, 21.005859),
    'Seychelles': (-4.679574, 55.491977),
    'Sierra Leone': (8.460555, -11.779889),
    'Solomon Islands': (-9.64571, 160.156194),
    'South Africa': (-30.559482, 22.937506),
    'Spain': (40.463667, -3.74922),
    'Sri Lanka': (7.873054, 80.771797),
    'Suriname': (3.919305, -56.027783),
    'Swaziland': (-26.522503, 31.465866),
    'Sweden': (60.128161, 18.643501),
    'Syrian Arab Republic': (34.802075, 38.996815),
    'Tajikistan': (38.861034, 71.276093),
    'Thailand': (15.870032, 100.992541),
    'Timor-Leste': (-8.874217, 125.727539),
    'Togo': (8.619543, 0.824782),
    'Tonga': (-21.178986, -175.198242),
    'Trinidad and Tobago': (10.691803, -61.222503),
    'Tunisia': (33.886917, 9.537499),
    'Turkey': (38.963745, 35.243322),
    'Turkmenistan': (38.969719, 59.556278),
    'Uganda': (1.373333, 32.290275),
    'Ukraine': (48.379433, 31.16558),
    'Uruguay': (-32.522779, -55.765835),
    'Uzbekistan': (41.377491, 64.585262),
    'Vanuatu': (-15.376706, 166.959158),
    'Zambia': (-13.133897, 27.849332),
    'Zimbabwe': (-19.015438, 29.154857)
}
year_options = [{'label': str(year), 'value': year} for year in range(2000,2015)]
factor_options = [{'label': 'Average BMI', 'value': 'bmi'},
                  {'label': 'Alcohol Consumption per capita (15+) in Liters', 'value': 'alcohol'},
                  {'label': 'Number of Infant Deaths per 1000 population', 'value': 'infant_deaths'},
                  {'label': 'Number of under-five deaths per 1000 population', 'value': 'under-five_deaths'},
                  {'label': 'Measles - reported cases per 1000 population', 'value': 'measles'},
                  {'label': 'Polio immunization among 1-year-olds (%)', 'value': 'polio'},
                  {'label': 'Hepatitis B immunization among 1-year-olds (%)', 'value': 'hepatitis_b'},
                  {'label': 'Diphtheria tetanus toxoid and pertussis immunization among 1-year-olds (%)', 'value': 'diphtheria'},
                  {'label': 'GDP per capita (in USD)', 'value': 'gdp'},
                  {'label': 'Expenditure on health as a percentage of total government expenditure (%)', 'value': 'total_expenditure'},
                  {'label': 'Number of years of Schooling (years)', 'value': 'schooling'},
                  ]
var_options = [x for x in factor_options]
var_options.append({'label': 'Life Expectancy', 'value': 'life_expectancy'})
country_options = list(country_coords.keys())
development_color_map = {
    'Developing': red_bright,
    'Developed': emerald
}

""" Dashboard """

app = Dash()
app.layout = html.Div(
    id='main-wrapper',
    children=[
        html.H1(
            id='dashboard-title',
            children='World Life Expectancy Dashboard'
        ),

        html.Div(
            id='map-div',
            className='card',
            children=[
                dcc.Graph(
                    id='map-graph',
                    figure={}
                )
            ]
        ),

        html.Div(
            id='tray-1',
            children=[
                html.Div(
                    id='group-1',
                    children=[
                        html.Div(
                            className='card',
                            id='scatter-div',
                            children=dcc.Graph(id='scatter-graph')
                            ),

                        dcc.Dropdown(
                                    id='year-dropdown',
                                    className='dropdown',
                                    options=year_options,
                                    placeholder='Select year',
                                    clearable=False,
                                    value=2000
                                )
                            ]
                        ),

                html.Div(
                    id='group-2',
                    children=[
                        html.Div(
                            className='card',
                            id='histogram-div',
                            children=[
                                dcc.Graph(
                                    id='histogram-graph'
                                )
                            ]
                        ),

                        dcc.Dropdown(
                            className='dropdown',
                            id='factor-dropdown',
                            options=[
                                        {'label': 'Average BMI', 'value': 'bmi'},
                                        {'label': 'Alcohol Consumption per capita (15+) in Liters', 'value': 'alcohol'},
                                        {'label': 'Number of Infant Deaths per 1000 population', 'value': 'infant_deaths'},
                                        {'label': 'Number of under-five deaths per 1000 population', 'value': 'under-five_deaths'},
                                        {'label': 'Measles - reported cases per 1000 population', 'value': 'measles'},
                                        {'label': 'Polio immunization among 1-year-olds (%)', 'value': 'polio'},
                                        {'label': 'Hepatitis B immunization among 1-year-olds (%)', 'value': 'hepatitis_b'},
                                        {'label': 'Diphtheria tetanus toxoid and pertussis immunization among 1-year-olds (%)', 'value': 'diphtheria'},
                                        {'label': 'GDP per capita (in USD)', 'value': 'gdp'},
                                        {'label': 'Expenditure on health as a percentage of total government expenditure (%)', 'value': 'total_expenditure'},
                                        {'label': 'Number of years of Schooling (years)', 'value': 'schooling'},
                                    ],
                            value='bmi',
                            clearable=False
                        )
                    ]
                )
            ]
        ),

        html.Div(
            className='card',
            id='bar-div',
            children=[
                dcc.Graph(
                    id='bar-graph'
                )
            ]
        ),

        html.Div(
            html.Center(children=[
                html.H2(id='country-dynamic-text', children='temp'),
                html.H2(id='focus-title', children=': A Closer Look')
                ]
            )
        ),

        
        html.Div(
            id='focus-section-top-group',
            children=[
                html.Div(
                    className='card',
                    id='focus-section-controls-container',
                    children=[         
                        html.P(
                            id='focus-section-controls-title',
                            children='Controls'
                        ),

                        dcc.Dropdown(
                            className='dropdown',
                            id='focus-country-dropdown',
                            options=country_options,
                            clearable=False,
                            value='Philippines'
                        ),

                        dcc.Dropdown(
                            className='dropdown',
                            id='focus-year-dropdown',
                            options=year_options,
                            clearable=False,
                            value=2000
                        ),
                        ]
                ),

                html.Div(
                    id='focus-section-grid-container',
                    children=[
                        html.Div(
                            className='stat-card',
                            id='status-container',
                            children=[
                                html.P(
                                    className='stat-title',
                                    children='Status'
                                ),

                                html.P(
                                    className='stat',
                                    id='status-stat',
                                    children='test'
                                )
                            ]
                        ),

                        html.Div(
                            className='stat-card',
                            id='population-container',
                            children=[
                                html.P(
                                    className='stat-title',
                                    children='Population'
                                ),

                                html.P(
                                    className='stat',
                                    id='population-stat',
                                    children='test'
                                )
                            ]
                        ),

                        html.Div(
                            className='stat-card',
                            id='gdp-container',
                            children=[
                                html.P(
                                    className='stat-title',
                                    children='GDP per capita (in USD)'
                                ),

                                html.P(
                                    className='stat',
                                    id='gdp-stat',
                                    children='test'
                                )
                            ]
                        ),

                        html.Div(
                            className='stat-card',
                            id='life-expectancy-container',
                            children=[
                                html.P(
                                    className='stat-title',
                                    children='Life Expectancy'
                                ),

                                html.P(
                                    className='stat',
                                    id='life-expectancy-stat',
                                    children='test'
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        dcc.Dropdown(
           className='dropdown',
           id='factor-dropdown-line',
           options=var_options,
           clearable=False,
           value='bmi'
        ),

        html.Div(
            className='card',
            id='line-div',
            children=dcc.Graph(id='line-graph')
        )
        
    ]
)

@app.callback(
    Output(component_id='map-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)
def update_map(year):
    df = pd.read_csv(dataset_url).dropna()
    df.columns = [x.strip().lower().replace('  ', '_').replace(' ', '_') for x in df.columns]
    df['lon'] = df['country'].apply(lambda x: country_coords.get(x, (np.nan, np.nan))[1])
    df['lat'] = df['country'].apply(lambda x: country_coords.get(x, (np.nan, np.nan))[0])
    df.dropna(inplace=True)

    min_life_expectancy = df['life_expectancy'].min()
    max_life_expectancy = df['life_expectancy'].max()

    map_fig = px.scatter_mapbox(
        df.loc[df['year'] == year],
        lon='lon',
        lat='lat',
        zoom=1,
        mapbox_style='carto-darkmatter',
        color='life_expectancy',
        color_continuous_scale=[red_dark, red_bright, mint, emerald],
        range_color=[min_life_expectancy, max_life_expectancy],
        title='Life Expectancy',
        hover_name='country',
        hover_data={'life_expectancy': True, 'lon': False, 'lat': False}
    )

    map_fig.update_traces(hovertemplate='<b>Country:</b> %{hovertext}<br>' +
                                       '<b>Life Expectancy:</b> %{customdata[0]:.2f}<br>' +
                                       '<extra></extra>')

    map_fig.update_layout(
        paper_bgcolor=dark2,
        title=dict(
            text=f'Life Expectancy per Country (years) in {year}',
            font=dict(
                family='Poppins',
                color=light),
            y=0.1,
            x=0.5,
            xanchor='center'
        ),
        coloraxis_colorbar=dict(
            orientation='h',
            title=None,
            title_font=dict(
                family='Poppins',
                color=light),
            tickfont=dict(
                family='Poppins',
                color=light),
            thickness=15,
            len=0.7,
            xanchor='center',
            x=0.5,
            yanchor='bottom',
            y=0.05,
            outlinecolor='black',
            outlinewidth=2,
            tickvals=[min_life_expectancy, max_life_expectancy],
            ticktext=[f'{min_life_expectancy:.1f}', f'{max_life_expectancy:.1f}'],
    ),
        margin=dict(l=25, r=25, t=25, b=25)
    )

    return map_fig


@app.callback(
    Output(component_id='scatter-graph', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value'),
     Input(component_id='factor-dropdown', component_property='value')]
)
def update_scatter(year, factor):
    if factor is None or factor == '':
        return px.scatter()
    df = pd.read_csv(dataset_url).dropna()
    df.columns = [x.strip().lower().replace('  ', '_').replace(' ', '_') for x in df.columns]
    df['lon'] = df['country'].apply(lambda x: country_coords.get(x, (np.nan, np.nan))[1])
    df['lat'] = df['country'].apply(lambda x: country_coords.get(x, (np.nan, np.nan))[0])
    df.dropna(inplace=True)
    df = df.loc[df['year'] == year]

    scatter_fig = px.scatter(
        df,
        x=factor,
        y='life_expectancy',
        color='status',
        color_discrete_map=development_color_map,
        hover_data={'country': True, 'life_expectancy': True}
    )

    scatter_fig.update_layout(
        paper_bgcolor=dark2,
        plot_bgcolor=dark2,
        font=dict(
                family='Poppins',
                color=light),
        titlefont=dict(
                family='Poppins',
                color=light),
        legend=dict(
            title='Status',
            orientation='h',
            yanchor='bottom',
            y=-0.3,
            xanchor='center',
            x=0.5
        )
    )

    scatter_fig.update_traces(
        hovertemplate='<b>Country:</b> %{text}<br>' +
                      '<b>Life Expectancy:</b> %{y}<br>' +
                      '<extra></extra>',
        text=df['country']
    )

    scatter_fig.update_xaxes(
        gridcolor='#3d3d3d',
        gridwidth=1,
        zerolinecolor='#3d3d3d',
        zerolinewidth=2
    )

    scatter_fig.update_yaxes(
        gridcolor=light,
        gridwidth=1,
        zerolinecolor=light,
        zerolinewidth=2
    )

    return scatter_fig


@app.callback(
    Output(component_id='histogram-graph', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value'),
     Input(component_id='factor-dropdown', component_property='value')]
)
def update_histogram(selected_year, selected_factor):
    df = pd.read_csv(dataset_url).dropna()
    df.columns = [x.strip().lower().replace('  ', '_').replace(' ', '_') for x in df.columns]
    df = df.loc[df['year'] == selected_year]
    fig = ff.create_distplot(
            [df.loc[df['status'] == 'Developing'][selected_factor], df.loc[df['status'] == 'Developed'][selected_factor]],
            ['Developing', 'Developed'],
            colors=[red_bright, emerald],
            show_rug=False
        )
    
    fig.update_layout(
        paper_bgcolor=dark2,
        plot_bgcolor=dark2,
        font=dict(
                family='Poppins',
                color=light),
        legend=dict(
            font=dict(
                family='Poppins',
                color=light),
            title='Status',
            orientation='h',
            yanchor='bottom',
            y=-0.3,
            xanchor='center',
            x=0.5
        )
    )
    return fig

@app.callback(
    Output(component_id='bar-graph', component_property='figure'),
    [Input(component_id='year-dropdown', component_property='value'),
     Input(component_id='factor-dropdown', component_property='value')]
)
def update_bar(year, factor):
    df = pd.read_csv(dataset_url).dropna()
    df.columns = [x.strip().lower().replace('  ', '_').replace(' ', '_') for x in df.columns]
    df1 = df.loc[df['year'] == year].sort_values(factor, ascending=False).nlargest(10, factor)

    fig = px.bar(
            df1.sort_values(factor, ascending=False),
            x='country',
            y=factor,
            color='status',
            color_discrete_map=development_color_map,
        )
    
    min_value = df1[factor].min() * 0.9
    max_value = df1[factor].max() * 1.1

    fig.update_layout(
        title=dict(
            text='Top countries in this category',
            font=dict(
                family='Poppins',
                color=light),
            x=0.5,
            y=0.9,
            xanchor='center'
        ),
        yaxis=dict(
            range=[min_value, max_value]
        ),
        paper_bgcolor=dark2,
        plot_bgcolor=dark2,
        font=dict(color=light),
        legend=dict(
            font=dict(
                family='Poppins',
                color=light),
            title='Status',
            orientation='h',
            yanchor='bottom',
            y=-0.3,
            xanchor='center',
            x=0.5
        ),
        margin=dict(
            l=80,
            r=50,
            t=50,
            b=50
        )
    )

    return fig

@app.callback(
    Output(component_id='country-dynamic-text', component_property='children'),
    [Input(component_id='focus-country-dropdown', component_property='value'),
    Input(component_id='focus-year-dropdown', component_property='value'),]
)
def update_focus_country(country, year):
    return f"{country} ({year})"


@app.callback(
    [Output(component_id='status-stat', component_property='children'),
     Output(component_id='population-stat', component_property='children'),
     Output(component_id='gdp-stat', component_property='children'),
     Output(component_id='life-expectancy-stat', component_property='children')],
    [Input(component_id='focus-country-dropdown', component_property='value'),
    Input(component_id='focus-year-dropdown', component_property='value'),]
)
def update_stats(country, year):
    df = pd.read_csv(dataset_url).dropna()
    df.columns = [x.strip().lower().replace('  ', '_').replace(' ', '_') for x in df.columns]
    df = df.loc[(df['year'] == year) & (df['country'] == country)]

    status = df['status'].iloc[0] if 'status' in df.columns and not df.empty else 'No data'
    pop = f"{int(df['population'].iloc[0]):,}" if 'population' in df.columns and not df.empty else 'No data'
    gdp = f"{round(df['gdp'].iloc[0], 2):,}" if 'gdp' in df.columns and not df.empty else 'No data'
    le = df['life_expectancy'].iloc[0] if 'life_expectancy' in df.columns and not df.empty else 'No data'

    return status, pop, gdp, le
    
@app.callback(
    Output(component_id='line-graph', component_property='figure'),
    [Input(component_id='focus-country-dropdown', component_property='value'),
     Input(component_id='factor-dropdown-line', component_property='value')]
)
def update_line(country, factor):
    df = pd.read_csv(dataset_url).dropna()
    df.columns = [x.strip().lower().replace('  ', '_').replace(' ', '_') for x in df.columns]
    df = df.loc[df['country'] == country]

    fig = px.line(
        df,
        x='year',
        y=factor
    )

    fig.update_layout(
        xaxis=dict(
            tickmode='linear',
            tickfont=dict(color=light),
            titlefont=dict(color=light),
            tickcolor=dark,
            gridcolor=dark
        ),
        yaxis=dict(
            tickfont=dict(color=light),
            titlefont=dict(color=light),
            tickcolor=dark,
            gridcolor=dark
        ),
        paper_bgcolor=dark2,
        plot_bgcolor=dark2,
        font=dict(color=light)
    )



    fig.update_traces(
        line=dict(color=emerald),
    )

    return fig
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=False)
