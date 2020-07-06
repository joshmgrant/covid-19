import csv


with open('covid_totals_by_country.csv') as file:
    reader = csv.DictReader(file)
    covid_cases = [row['Confirmed'] for row in reader]

with open('covid_totals_by_country.csv') as file:
    reader = csv.reader(file)
    covid_countries = [row[0] for row in reader]

with open('API_SI.POV.GINI_DS2_en_csv_v2_1068836.csv') as file:
    reader = csv.DictReader(file)
    gini_coef = [row['2019'] for row in reader]

with open('API_SI.POV.GINI_DS2_en_csv_v2_1068836.csv') as file:
    reader = csv.reader(file)
    gini_countries = [row[0] for row in reader]

covid_data = [*zip(covid_countries, covid_cases)]
gini_data = [*zip(gini_countries, gini_coef)]

output = []
# based on file lengths, Gini data has more entries
for c_country, case in covid_data:
    output.append([c_country, case])