import pandas as pd, os
import plotly.express as px

def deathChart():
    # Gather Paths to local Data Sources
    jhuFolder = "c:\\temp\\covid19\\jhu\\"
    CDCExcessFolder = "c:\\temp\\covid19\\CDCExcess\\"
    covidTrackingFolder = "c:\\temp\\covid19\\covidtracking\\"

    # Build John Hopkins Chart
    chartJHU = False
    chartJHU = pd.concat(pd.read_csv(jhuFolder + csv) for csv in os.listdir(jhuFolder))
    chartJHU = chartJHU.rename(columns={'Province_State': 'Location', "Last_Update": "Date", "Deaths": "John Hopkins Total Deaths"})
    chartJHU = chartJHU[chartJHU["Location"] != "Recovered" ]

    # Build CDC Chart
    chartCDCExcess = pd.read_csv(CDCExcessFolder + "CDCExcess.csv")
    chartCDCExcess = chartCDCExcess.rename(columns={"State": "Location"})

    # Build covidtracking.com Charts
    chartCTS = pd.read_csv(covidTrackingFolder + "covidtrackingstates.csv")
    chartCTS = chartCTS.rename(columns={'state': 'Location', "death": "covidtracking.com Total Deaths"})
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
    chartCTU = chartCTU.rename(columns={'state': 'Location', "death": "covidtracking.com Total Deaths"})
    chartCTU["Location"] = "United States"
    chartCTU = chartCTU.loc[chartCTU["dateChecked"].str.contains('(?!2020-01)^202')]

    #Build State list based on John Hopkins List - As it's a giant spreadsheet
    states = set(chartJHU['Location'])
    states = list(states)
    states = states + ["United States"]
    states = sorted(states)

    # Customize Lists into smaller chunks for plotting - Specifically Higher CDC Estimates
    chartCDCHigher = chartCDCExcess.loc[chartCDCExcess["Type"] == "Predicted (weighted)"]
    chartCDCHigher = chartCDCHigher.loc[chartCDCHigher["Outcome"] == "All causes"]
    chartCDCHigher = chartCDCHigher.loc[chartCDCHigher["Week Ending Date"].str.contains('(?!2020-01)^202')]
    chartCDCHigher = chartCDCHigher.rename(columns={'Excess Higher Estimate': 'CDC Excess Higher Estimate', "Week Ending Date": "Date"})

    # New york was divided into city/state, so this brings them back together
    chartCDCHigherNY = chartCDCHigher.loc[chartCDCHigher["Location"].str.contains("New York")] # Corrects New York
    chartCDCHigherNY['CDC Excess Higher Estimate'] = chartCDCHigherNY.groupby('Date')['CDC Excess Higher Estimate'].transform('sum') # Corrects New York
    chartCDCHigher = chartCDCHigher.replace("New York", "This Doesn't Exist") # Corrects New York

    # Customize Lists into smaller chunks for plotting - Specifically Lower CDC Estimates
    chartCDCLower = chartCDCExcess.loc[chartCDCExcess["Type"] == "Predicted (weighted)"]
    chartCDCLower = chartCDCLower.loc[chartCDCLower["Outcome"] == "All causes"]
    chartCDCLower = chartCDCLower.loc[chartCDCLower["Week Ending Date"].str.contains('(?!2020-01)^202')]
    chartCDCLower = chartCDCLower.rename(columns={'Excess Lower Estimate': 'CDC Excess Lower Estimate', "Week Ending Date": "Date"})

    # New york was divided into city/state, so this brings them back together
    chartCDCLowerNY = chartCDCLower.loc[chartCDCLower["Location"].str.contains("New York")] # Corrects New York
    chartCDCLowerNY['CDC Excess Lower Estimate'] = chartCDCLowerNY.groupby('Date')['CDC Excess Lower Estimate'].transform('sum') # Corrects New York
    chartCDCLower = chartCDCLower.replace("New York", "This Doesn't Exist") # Corrects New York

    # Build initial plot line from John Hopkins Data
    fig = px.line(chartJHU, x='Date', y = "John Hopkins Total Deaths", title='Deaths by Location', line_group="Location", color="Location")

    # Build and Add Plot Line of CDC Excess Deaths added to graph
    for state in states:
        try:
            chartTempHigher = chartCDCHigher.loc[chartCDCHigher["Location"] == state]
            chartTempLower = chartCDCLower.loc[chartCDCLower["Location"] == state]
            chartTempHigher['CDC Excess Higher Estimate'] = chartTempHigher['CDC Excess Higher Estimate'].rolling(min_periods=1, window=100).sum()
            chartTempLower['CDC Excess Lower Estimate'] = chartTempLower['CDC Excess Lower Estimate'].rolling(min_periods=1, window=100).sum()
            fig.add_trace(px.line(chartTempHigher, x="Date", y='CDC Excess Higher Estimate', title="Excess Deaths Upper Limit", line_group="Location", color="Location", color_discrete_map={state: "red"}).data[0])
            fig.add_trace(px.line(chartTempLower, x="Date", y='CDC Excess Lower Estimate', title="Excess Deaths Lower Limit", line_group="Location", color="Location", color_discrete_map={state: "blue"}).data[0])
        except: continue

    #Build and add plot line for covidtracking to graph
    for state in states:
        try:
            chartCTStemp = chartCTS.loc[chartCTS["Location"] == state]
            fig.add_trace(px.line(chartCTStemp, x="dateModified", y='covidtracking.com Total Deaths', title="covidtracking.com Total Deaths", line_group="Location", color="Location", color_discrete_map={state: "black"}).data[0])
        except: continue
    fig.add_trace(px.line(chartCTU, x="dateChecked", y='covidtracking.com Total Deaths', title="covidtracking.com Total Deaths", line_group="Location", color="Location", color_discrete_map={"United States": "black"}).data[0])


    # These are to add up New york numbers since they're divided (previously city and state)
    chartCDCLowerNY['CDC Excess Lower Estimate'] = chartCDCLowerNY['CDC Excess Lower Estimate'].rolling(min_periods=1, window=100).sum()
    fig.add_trace(px.line(chartCDCLowerNY, x="Date", y='CDC Excess Lower Estimate', title="Excess Deaths Lower Limit", line_group="Location", color="Location", color_discrete_map={"New York": "blue"}).data[0])
    chartCDCHigherNY['CDC Excess Higher Estimate'] = chartCDCHigherNY['CDC Excess Higher Estimate'].rolling(min_periods=1, window=100).sum()
    fig.add_trace(px.line(chartCDCHigherNY, x="Date", y='CDC Excess Higher Estimate', title="Excess CDC Excess Higher Estimate", line_group="Location", color="Location", color_discrete_map={"New York": "red"}).data[0])

    # Plot sEntire USA John Hopkins Numbers onto graph
    chartUSAJHU = chartJHU
    chartUSAJHU["John Hopkins Total Deaths"] = chartUSAJHU.groupby('Date')["John Hopkins Total Deaths"].transform('sum') # Combines USA
    chartUSAJHU = chartUSAJHU.loc[chartUSAJHU["Location"] == "Alabama"] # Combines USA
    chartUSAJHU = chartUSAJHU.replace("Alabama", "United States") # Combines USA
    fig.add_trace(px.line(chartUSAJHU, x="Date", y="John Hopkins Total Deaths", title="John Hopkins Total Deaths", line_group="Location", color="Location", color_discrete_map={"United States": "green"}).data[0])
    # updates the look of the graph
    fig.update_layout(
        height=600,
        autosize=True,
        margin=dict(t=0, b=0, l=0, r=0),
        template="plotly_white",
        hovermode="x",
        yaxis_title = "Total Deaths",
        xaxis_title = "Date"
    )
    return fig

def casesChart():
    # Gather Paths to local Data Sources
    jhuFolder = "c:\\temp\\covid19\\jhu\\"
    CDCExcessFolder = "c:\\temp\\covid19\\CDCExcess\\"
    covidTrackingFolder = "c:\\temp\\covid19\\covidtracking\\"

    # Build John Hopkins Chart
    chartJHU = False
    chartJHU = pd.concat(pd.read_csv(jhuFolder + csv) for csv in os.listdir(jhuFolder))
    chartJHU = chartJHU.rename(columns={'Province_State': 'Location', "Last_Update": "Date", "Confirmed": "John Hopkins Total Cases"})
    chartJHU = chartJHU[chartJHU["Location"] != "Recovered" ]

    # Build covidtracking.com Charts
    chartCTS = pd.read_csv(covidTrackingFolder + "covidtrackingstates.csv")
    chartCTS = chartCTS.rename(columns={'state': 'Location', "positive": "covidtracking.com Total Cases"})
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
    chartCTU = chartCTU.rename(columns={'state': 'Location', "positive": "covidtracking.com Total Cases"})
    chartCTU["Location"] = "United States"
    chartCTU = chartCTU.loc[chartCTU["dateChecked"].str.contains('(?!2020-01)^202')]

    #Build State list based on John Hopkins List - As it's a giant spreadsheet
    states = set(chartJHU['Location'])
    states = list(states)
    states = states + ["United States"]
    states = sorted(states)

    # Build initial plot line from John Hopkins Data
    fig = px.line(chartJHU, x='Date', y = "John Hopkins Total Cases", title='Cases by Location', line_group="Location", color="Location")

    #Build and add plot line for covidtracking to graph
    for state in states:
        try:
            chartCTStemp = chartCTS.loc[chartCTS["Location"] == state]
            fig.add_trace(px.line(chartCTStemp, x="dateModified", y='covidtracking.com Total Cases', title="covidtracking.com Total Cases", line_group="Location", color="Location", color_discrete_map={state: "black"}).data[0])
        except: continue
    fig.add_trace(px.line(chartCTU, x="dateChecked", y='covidtracking.com Total Cases', title="covidtracking.com Total Cases", line_group="Location", color="Location", color_discrete_map={"United States": "black"}).data[0])

    # Plots Entire USA John Hopkins Numbers onto graph
    chartUSAJHU = chartJHU
    chartUSAJHU["John Hopkins Total Cases"] = chartUSAJHU.groupby('Date')["John Hopkins Total Cases"].transform('sum') # Combines USA
    chartUSAJHU = chartUSAJHU.loc[chartUSAJHU["Location"] == "Alabama"] # Combines USA
    chartUSAJHU = chartUSAJHU.replace("Alabama", "United States") # Combines USA
    fig.add_trace(px.line(chartUSAJHU, x="Date", y="John Hopkins Total Cases", title="John Hopkins Total Cases", line_group="Location", color="Location", color_discrete_map={"United States": "green"}).data[0])
    # updates the look of the graph
    fig.update_layout(
        height=600,
        autosize=True,

        margin=dict(t=0, b=0, l=0, r=0),
        template="plotly_white",
        hovermode="x",
        yaxis_title="Total Cases",
        xaxis_title="Date"

    )
    return fig


def deathDayChart():
    # Gather Paths to local Data Sources
    jhuFolder = "c:\\temp\\covid19\\jhu\\"
    CDCExcessFolder = "c:\\temp\\covid19\\CDCExcess\\"
    covidTrackingFolder = "c:\\temp\\covid19\\covidtracking\\"

    # Build John Hopkins Chart
    chartJHU = False
    chartJHU = pd.concat(pd.read_csv(jhuFolder + csv) for csv in os.listdir(jhuFolder))
    chartJHU = chartJHU.rename(columns={'Province_State': 'Location', "Last_Update": "Date", "Deaths": "John Hopkins Deaths Per Day"})
    chartJHU = chartJHU[chartJHU["Location"] != "Recovered" ]

    # Build CDC Chart
    chartCDCExcess = pd.read_csv(CDCExcessFolder + "CDCExcess.csv")
    chartCDCExcess = chartCDCExcess.rename(columns={"State": "Location"})

    # Build covidtracking.com Charts
    chartCTS = pd.read_csv(covidTrackingFolder + "covidtrackingstates.csv")
    chartCTS = chartCTS.rename(columns={'state': 'Location', "deathIncrease": "covidtracking.com Deaths Per Day"})
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
    chartCTU = chartCTU.rename(columns={'state': 'Location', "deathIncrease": "covidtracking.com Deaths Per Day"})
    chartCTU["Location"] = "United States"
    chartCTU = chartCTU.loc[chartCTU["dateChecked"].str.contains('(?!2020-01)^202')]

    #Build State list based on John Hopkins List - As it's a giant spreadsheet
    states = set(chartJHU['Location'])
    states = list(states)
    states = states + ["United States"]
    states = sorted(states)

    # Build initial plot line from John Hopkins Data
    fig = px.line()

    for state in states:
        try:
            chartJHUTemp = chartJHU.loc[chartJHU["Location"] == state]
            chartJHUTemp['John Hopkins Deaths Per Day'] = chartJHUTemp['John Hopkins Deaths Per Day'].diff()
            fig.add_trace(px.line(chartJHUTemp, x='Date', y = "John Hopkins Deaths Per Day", title='Deaths by Location', line_group="Location", color="Location",
                                  color_discrete_map={state: "green"}).data[0])
        except: continue

    # Customize Lists into smaller chunks for plotting - Specifically Higher CDC Estimates
    chartCDCHigher = chartCDCExcess.loc[chartCDCExcess["Type"] == "Predicted (weighted)"]
    chartCDCHigher = chartCDCHigher.loc[chartCDCHigher["Outcome"] == "All causes"]
    chartCDCHigher = chartCDCHigher.loc[chartCDCHigher["Week Ending Date"].str.contains('(?!2020-01)^202')]
    chartCDCHigher = chartCDCHigher.rename(columns={'Excess Higher Estimate': 'CDC Excess Higher Estimate (week avg)', "Week Ending Date": "Date"})

    # New york was divided into city/state, so this brings them back together
    chartCDCHigherNY = chartCDCHigher.loc[chartCDCHigher["Location"].str.contains("New York")] # Corrects New York
    chartCDCHigherNY['CDC Excess Higher Estimate (week avg)'] = chartCDCHigherNY.groupby('Date')['CDC Excess Higher Estimate (week avg)'].transform('sum') # Corrects New York
    chartCDCHigher = chartCDCHigher.replace("New York", "This Doesn't Exist") # Corrects New York

    # Customize Lists into smaller chunks for plotting - Specifically Lower CDC Estimate (week avg)s
    chartCDCLower = chartCDCExcess.loc[chartCDCExcess["Type"] == "Predicted (weighted)"]
    chartCDCLower = chartCDCLower.loc[chartCDCLower["Outcome"] == "All causes"]
    chartCDCLower = chartCDCLower.loc[chartCDCLower["Week Ending Date"].str.contains('(?!2020-01)^202')]
    chartCDCLower = chartCDCLower.rename(columns={'Excess Lower Estimate': 'CDC Excess Lower Estimate (week avg)', "Week Ending Date": "Date"})

    # New york was divided into city/state, so this brings them back together
    chartCDCLowerNY = chartCDCLower.loc[chartCDCLower["Location"].str.contains("New York")] # Corrects New York
    chartCDCLowerNY['CDC Excess Lower Estimate (week avg)'] = chartCDCLowerNY.groupby('Date')['CDC Excess Lower Estimate (week avg)'].transform('sum') # Corrects New York
    chartCDCLower = chartCDCLower.replace("New York", "This Doesn't Exist") # Corrects New York

    for state in states:
        try:
            chartTempHigher = chartCDCHigher.loc[chartCDCHigher["Location"] == state]
            chartTempLower = chartCDCLower.loc[chartCDCLower["Location"] == state]
            chartTempHigher['CDC Excess Higher Estimate (week avg)'] = chartTempHigher['CDC Excess Higher Estimate (week avg)'].floordiv(7)
            chartTempLower['CDC Excess Lower Estimate (week avg)'] = chartTempLower['CDC Excess Lower Estimate (week avg)'].floordiv(7)
            fig.add_trace(px.line(chartTempHigher, x="Date", y='CDC Excess Higher Estimate (week avg)', title="Excess Deaths Upper Limit", line_group="Location", color="Location", color_discrete_map={state: "red"}).data[0])
            fig.add_trace(px.line(chartTempLower, x="Date", y='CDC Excess Lower Estimate (week avg)', title="Excess Deaths Lower Limit", line_group="Location", color="Location", color_discrete_map={state: "blue"}).data[0])
        except: continue

    #Build and add plot line for covidtracking to graph
    for state in states:
        try:
            chartCTStemp = chartCTS.loc[chartCTS["Location"] == state]
            fig.add_trace(px.line(chartCTStemp, x="dateModified", y='covidtracking.com Deaths Per Day', title="covidtracking.com Deaths Per Day", line_group="Location", color="Location", color_discrete_map={state: "black"}).data[0])
        except: continue
    fig.add_trace(px.line(chartCTU, x="dateChecked", y='covidtracking.com Deaths Per Day', title="covidtracking.com Deaths Per Day", line_group="Location", color="Location", color_discrete_map={"United States": "black"}).data[0])

    # Plot sEntire USA John Hopkins Numbers onto graph
    chartUSAJHU = chartJHU
    chartUSAJHU["John Hopkins Deaths Per Day"] = chartUSAJHU.groupby('Date')["John Hopkins Deaths Per Day"].transform('sum') # Combines USA
    chartUSAJHU = chartUSAJHU.loc[chartUSAJHU["Location"] == "Alabama"] # Combines USA
    chartUSAJHU['John Hopkins Deaths Per Day'] = chartUSAJHU['John Hopkins Deaths Per Day'].diff()
    chartUSAJHU = chartUSAJHU.replace("Alabama", "United States") # Combines USA
    fig.add_trace(px.line(chartUSAJHU, x="Date", y="John Hopkins Deaths Per Day", title="John Hopkins Deaths Per Day", line_group="Location", color="Location", color_discrete_map={"United States": "green"}).data[0])
    # updates the look of the graph
    fig.update_layout(
        height=600,
        autosize=True,
        margin=dict(t=0, b=0, l=0, r=0),
        template="plotly_white",
        hovermode="x",
        yaxis_title="Deaths Per Day",
        xaxis_title="Date"

    )
    return fig

def casesDayChart():
    # Gather Paths to local Data Sources
    jhuFolder = "c:\\temp\\covid19\\jhu\\"
    CDCExcessFolder = "c:\\temp\\covid19\\CDCExcess\\"
    covidTrackingFolder = "c:\\temp\\covid19\\covidtracking\\"

    # Build John Hopkins Chart
    chartJHU = False
    chartJHU = pd.concat(pd.read_csv(jhuFolder + csv) for csv in os.listdir(jhuFolder))
    chartJHU = chartJHU.rename(columns={'Province_State': 'Location', "Last_Update": "Date", "Confirmed": "John Hopkins Cases Per Day"})
    chartJHU = chartJHU[chartJHU["Location"] != "Recovered" ]

    # Build covidtracking.com Charts
    chartCTS = pd.read_csv(covidTrackingFolder + "covidtrackingstates.csv")
    chartCTS = chartCTS.rename(columns={'state': 'Location', "positiveIncrease": "covidtracking.com Cases Per Day"})
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
    chartCTU = chartCTU.rename(columns={'state': 'Location', "positiveIncrease": "covidtracking.com Cases Per Day"})
    chartCTU["Location"] = "United States"
    chartCTU = chartCTU.loc[chartCTU["dateChecked"].str.contains('(?!2020-01)^202')]

    #Build State list based on John Hopkins List - As it's a giant spreadsheet
    states = set(chartJHU['Location'])
    states = list(states)
    states = states + ["United States"]
    states = sorted(states)

    # Build initial plot line from John Hopkins Data
    fig = px.line()

    for state in states:
        try:
            chartJHUTemp = chartJHU.loc[chartJHU["Location"] == state]
            chartJHUTemp['John Hopkins Cases Per Day'] = chartJHUTemp['John Hopkins Cases Per Day'].diff()
            fig.add_trace(px.line(chartJHUTemp, x='Date', y = "John Hopkins Cases Per Day", title='Cases by Location', line_group="Location", color="Location",
                                  color_discrete_map={state: "green"}).data[0])
        except: continue
    #Build and add plot line for covidtracking to graph

    for state in states:
        try:
            chartCTStemp = chartCTS.loc[chartCTS["Location"] == state]
            fig.add_trace(px.line(chartCTStemp, x="dateModified", y='covidtracking.com Cases Per Day', title="covidtracking.com Cases Per Day", line_group="Location", color="Location", color_discrete_map={state: "black"}).data[0])
        except: continue
    fig.add_trace(px.line(chartCTU, x="dateChecked", y='covidtracking.com Cases Per Day', title="covidtracking.com Cases Per Day", line_group="Location", color="Location", color_discrete_map={"United States": "black"}).data[0])

#    Plots Entire USA John Hopkins Numbers onto graph
    chartUSAJHU = chartJHU
    chartUSAJHU["John Hopkins Cases Per Day"] = chartUSAJHU.groupby('Date')["John Hopkins Cases Per Day"].transform('sum') # Combines USA
    chartUSAJHU = chartUSAJHU.loc[chartUSAJHU["Location"] == "Alabama"] # Combines USA
    chartUSAJHU['John Hopkins Cases Per Day'] = chartUSAJHU['John Hopkins Cases Per Day'].diff()
    chartUSAJHU = chartUSAJHU.replace("Alabama", "United States") # Combines USA
    fig.add_trace(px.line(chartUSAJHU, x="Date", y="John Hopkins Cases Per Day", title="John Hopkins Cases Per Day", line_group="Location", color="Location", color_discrete_map={"United States": "green"}).data[0])

#    updates the look of the graph
    fig.update_layout(
        height=600,
        autosize=True,

        margin=dict(t=0, b=0, l=0, r=0),
        template="plotly_white",
        hovermode="x",
        yaxis_title="Cases Per Day",
        xaxis_title="Date"

    )
    return fig

