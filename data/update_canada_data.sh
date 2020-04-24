head -1 time-series-19-covid-combined.csv > canada-time-series-combined.csv
head -1 time-series-19-covid-combined.csv > ontario-time-series-combined.csv
head -1 time-series-19-covid-combined.csv > bc-time-series-combined.csv
head -1 time-series-19-covid-combined.csv > alberta-time-series-combined.csv

grep 'Canada' time-series-19-covid-combined.csv >> canada-time-series-combined.csv
grep 'Ontario' time-series-19-covid-combined.csv >> ontario-time-series-combined.csv
grep 'British Columbia' time-series-19-covid-combined.csv >> bc-time-series-combined.csv
grep 'Alberta' time-series-19-covid-combined.csv >> alberta-time-series-combined.csv