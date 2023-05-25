export SOLRUSER=frothkoetter
export SOLRPWD='CXXXXXX$'
curl -k -negotiate --user $SOLRUSER:$SOLRPWD -u : 'https://itz-search-demo-gateway.se-sandb.a465-9q4k.cloudera.site/itz-search-demo/cdp-proxy-api/solr/airlinedata_tweets/update?commit=true'  -H 'Content-type:application/json' -d '
[ {
  "ts" : "2023-05-23 12:27:58",
  "ip" : "81.88.175.159",
  "email" : "nathanjackson@cabrera-garcia.com",
  "username" : "brandonberry",
  "airport" : "LAX",
  "val1" : 746575638,
  "val2" : 696,
  "satz" : "Ago play paper office hospital have wonder already against which continue buy decision song view age international big employee determine."
} ]'
