from datetime import datetime, timedelta
import requests
import os

def nvd():
    # save the date of 24 hours ago as last_mod_date, then format it for use in the API call
    last_mod_date = str(datetime.today() - timedelta(hours=1))[:-3]
    last_mod_date = (last_mod_date.replace(".", ":").replace(" ", "T") + "%20UTC%2B10:00")
    url = "https://services.nvd.nist.gov/rest/json/cves/1.0?"
    last_mod_pram = "modStartDate=" + last_mod_date
    page_limit = "resultsPerPage=5000"
    nvd_vulns = requests.get(url + last_mod_pram + '&' + page_limit)
    
    
    
    # open and save nvd_$date, then save the response
    now = str(datetime.today()).replace(" ", "_")
    todays_vulns = open("/home/vulnerabilities/nvd/nvd_" + now + ".json", "w+")
    todays_vulns.write(nvd_vulns.text + "\n")
    todays_vulns.close()

nvd()