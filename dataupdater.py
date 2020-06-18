import datetime as dt
import re
import urllib.error
import urllib.parse
import urllib.request
import os

# prevents server checks more than 4x a day
def lastUpdate(folder):
    lastCheck = True
    today = dt.datetime.today() - dt.timedelta(hours=6)
    for file in os.listdir(folder):
        filetime = dt.datetime.fromtimestamp(
            os.path.getmtime(folder + file))
        if filetime >= today:
            lastCheck = False
            break
    return lastCheck

# Used to download files
def download(url, folder, file):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode("utf-8")
    f = open(folder + file, "w")
    f.write(str(webContent))
    f.close()

# updates log file
def log(folder):
    log = open(folder + "logs.log", "w")
    log.write("Last updated @ " + str(dt.datetime.today()))
    log.close

# Downloads the latest John Hopkins Database
def JHU():
    jhuFolder = "c:\\temp\\covid19\\jhu\\"
    try: os.mkdir(jhuFolder)
    except: pass
    lastCheck = lastUpdate(jhuFolder)
    if not lastCheck:
        print("JHU already up to date!")
    else:
        print("Updating JHU!")
        url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us'
        response = urllib.request.urlopen(url)
        webContent = response.read().decode("utf-8")
        webContent = set(re.findall('[0-9]{2}-[0-9]{2}-[0-9]{4}\.csv', webContent))
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/"
        jhuLocalList = list(os.listdir("c:\\temp\\covid19\\jhu"))
        for x in webContent:
            if x not in jhuLocalList:
                download(url+x, jhuFolder, x)
        log(jhuFolder)

# Downloads the latest CDC Excess Deaths
def CDCExcess():
    CDCExcessFolder = "c:\\temp\\covid19\\CDCExcess\\"
    file = "CDCExcess.csv"
    url = "https://data.cdc.gov/api/views/xkkf-xrst/rows.csv"
    try: os.mkdir(CDCExcessFolder)
    except: pass
    lastCheck = lastUpdate(CDCExcessFolder)
    if not lastCheck:
        print("CDC Excess Deaths already up to date!")
    else:
        print("Updating CDC Excess Deaths!")
            # If this URL changes, then the page https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm will need to be scraped
        download(url, CDCExcessFolder, file)
        log(CDCExcessFolder)

# Downloads the latest covidtracking.com database
def covidTracking():
    covidTrackingFolder = "c:\\temp\\covid19\\covidtracking\\"
    fileStates = "covidtrackingstates.csv"
    urlStates = "https://covidtracking.com/api/v1/states/daily.csv"
    fileUSA = "covidtrackingusa.csv"
    urlUSA = "https://covidtracking.com/api/v1/us/daily.csv"
    try: os.mkdir(covidTrackingFolder)
    except: pass
    lastCheck = lastUpdate(covidTrackingFolder)
    if not lastCheck:
        print("covidtracking.com already up to date!")
    else:
        print("Updating covidtracking.com!")
        download(urlStates, covidTrackingFolder, fileStates)
        download(urlUSA, covidTrackingFolder, fileUSA)
        log(covidTrackingFolder)
