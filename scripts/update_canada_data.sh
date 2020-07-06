head -1 ./data/time-series-19-covid-combined.csv > data/canada-time-series-combined.csv
head -1 ./data/time-series-19-covid-combined.csv > data/ontario-time-series-combined.csv
head -1 ./data/time-series-19-covid-combined.csv > data/bc-time-series-combined.csv
head -1 ./data/time-series-19-covid-combined.csv > data/alberta-time-series-combined.csv

grep 'Canada' ./data/time-series-19-covid-combined.csv >> data/canada-time-series-combined.csv
grep 'Ontario' ./data/time-series-19-covid-combined.csv >> data/ontario-time-series-combined.csv
grep 'British Columbia' ./data/time-series-19-covid-combined.csv >> data/bc-time-series-combined.csv
grep 'Alberta' ./data/time-series-19-covid-combined.csv >> data/alberta-time-series-combined.csv
