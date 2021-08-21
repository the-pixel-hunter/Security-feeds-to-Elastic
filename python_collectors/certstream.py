import certstream
import logging
from elasticsearch import Elasticsearch
import time

elastic_url = "http://localhost:9200/"
elastic_ssl_verify = False
elastic_index = "certstream"
elastic_pipelane_name = "certstream_to_elastic"

def print_callback(message, context):

    logging.debug("Message -> {}".format(message))

    if message['message_type'] == "heartbeat":
        logging.debug("Message -> Heartbeat recived...")
        return

    if message['message_type'] == "certificate_update":
        elastic_json = message['data']
        all_domains = message['data']['leaf_cert']['all_domains']

        if len(all_domains) == 0:
            all_domains[0] = "NULL"
        else:
            elastic_json['leaf_cert']['domain'] = all_domains[0]

        elastic_connection.index(elastic_index, elastic_json,  pipeline=elastic_pipelane_name)	
    
if __name__ == "__main__":
    elastic_connection = Elasticsearch([elastic_url],verify_certs=elastic_ssl_verify)
    logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(message)s', level=logging.INFO)
    while True:
        try:
            certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io/')
        except:
            print("Error Sleeping for 5s")
            time.sleep(5)