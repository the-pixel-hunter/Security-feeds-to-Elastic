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

## RSS Feeds Flow
RSS Feed => Logstash RSS poll => Pipeles to add fields/modify => ElasticSearch => View in Kibana

### RSS Added Fields
Fileds added for visuals:
- rss.source.name: common name for the source type example BHIS for Black Hill Information Security
- rss.source.name_full: full un-shortend name
- rss.feed.type: Should be one of, 'News', 'Blog', 'Advisoriy', 'Podcast'

### RSS visuals


## To-Do
- [ ] Always More RSS Feeds
- [ ] Add Podcast feeds /filter them out
- [ ] Add some more twitter account examples
- [ ] Add finish RSS feeds off
- [ ] Clean up pipelines
- [ ] Create Dashboards
- [ ] Create Mappings 
- [ ] Create Dashboards (Home, Twitter, RSS, CVE, etc)
- [ ] Canvas Viewing Option example 
- [ ] Add twitter pipelines regex match for CVE and IPs? 'CVE (?i)\bcve\-\d{4}-\d{4,7}'
- [ ] 
- [ ] Create install guide


- [ ] Add Certstream - https://medium.com/security-analytics/elasticphish-using-certstream-and-the-elastic-stack-for-phishing-intelligence-b03b86ad5cfe
