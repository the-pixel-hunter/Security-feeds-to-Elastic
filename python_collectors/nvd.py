import requests
import datetime
import time
import json
from elasticsearch import Elasticsearch

elastic_url = "http://localhost:9200/"
elastic_ssl_verify = False
elastic_index = "intel-cves-nvd"
elastic_pipelane_name = "nvd_to_elastic"
BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=2000"
LOOKBACK_TIME = 60
start_index = 0
total_left = 0
step_value = 2000


def nvd_collect(start_from):
    start_index = "&startIndex=" + str(start_from)
    mod_prama = "&modStartDate=" + old_time()
   
    url = BASE_URL + start_index + mod_prama
    print("GET", url)
    response = requests.get(url)

    if response.status_code != 200:
        print("ERROR: unexpcted status code, ", response.status_code)
        return None
 

    response_json = json.loads(response.text)

    cves = response_json['result']['CVE_Items']
    if len(cves) != 0: 
        elastic_connection = Elasticsearch([elastic_url],verify_certs=elastic_ssl_verify)
        for cve in cves:
            doc_id = "nvd_" + str(cve['cve']['CVE_data_meta']['ID'])
            elastic_connection.index(elastic_index, cve,  id=doc_id,pipeline=elastic_pipelane_name)
    
    return response_json['totalResults']



def sleep_for_X_secounds(sleep_count):
    i = 0
    print("Sleeping for {}s...".format(sleep_count))
    for i in range(sleep_count):
        print(sleep_count - i)
        time.sleep(1)

def old_time():
    time_old = datetime.datetime.now() - datetime.timedelta(minutes=LOOKBACK_TIME)
    look_back_time = time_old.strftime("%Y-%m-%dT%H:%M:%S") + ":000%20UTC-00:00"
    return look_back_time


if __name__ == "__main__":

    while True:
        request_number = (start_index / step_value) + 1
        print("Request Number: {},  Start Index: {},  total: {}".format(request_number, start_index, total_left))
        total_left = nvd_collect(start_index)
        start_index += step_value

        if total_left == None:
            #Error
            break
        if total_left > start_index:
            if start_index == 70000 or start_index == 150000:   
                sleep_for_X_secounds(600)
            else:
                sleep_for_X_secounds(60)
        else:
            print("Total CVEs collected: {}".format(total_left))
            break
           