from dash import Dash, dcc, html
from src.graphs import *

#--------#
### Dash application
#--------#

# Define application
app = Dash(__name__, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

# Define layout
app.layout = html.Div(id="main", children=[
    
    html.Div(id="graphs", children=[

            html.Div(id="dash-title", children=[
                    html.H1(children='Global Unicorn Investments and Valuations - Q1 2022'),
                    html.H2(children='Unicorn fundings is still a hot topic in the first quarter of 2022, although it is showing signs of slowdown from the 2021 fever. What do new unicorns in the first quarter (Q1) statistics in 2022 tell us and how do they compare to the previous years?')
            ]),

            html.Div(id="total_fundings_by_year", children=[
                    
                    html.H3(children='Fundings in Q1 2022 have declined a bit compared to Q1 2021...', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='total-fundings-by-year-graph',
                        figure=total_fundings_by_year_graph
                    )
            ]),

            html.Div(id="average-number-of-investors", children=[
                    
                    html.H3(children='...while the average number of investors per unicorn in Q1 has stabilized to almost 3.', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='average-number-of-investors-graph',
                        figure=avg_number_investors_by_year_graph
                    )
            ]),

            html.Div(id="top-5-unicorns-by-valuation", children=[
                    
                    html.H3(children='A digital whiteboard software company is by far the most valued new unicorn of Q1 2022.', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='top-5-unicorns-by-valuation-graph',
                        figure=top_unicorn_by_valuation_graph
                    )
            ]),

            html.Div(id="total-valuation-by-industry-continent", children=[
                    
                    html.H3(children='While fintech in Q1 2022 is a hot industry in North America and Europe, e-commerce & direct-to-consumer industry is leading valuation in Asia.', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='total-valuation-by-industry-continent-graph',
                        figure=total_valuation_by_industry_continent_graph
                    ),
            ]),

            html.Div(id="top-5-investors-by-roi", children=[
                    
                    html.H3(children='A women-led investment firm is leading the ROI race of investments in Q1 2022.', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='top-5-investors-by-roi-graph',
                        figure=top_investors_by_roi_graph
                    )
            ]),

            html.Div(id="average-funding-roi-by-country", children=[
                    
                    html.H3(children='Chinese unicorns are the most funded in Q1 2022 in average, while Norwegian firms have the highest ROI.', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='average-funding-roi-by-country-graph',
                        figure=avg_funding_roi_by_country_graph
                    )
            ]),
        
            html.Div(id="total_funding_by_industry", children=[
                    
                    html.H3(children='Most of the funding efforts in the Q1 2022 were directed to fintech firms, but the highest returns appear to be coming from the firms in the internet software and services industry.', style={
                        'textAlign': 'center',
                        'color': "#FFFFFF"
                    }),

                    dcc.Graph(
                        id='total-funding-by-industry-graph',
                        figure=total_funding_by_industry_graph
                    )
            ])
    ]),
    html.Div(id = "total-valuation-by-industry-continent-legend", children="* AI = \"Artificial Intelligence\", A&T = \"Auto & transportation, C&R = Consumer & retail\", C = \"Cybersecurity\", DM&A = \"Data management & analytics\", E&D = \"E-commerce & direct-to-consumer\", E = \"Edtech\", F = \"Fintech\", HW = \"Hardware\", H = \"Health\", IS&S = \"Internet software & services\", M&T = \"Mobile & telecommunications\", O = \"Other\", SL&D = \"Supply chain, logistics, & delivery\", T = \"Travel\""),
    html.Div(id="footer", children=[
        html.Div(id="container", children=[
            html.Div(id="foot-text", children="Created and designed with ❤️ and ☕ by Kauvin Lucas.")
        ])
    ])
])

# Start application
if __name__ == '__main__':
    app.run_server(debug=True)