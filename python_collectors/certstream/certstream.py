
import certstream
import logging
import datetime
import certstream

def print_callback(message, context):

    logging.debug("Message -> {}".format(message))

    if message['message_type'] == "heartbeat":
        logging.debug("Message -> Heartbeat recived...")
        return

    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']

        if len(all_domains) == 0:
            domain = "NULL"
        else:
            domain = all_domains[0]
        
        day = 'today'	
        with open('certstream_{}.log'.format(day), 'a') as file:
        	file.write(u"[{}] {} (SAN: {})\n".format(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S'), domain, ", ".join(message['data']['leaf_cert']['all_domains'][1:])))
    return

def on_open():
	 logging.info("Connection successfully established!")

def on_error(instance, exception):
    # Instance is the CertStreamClient instance that barfed
	 logging.error("Exception in instance -> {}, Exception -> {}".format(instance, exception))

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(message)s', level=logging.INFO)
    certstream.listen_for_events(print_callback, on_open=on_open, on_error=on_error, url='wss://certstream.calidog.io/')
