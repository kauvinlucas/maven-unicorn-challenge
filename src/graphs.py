import plotly.express as px
from plotly.graph_objs import Line
import pandas as pd
from src.preprocessing import *


##################
### Dataframes ###
##################

# Total fundings by year
total_fundings_by_year = df.drop_duplicates(subset="Company").sort_values(by="Funding").groupby("Year Joined")[["Valuation", "Funding", "ROI"]].sum().reset_index()
total_fundings_by_year.rename(columns = {'Funding':'Total funding'}, inplace = True)

# Average number of investors by year
avg_number_investors_by_year = df.drop_duplicates(subset="Company")
df_1 = df.groupby("Company")[["Select Investors", "Company"]].count()["Select Investors"].reset_index()
avg_number_investors_by_year = avg_number_investors_by_year.merge(df_1, on="Company")
avg_number_investors_by_year = avg_number_investors_by_year.groupby("Year Joined")[["Select Investors_y"]].mean().reset_index()
avg_number_investors_by_year.rename(columns = {'Select Investors_y':'Average of investors'}, inplace = True)

# Top 5 unicorns by valuation
top_unicorn_by_valuation = df[df["Year Joined"] == 2022].drop_duplicates("Company").sort_values(by="Valuation", ascending=False).head(5)

# Total valuation by industry and continent
total_valuation_by_industry_continent = df.groupby(["Continent", "Industry"])[["Valuation"]].sum().reset_index()
total_valuation_by_industry_continent.rename(columns = {'Industry':'Industry *'}, inplace = True)
total_valuation_by_industry_continent = total_valuation_by_industry_continent.pivot(index="Continent",columns="Industry *", values="Valuation")

# Top 5 investors by ROI
top_investors_by_roi = df[df["Year Joined"] == 2022].groupby("Select Investors").mean().sort_values(by="ROI", ascending=False).reset_index().head(5)
top_investors_by_roi.rename(columns = {'Select Investors':'Investor'}, inplace = True)

# Average funding and ROI by country
avg_funding_roi_by_country = df[df["Year Joined"] == 2022].drop_duplicates().groupby("iso_alpha")[["Funding", "ROI"]].mean().reset_index()
avg_funding_roi_by_country.rename(columns = {'Funding':'Average funding', 'ROI': 'Average ROI'}, inplace = True)

# Total funding and ROI by industry
total_funding_by_industry = df[df["Year Joined"] == 2022].groupby(["Company"]).agg({'Funding': 'sum',
                       'Industry': 'first',
                        'ROI': 'mean'}).reset_index()


#####################
### Plotly Graphs ###
#####################

# Total fundings by year (bar chart)
total_fundings_by_year_graph = px.bar(
                                     data_frame = total_fundings_by_year, 
                                     x="Year Joined", 
                                     y="Total funding"
)
total_fundings_by_year_graph.update_layout(
                                           plot_bgcolor = "rgba(0,0,0,0)", 
                                           paper_bgcolor = "rgba(0,0,0,0)", 
                                           xaxis_showgrid=False, 
                                           yaxis_showgrid=False,
                                           font_color="#FFFFFF"
)
total_fundings_by_year_graph.update_xaxes(showline=True, linewidth=1, linecolor='#585858')
total_fundings_by_year_graph.update_yaxes(showline=True, linewidth=1, linecolor='#585858')
total_fundings_by_year_graph['layout'].update(margin=dict(l=80,r=20,b=20,t=20))
total_fundings_by_year_graph.update_traces(marker_color='#4B007F')


# Average number of investors by year (bar chart)
help_fig = px.scatter(
                      avg_number_investors_by_year, 
                      y = 'Average of investors', 
                      x= 'Year Joined',
                      trendline='lowess',trendline_color_override='red'
)
x_trend = help_fig["data"][1]['x']
y_trend = help_fig["data"][1]['y']

avg_number_investors_by_year_graph = px.bar(
                                            data_frame = avg_number_investors_by_year, 
                                            y="Average of investors",
                                            x="Year Joined"
)
avg_number_investors_by_year_graph.update_traces(marker_color='#4B007F')
avg_number_investors_by_year_graph.update_layout(
                                                 plot_bgcolor = "rgba(0,0,0,0)", 
                                                 paper_bgcolor = "rgba(0,0,0,0)", 
                                                 xaxis_showgrid=False, 
                                                 yaxis_showgrid=False,
                                                 font_color="#FFFFFF"
)
avg_number_investors_by_year_graph.update_xaxes(showline=True, linewidth=1, linecolor='#585858')
avg_number_investors_by_year_graph.update_yaxes(showline=True, linewidth=1, linecolor='#585858')
avg_number_investors_by_year_graph['layout'].update(margin=dict(l=70,r=20,b=60,t=20))
avg_number_investors_by_year_graph.add_trace(Line(x=x_trend, y=y_trend, name="LOWESS trend", fillcolor="#137B68"))
avg_number_investors_by_year_graph.update_traces(showlegend=False)

# Top 5 unicorns by valuation (horizontal bar chart)
color_discrete_map = {
                      'Miro': '#137B68',
                      'RELEX Solutions': '#4B007F',
                      'Qonto': '#4B007F',
                      'Hozon Auto': '#4B007F',
                      'Yuga Labs':'#4B007F'
}
top_unicorn_by_valuation_graph = px.bar(
                                        data_frame = top_unicorn_by_valuation,
                                        y="Company", 
                                        x="Valuation", 
                                        orientation='h',
                                        color="Company",
                                        color_discrete_map = color_discrete_map
)
top_unicorn_by_valuation_graph.update_layout(
                                             plot_bgcolor = "rgba(0,0,0,0)", 
                                             paper_bgcolor = "rgba(0,0,0,0)", 
                                             xaxis_showgrid=False, 
                                             yaxis_showgrid=False,
                                             font_color="#FFFFFF", 
                                             showlegend=False
)
top_unicorn_by_valuation_graph.update_xaxes(showline=True, linewidth=1, linecolor='#585858')
top_unicorn_by_valuation_graph.update_yaxes(showline=True, linewidth=1, linecolor='#585858')
top_unicorn_by_valuation_graph['layout'].update(margin=dict(l=150,r=20,b=60,t=20))


# Total valuation by industry and continent (heat map)
total_valuation_by_industry_continent_graph = px.imshow(
                                                        total_valuation_by_industry_continent, 
                                                        labels=dict(color = "Valuation"),
                                                        color_continuous_scale='viridis', 
                                                        x = ["AI", "A&T", "C&R", "C", "DM&A", "E&D", "E", "F", "HW", "H", "IS&S", "M&T", "O", "SL&D", "T"]
)
total_valuation_by_industry_continent_graph.update_layout(
                                                          plot_bgcolor = "rgba(0,0,0,0)", 
                                                          paper_bgcolor = "rgba(0,0,0,0)", 
                                                          xaxis_showgrid=False, 
                                                          yaxis_showgrid=False,
                                                          font_color="#FFFFFF"
)
total_valuation_by_industry_continent_graph.update_xaxes(showline=True, linewidth=1, linecolor='#585858', side="top")
total_valuation_by_industry_continent_graph.update_yaxes(showline=True, linewidth=1, linecolor='#585858')
total_valuation_by_industry_continent_graph['layout'].update(margin=dict(l=140,r=20,b=10,t=100))


# Top 5 investors by ROI (horizontal bar chart)
color_discrete_map = {
                      'First Light Capital Group': '#137B68',
                      'The Raine Group': '#4B007F',
                      'Malabar Investments': '#4B007F',
                      'AltaIR Capital': '#4B007F',
                      'L Catterton':'#4B007F'
}
top_investors_by_roi_graph = px.bar(
                                    data_frame = top_investors_by_roi, 
                                    y="Investor", 
                                    x="ROI", 
                                    orientation='h',
                                    color="Investor",
                                    color_discrete_map = color_discrete_map
                                    )
top_investors_by_roi_graph.update_layout(
                                         plot_bgcolor = "rgba(0,0,0,0)", 
                                         paper_bgcolor = "rgba(0,0,0,0)", 
                                         xaxis_showgrid=False, 
                                         yaxis_showgrid=False,
                                         font_color="#FFFFFF",
                                         showlegend=False
                                         )
top_investors_by_roi_graph.update_xaxes(showline=True, linewidth=1, linecolor='#585858')
top_investors_by_roi_graph.update_yaxes(showline=True, linewidth=1, linecolor='#585858')
top_investors_by_roi_graph['layout'].update(margin=dict(l=195,r=20,b=60,t=20))


# Average funding and ROI by country (scatter map)
avg_funding_roi_by_country_graph = px.scatter_geo(
                                                  avg_funding_roi_by_country, 
                                                  locations="iso_alpha", 
                                                  color="Average ROI", size="Average funding",
                                                  projection="equirectangular", color_continuous_scale='viridis'
                                                  )
avg_funding_roi_by_country_graph.update_geos(
                                             resolution=50,
                                             showcoastlines=True, coastlinecolor="RebeccaPurple",
                                             showland=True, landcolor="rgba(24,55,24,0.7)",
                                             showocean=True, oceancolor="rgba(0,0,0,0)",
                                             showlakes=True, lakecolor="Blue"
                                             )
avg_funding_roi_by_country_graph.update_layout(
                                               plot_bgcolor = "rgba(0,0,0,0)",
                                               geo_bgcolor  = "rgba(0,0,0,0.3)",
                                               paper_bgcolor = "rgba(0,0,0,0)", 
                                               xaxis_showgrid=False, 
                                               yaxis_showgrid=False,
                                               font_color="#FFFFFF"
                                               )
avg_funding_roi_by_country_graph['layout'].update(margin=dict(l=10,r=10,b=20,t=10))


# Total funding and ROI by industry (tree map)
total_funding_by_industry_graph = px.treemap(
                                             total_funding_by_industry, 
                                             path=[px.Constant("Industry"), 'Industry', "Company"], 
                                             values='Funding',
                                             color='ROI', color_continuous_scale='viridis'
                                            )
total_funding_by_industry_graph.update_traces(root_color="black")
total_funding_by_industry_graph.update_layout(
                                              plot_bgcolor = "rgba(0,0,0,0)", 
                                              paper_bgcolor = "rgba(0,0,0,0)", 
                                              xaxis_showgrid=False, 
                                              yaxis_showgrid=False,
                                              font_color="#FFFFFF"
                                              )
total_funding_by_industry_graph.update_xaxes(showline=True, linewidth=1, linecolor='#585858')
total_funding_by_industry_graph.update_yaxes(showline=True, linewidth=1, linecolor='#585858')
total_funding_by_industry_graph['layout'].update(margin=dict(l=10,r=10,b=20,t=20))
total_funding_by_industry_graph.data[0]['textfont']['color'] = "#FFFFFF"

