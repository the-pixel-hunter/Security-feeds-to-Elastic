# Elastic Security Feeds

## Overview

## Setup
- Install elasticsearch, Logstash, Kibana
- setup configs
- import templates
- Import Obejects for fancy dashboards

## RSS Feeds Flow
RSS Feed => Logstash RSS poll => Pipeles to add fields/modify => ElasticSearch => View in Kibana

### RSS Added Fields
Fileds added for visuals:
- rss.source.name: commonaly known name for the source type example BHIS for Black Hill Information Security
- rss.source.name_full: full un-shortend name of the source
- rss.feed.type: Should be one of, 'news', 'blog', 'advisoriy', 'podcast', 'reddit'

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
- [x] Add twitter pipelines regex match for CVE and IPs? 'CVE (?i)\bcve\-\d{4}-\d{4,7}'
- [ ] Create install guide

- [x] Add Certstream
