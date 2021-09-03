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

