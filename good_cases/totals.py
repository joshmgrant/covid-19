import csv


with open('mongolia.csv') as file:
    reader = csv.DictReader(file)
    mongolia_cases = [row['Confirmed'] for row in reader]
    mongolia_deaths = [row['Deaths'] for row in reader]

with open('trinidad_tobago.csv') as file:
    reader = csv.DictReader(file)
    trini_cases = [row['Confirmed'] for row in reader]
    trini_deaths = [row['Deaths'] for row in reader]

with open('vietnam.csv') as file:
    reader = csv.DictReader(file)
    vietnam_cases = [row['Confirmed'] for row in reader]
    vietnam_deaths = [row['Deaths'] for row in reader]

total_cases = int(mongolia_cases[-1]) + int(trini_cases[-1]) + int(vietnam_cases[-1])
try:
    mg_total_deaths = int(mongolia_deaths[-1])
except IndexError:
    mg_total_deaths = 0
try:
    tr_total_deaths = int(trini_deaths[-1])
except IndexError:
    tr_total_deaths = 0
try:
    vt_total_deaths = int(vietnam_deaths[-1])
except IndexError:
    vt_total_deaths = 0

                
total_deaths = mg_total_deaths + tr_total_deaths + vt_total_deaths

print("Mongolia, Trinidad and Tobago, and Vietnam")
print("Total cases: {}".format(total_cases))
print("Total deaths: {}".format(total_deaths))
