# Elastic Security Feeds

## Overview
A simple project that brings together many great open Projects and some of my own changes to pull a bunch of ONIST Sources and put them into a vairaty dashboards.

Twitter Stream => Logstash Twitter API => Pipeline => ElasticSearch => View in Kibana
RSS Feed => Logstas RSS Poller => Pipeline => ElasticSearch => View in Kibana
Certstream => Python-puller => Logstash File Reader => ElasticSearch => View in Kibana
Filebeat Threatintel = > ElasticSearch => View in Kibana

- Install elasticsearch, Logstash, Kibana
- Download logstash pipelines
- Add config to pipeline.yml file
- Create Inde(s)
- Import Obejects for fancy dashboards

## RSS Feeds

RSS Feed => Logstash RSS poll => Pipeles to add fields/modify => ElasticSearch => View in Kibana

### RSS Added Fields
Fileds added for visuals:

- rss.source.name
- rss.source.name_full:
- rss.feed.type: 
- rss.feed.url:
### RSS visuals


## To-Do
- [ ] Always More Security Feeds
- [ ] Add Podcast feeds
- [ ] More Dashboards
- [ ] Canvas Dash for twitter and RSS
- [ ] Twitter tweets text analyises
- [ ] Install guide
- [ ] Add Certstream https://medium.com/security-analytics/elasticphish-using-certstream-and-the-elastic-stack-for-phishing-intelligence-b03b86ad5cfe
