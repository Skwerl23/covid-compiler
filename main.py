import pandas as pd, os
import plotly.express as px
import dataupdater as dUpdate
import plotly as pl

# These functions pull the latest Date sources
dUpdate.JHU()
dUpdate.CDCExcess()
dUpdate.covidTracking()

# Gather Paths to local Data Sources
jhuFolder = "c:\\temp\\covid19\\jhu\\"
CDCExcessFolder = "c:\\temp\\covid19\\CDCExcess\\"
covidTrackingFolder = "c:\\temp\\covid19\\covidtracking\\"

# Build John Hopkins Chart
chartJHU = False
chartJHU = pd.concat(pd.read_csv(jhuFolder + csv) for csv in os.listdir(jhuFolder))
chartJHU = chartJHU.rename(columns={'Province_State': 'Location', "Last_Update": "Date", "Deaths": "John Hopkins Death Count"})
chartJHU = chartJHU[chartJHU["Location"] != "Recovered" ]

# Build CDC Chart
chartCDCExcess = pd.read_csv(CDCExcessFolder + "CDCExcess.csv")
chartCDCExcess = chartCDCExcess.rename(columns={"State": "Location"})

# Build covidtracking Charts

chartCTS = pd.read_csv(covidTrackingFolder + "covidtrackingstates.csv")
chartCTS = chartCTS.rename(columns={'state': 'Location', "death": "covidtracking.com Death Count"})
chartCTS = chartCTS.replace('AK', 'Alaska')
chartCTS = chartCTS.replace('AL', 'Alabama')
chartCTS = chartCTS.replace('AR', 'Arkansas')
chartCTS = chartCTS.replace('AS', 'American Samoa')
chartCTS = chartCTS.replace('AZ', 'Arizona')
chartCTS = chartCTS.replace('CA', 'California')
chartCTS = chartCTS.replace('CO', 'Colorado')
chartCTS = chartCTS.replace('CT', 'Connecticut')
chartCTS = chartCTS.replace('DC', 'District of Columbia')
chartCTS = chartCTS.replace('DE', 'Delaware')
chartCTS = chartCTS.replace('FL', 'Florida')
chartCTS = chartCTS.replace('GA', 'Georgia')
chartCTS = chartCTS.replace('GU', 'Guam')
chartCTS = chartCTS.replace('HI', 'Hawaii')
chartCTS = chartCTS.replace('IA', 'Iowa')
chartCTS = chartCTS.replace('ID', 'Idaho')
chartCTS = chartCTS.replace('IL', 'Illinois')
chartCTS = chartCTS.replace('IN', 'Indiana')
chartCTS = chartCTS.replace('KS', 'Kansas')
chartCTS = chartCTS.replace('KY', 'Kentucky')
chartCTS = chartCTS.replace('LA', 'Louisiana')
chartCTS = chartCTS.replace('MA', 'Maine')
chartCTS = chartCTS.replace('MD', 'Maryland')
chartCTS = chartCTS.replace('ME', 'Massachusetts')
chartCTS = chartCTS.replace('MI', 'Michigan')
chartCTS = chartCTS.replace('MN', 'Minnesota')
chartCTS = chartCTS.replace('MO', 'Missouri')
chartCTS = chartCTS.replace('MP', 'Northern Mariana Islands')
chartCTS = chartCTS.replace('MS', 'Mississippi')
chartCTS = chartCTS.replace('MT', 'Montana')
chartCTS = chartCTS.replace('NC', 'North Carolina')
chartCTS = chartCTS.replace('ND', 'North Dakota')
chartCTS = chartCTS.replace('NE', 'Nebraska')
chartCTS = chartCTS.replace('NH', 'New Hampshire')
chartCTS = chartCTS.replace('NJ', 'New Jersey')
chartCTS = chartCTS.replace('NM', 'New Mexico')
chartCTS = chartCTS.replace('NV', 'Nevada')
chartCTS = chartCTS.replace('NY', 'New York')
chartCTS = chartCTS.replace('OH', 'Ohio')
chartCTS = chartCTS.replace('OK', 'Oklahoma')
chartCTS = chartCTS.replace('OR', 'Oregon')
chartCTS = chartCTS.replace('PA', 'Pennsylvania')
chartCTS = chartCTS.replace('PR', 'Puerto Rico')
chartCTS = chartCTS.replace('RI', 'Rhode Island')
chartCTS = chartCTS.replace('SC', 'South Carolina')
chartCTS = chartCTS.replace('SD', 'South Dakota')
chartCTS = chartCTS.replace('TN', 'Tennessee')
chartCTS = chartCTS.replace('TX', 'Texas')
chartCTS = chartCTS.replace('UT', 'Utah')
chartCTS = chartCTS.replace('VA', 'Virginia')
chartCTS = chartCTS.replace('VI', 'Virgin Islands')
chartCTS = chartCTS.replace('VT', 'Vermont')
chartCTS = chartCTS.replace('WA', 'Washington')
chartCTS = chartCTS.replace('WI', 'Wisconsin')
chartCTS = chartCTS.replace('WV', 'West Virginia')
chartCTS = chartCTS.replace('WY', 'Wyoming')

chartCTU = pd.read_csv(covidTrackingFolder + "covidtrackingusa.csv")
chartCTU = chartCTU.rename(columns={'state': 'Location', "death": "covidtracking.com Death Count"})
chartCTU["Location"] = "United States"
chartCTU = chartCTU.loc[chartCTU["dateChecked"].str.contains('^2020-03|^2020-04|^2020-05|^2020-06')]

#Build State list based on John Hopkins List - As it's a giant spreadsheet
states = set(chartJHU['Location'])

# Creates button for drop down options - Currently Not Used
list_updatemenus = [{'label': 'All', 'method': 'update', 'args': [{'visible': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]}, {'title': 'All'}]}]
for n, state in enumerate(states):
    visible = [False] * len(states)
    visible[n] = True
    temp_dict = dict(label = str(state),
                 method = 'update',
                 args = [{'visible': visible},
                         {'title': state}])
    list_updatemenus.append(temp_dict)

# Customize Lists into smaller chunks for plotting - Specifically Higher CDC Estimates
chartCDCHigher = chartCDCExcess.loc[chartCDCExcess["Type"] == "Predicted (weighted)"]
chartCDCHigher = chartCDCHigher.loc[chartCDCHigher["Outcome"] == "All causes"]
chartCDCHigher = chartCDCHigher.loc[chartCDCHigher["Week Ending Date"].str.contains('^2020-03|^2020-04|^2020-05|^2020-06')]
chartCDCHigher = chartCDCHigher.rename(columns={'Excess Higher Estimate': 'CDC Excess Higher Estimate', "Week Ending Date": "Date"})

# New york was divided into city/state, so this brings them back together
chartCDCHigherNY = chartCDCHigher.loc[chartCDCHigher["Location"].str.contains("New York")] # Corrects New York
chartCDCHigherNY['CDC Excess Higher Estimate'] = chartCDCHigherNY.groupby('Date')['CDC Excess Higher Estimate'].transform('sum') # Corrects New York
chartCDCHigher = chartCDCHigher.replace("New York", "This Doesn't Exist") # Corrects New York

# Customize Lists into smaller chunks for plotting - Specifically Lower CDC Estimates
chartCDCLower = chartCDCExcess.loc[chartCDCExcess["Type"] == "Predicted (weighted)"]
chartCDCLower = chartCDCLower.loc[chartCDCLower["Outcome"] == "All causes"]
chartCDCLower = chartCDCLower.loc[chartCDCLower["Week Ending Date"].str.contains('^2020-03|^2020-04|^2020-05|^2020-06')]
chartCDCLower = chartCDCLower.rename(columns={'Excess Lower Estimate': 'CDC Excess Lower Estimate', "Week Ending Date": "Date"})

# New york was divided into city/state, so this brings them back together
chartCDCLowerNY = chartCDCLower.loc[chartCDCLower["Location"].str.contains("New York")] # Corrects New York
chartCDCLowerNY['CDC Excess Lower Estimate'] = chartCDCLowerNY.groupby('Date')['CDC Excess Lower Estimate'].transform('sum') # Corrects New York
chartCDCLower = chartCDCLower.replace("New York", "This Doesn't Exist") # Corrects New York

# Build initial plot line from John Hopkins Data
fig = px.line(chartJHU, x='Date', y = "John Hopkins Death Count", title='Deaths by Location', line_group="Location", color="Location")

# Build and Add Plot Line of CDC Excess Deaths added to graph
for place in states:
    try:
        chartTempHigher = chartCDCHigher.loc[chartCDCHigher["Location"] == place]
        chartTempLower = chartCDCLower.loc[chartCDCLower["Location"] == place]
        chartTempHigher['CDC Excess Higher Estimate'] = chartTempHigher['CDC Excess Higher Estimate'].rolling(min_periods=1, window=15).sum()
        chartTempLower['CDC Excess Lower Estimate'] = chartTempLower['CDC Excess Lower Estimate'].rolling(min_periods=1, window=15).sum()
        figtemp2 = px.line(chartTempHigher, x="Date", y='CDC Excess Higher Estimate', title="Excess Deaths Upper Limit", line_group="Location", color="Location", color_discrete_map={place: "red"})
        figtemp3 = px.line(chartTempLower, x="Date", y='CDC Excess Lower Estimate', title="Excess Deaths Lower Limit", line_group="Location", color="Location", color_discrete_map={place: "blue"})
        fig.add_trace(figtemp2.data[0])
        fig.add_trace(figtemp3.data[0])
    except: continue

#Build and add plot line for covidtracking to graph
for place in states:
    try:
        chartCTStemp = chartCTS.loc[chartCTS["Location"] == place]
        figtemp2 = px.line(chartCTStemp, x="dateModified", y='covidtracking.com Death Count', title="covidtracking.com Death Count", line_group="Location", color="Location", color_discrete_map={place: "black"})
        fig.add_trace(figtemp2.data[0])
    except: continue
fig2 = px.line(chartCTU, x="dateChecked", y='covidtracking.com Death Count', title="covidtracking.com Death Count", line_group="Location", color="Location", color_discrete_map={"United States": "black"})
fig.add_trace(fig2.data[0])


# These are to add up New york numbers since they're divided (previously city and state)
chartCDCLowerNY['CDC Excess Lower Estimate'] = chartCDCLowerNY['CDC Excess Lower Estimate'].rolling(min_periods=1, window=15).sum()
fig4 = px.line(chartCDCLowerNY, x="Date", y='CDC Excess Lower Estimate', title="Excess Deaths Lower Limit", line_group="Location", color="Location", color_discrete_map={"New York": "blue"})
fig.add_trace(fig4.data[0])
chartCDCHigherNY['CDC Excess Higher Estimate'] = chartCDCHigherNY['CDC Excess Higher Estimate'].rolling(min_periods=1, window=15).sum()
fig5 = px.line(chartCDCHigherNY, x="Date", y='CDC Excess Higher Estimate', title="Excess CDC Excess Higher Estimate", line_group="Location", color="Location", color_discrete_map={"New York": "red"})
fig.add_trace(fig5.data[0])

# Plots Entire USA CDC Numbers onto graph, as previously it's all states
chartUSAExcessHigher = chartCDCHigher.loc[chartCDCHigher["Location"] == "United States"]
chartUSAExcessHigher['CDC Excess Higher Estimate'] = chartUSAExcessHigher['CDC Excess Higher Estimate'].rolling(min_periods=1, window=15).sum()
figUSA = px.line(chartUSAExcessHigher, x="Date", y='CDC Excess Higher Estimate', title="Excess Deaths Lower Estimate", line_group="Location", color="Location", color_discrete_map={"United States": "red"})
fig.add_trace(figUSA.data[0])
chartUSAExcessLower = chartCDCLower.loc[chartCDCLower["Location"] == "United States"]
chartUSAExcessLower['CDC Excess Lower Estimate'] = chartUSAExcessLower['CDC Excess Lower Estimate'].rolling(min_periods=1, window=15).sum()
figUSAExcess = px.line(chartUSAExcessLower, x="Date", y='CDC Excess Lower Estimate', title="Excess Deaths Lower Estimate", line_group="Location", color="Location", color_discrete_map={"United States": "blue"})
fig.add_trace(figUSAExcess.data[0])

# Plot sEntire USA John Hopkins Numbers onto graph
chartUSAJHU = chartJHU
chartUSAJHU["John Hopkins Death Count"] = chartUSAJHU.groupby('Date')["John Hopkins Death Count"].transform('sum') # Combines USA
chartUSAJHU = chartUSAJHU.loc[chartUSAJHU["Location"] == "Alabama"] # Combines USA
chartUSAJHU = chartUSAJHU.replace("Alabama", "United States") # Combines USA
figUSAJHU = px.line(chartUSAJHU, x="Date", y="John Hopkins Death Count", title="John Hopkins Death Count", line_group="Location", color="Location", color_discrete_map={"United States": "green"})
fig.add_trace(figUSAJHU.data[0])

# updates the look of the graph
fig.update_layout(
#    updatemenus=list([dict(buttons=list_updatemenus)]),
    height=600,
    autosize=True,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
    hovermode="x"
)

# Creates HTML file temp-plot and opens it
pl.offline.plot(fig)
