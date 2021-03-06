# Secuity-RSS-Feeds

## Overview

Logstash RSS poll => Pipeles to add fields/modify => ElasticSearch => View in Kibana

- Install elasticsearch, Logstash, Kibana
- Download logstash pipelines,
- Add config to pipeline.yml file
- Create Index
- Import Obejects for fancy dashboards

### Tags
Tags are only used to ensure that the correct filters are applied to the correct feed

### Added Fields

- source: Author/Company
- types: Blogs, News, Advisory, Raw Intel
- vendor: Google, Cisco, CrowdStrike, Elastic, Neutral 
- sub_catagorys: Technical, Vulnerablitys, IPs, Intel, Vendor
- source_location: Worldwise, UK, USA, Europe, Asia

## To-Do
- [ ] Always More Security Feeds
- [ ] More Dashboards
- [ ] Make use of Canvas
- [ ] Add Geo Data for Source
- [ ] Add more custom fields
- [ ] Install guide

## Future Projects 
- [ ] Security Twitter Pipelines
