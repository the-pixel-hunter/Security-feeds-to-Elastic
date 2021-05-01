# Elastic Security Feeds

## Overview


Twitter Stream => Logstash Twitter API => Pipeline => ElasticSearch => View in Kibana

- Install elasticsearch, Logstash, Kibana
- Download logstash pipelines,
- Add config to pipeline.yml file
- Create Index
- Import Obejects for fancy dashboards

## RSS Feeds

RSS Feed => Logstash RSS poll => Pipeles to add fields/modify => ElasticSearch => View in Kibana

### RSS Tags
Tags are only used to ensure that the correct filters are applied to the correct feed

### RSS Added Fields
Fileds added for visuals:

- source: Author/Comapny
- types: Podcast, Blogs, News, Advisory, Raw Intel
- continents:Worldwise, UK, USA, Europe, Asia

### RSS visuals


## To-Do
- [ ] Always More Security Feeds
- [ ] Add Podcast feeds
- [ ] More Dashboards
- [ ] Canvas Dash for twitter and RSS
- [ ] Maybe Geo Data
- [ ] Twitter tweets text analyises
- [ ] Install guide
- [ ] Add Certstream https://medium.com/security-analytics/elasticphish-using-certstream-and-the-elastic-stack-for-phishing-intelligence-b03b86ad5cfe
