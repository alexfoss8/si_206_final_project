import os
import sqlite3

from getData import get_income_and_poverty, get_race
from processData import process_data
from visualizeData import visualize

# get state of intrest
state = input("Enter state of intrest: ").lower()

# read in state codes
state_codes = {}
with open('state_codes.txt') as f:
    for line in f.readlines():
        line = line.split('|')
        state_codes[line[2].lower()] = line[0]

# make sure valid state
while state not in state_codes:
    state = input('Enter state name again. Please check spelling: ')

# set up db
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+'census_data.db')
cur = conn.cursor()

# call income and poverty api
print('Calling income and poverty API . . .')
get_income_and_poverty(cur, conn)

# call race api
print('Calling race API . . .')
get_race(cur, conn)

# process data and send to output file
output_file = path + '/output'
data = process_data(cur, conn, state_codes[state], output_file)
with open(output_file, 'w') as out:
    out.writelines('|'.join(str(j) for j in i) + '\n' for i in data[:-2])
    out.write(data[-2])
    out.write(data[-1])
print(f'Processed data in {output_file}')

# create visualizetions
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')
output_folder = path + '/visualizations/'
visualize(data, output_folder, state)
print(f'Data Visuals in {output_folder}')
