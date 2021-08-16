import requests
import datetime
import json
from elasticsearch import Elasticsearch

elastic_url = "http://localhost:9200/"
elastic_ssl_verify = False
elastic_index = "nvd"
elastic_pipelane_name = "nvd_cve"

time_old = datetime.datetime.now() - datetime.timedelta(minutes=65)
look_back_time = time_old.strftime("%Y-%m-%dT%H:%M:%S") + ":000%20UTC-00:00"

base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=2000"
mod_prama = "&modStartDate=" + look_back_time
url = base_url + mod_prama

response = requests.get(url)

if response.status_code != 200:
    print("ERROR: unexpcted status code, ", response.status_code)
    #try again
    exit()

response_json = json.loads(response.text)
cves = response_json['result']['CVE_Items']
if len(cves) != 0: 
    elastic_connection = Elasticsearch([elastic_url],verify_certs=elastic_ssl_verify)
    for cve in cves:
        elastic_connection.index(elastic_index, cve,  pipeline=elastic_pipelane_name)	


