import certstream

certstream_url = 'wss://certstream.calidog.io'
domain_log = '/home/certstream/domains_log.json'


def handle(message, context):
    if message['message_type'] == "heartbeat":
        return

    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']
        print (all_domains)
        for domain in all_domains:
            with open(domain_log, 'a') as f:
                f.write("{}\n".format(domain))
    


if __name__ == '__main__':
    certstream.listen_for_events(handle, url=certstream_url)