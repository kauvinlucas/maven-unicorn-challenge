import plotly.express as px
import pandas as pd

# Import data
df = pd.read_csv("data/Unicorn_Companies.csv")

###########################
### Data cleaning steps ###
###########################

# Replace the duplicated company names
df.loc[40,"Company"] = 'Bolt (Estonia)'
df.loc[44,"Company"] = 'Bolt (US)'

# Replace mispelled category in "Industry"
df["Industry"] = df["Industry"].str.replace("intelligence", "Intelligence")

# Replace value in "Year Founded" of company "Yidian Zixun" to 2013
df.loc[714, "Year Founded"] = 2013

# Convert numerical columns to float type
df["Valuation"] = df["Valuation"].apply(lambda x: x.replace("B", "000000000").replace("$", "")).astype("float")
df["Funding"] = df["Funding"].apply(lambda x: x.replace("B", "000000000").replace("M", "000000").replace("$", "").replace("Unknown", "nan")).astype("float")

##########################
### Feature extraction ###
##########################

# Explode the elements in the column "Select Investors"
df["Select Investors"] = df["Select Investors"].astype("str").apply(lambda x: x.split(", "))
df = df.explode("Select Investors", ignore_index=False)

# Add "Year Joined" and "Quarter Joined"
df["Date Joined"] = df["Date Joined"].astype("datetime64[ns]")
df["Year Joined"] = df["Date Joined"].dt.year
df["Year/Quarter Joined"] = df["Date Joined"].dt.to_period('Q').astype("str")

# Add "Valuation-to-funding ratio"
df["ROI"] = (df["Valuation"] - df["Funding"]) / df["Funding"]

# Add "Year Founded to Joined"
df["Year Founded to Joined"] = df["Year Joined"] - df["Year Founded"]

# Drop companies that joined the Unicorn Club in 2007
df = df[~(df["Year Joined"] == 2007)]

# Add country ISO codes
df_gap_minder = px.data.gapminder().query("year==2007").drop_duplicates().loc[:,["country", "iso_alpha"]]
df = df.merge(df_gap_minder, left_on="Country", right_on="country").drop(columns="country")

# Filter first quater
df = df[df["Year/Quarter Joined"].str.endswith("Q1")]
