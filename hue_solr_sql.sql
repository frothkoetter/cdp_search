SELECT airport, count(1) as count_tweets
FROM airlinedata_tweets
GROUP BY airport
ORDER BY count_tweets desc
