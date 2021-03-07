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

- source: Author/Comapny
- types: Podcast, Blogs, News, Advisory, Raw Intel
- vendor: Google, Cisco, CrowdStrike, Elastic, Neutral 
- sub_catagorys: Technical, Vulnerablitys, IPs, Intel, Vendor, Reddit Group(/r NetSec)
- source_location: Worldwise, UK, USA, Europe, Asia

## To-Do
- [ ] Always More Security Feeds
- [ ] Add Podcast section
- [ ] More Dashboards
- [ ] Make use of Canvas
- [ ] Add Geo Data for Source
- [ ] Add more custom fields
- [ ] Install guide

## Future Projects 
- [ ] Security Twitter Pipelines
