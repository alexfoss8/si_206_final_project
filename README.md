# si_206_final_project
Objectivity of Alternative Data in the 2010 Census


## Motivation
The goal of this project was to examine the correlation between race, poverty, and income levels in all counties for a given state in the United States. Ultimately, the project was successful at calculating the percentage of minority individuals within a county and how this percentage correlated to the county’s poverty levels and median household income. 

## Install
1. Create virtual environment and activate:
```python3 -m venv env```
```source env/bin/activate```

2. Install requirements:
```pip3 install -r requirements.txt```

## Run
```python3 main.py```

>> “Enter state of Interest: “

<< User Input: User may enter any state for our program to run on (loop until receives correctly spelled state).


## API Refrence
Census Poverty and Income API: https://www.census.gov/programs-surveys/saipe/data/api.html 

Census Race API: https://www.census.gov/data/developers/data-sets/decennial-census.html


## Usage
Our program runs through our main.py file, which calls both of the files used for our data collection (getData.py) and calculations (processData.py), as well as an additional file for our visualizations (visualizeData.py). On user input, our program will collect all data necessary from the census APIs and run calculations for the state entered to output all visualizations for the given state.

## Data
API data: stored in census_data.db

Data Calculations: stored in output

Visualizations: stored in visualizations/ directory

The example usage of our program is included for this data, using the state Arizona.

## Documentation
main.py 

As per the usage section, our program is run by calling the main.py file. This file imports all other functions we employ from our getData.py, processData.py, and visualizeData.py. We take in user input that becomes the state we run our program with, read in a map of state names to census state codes from the state_codes.txt file and finally call the functions from the imported files in the order listed above.

getData.py 

This file holds two functions, get_income_and_poverty and get_race that both take in the sqlite cursor and connection, and each call an API and store the resulting data in our database with a void return.

get_income_and_poverty(cur, conn) calls https://api.census.gov/data/timeseries/poverty/saipe?get=SAEPOVALL_PT,SAEMHI_PT,NAME&for=county:*&in=state:*&time=2010
And creates two tables: income and poverty. Inside these tables we insert average income and total number of people in poverty for all counties in the United States, with each row being identified with a county id, county name, and state census code.

get_income_and_poverty(cur, conn) calls https://api.census.gov/data/2010/dec/sf1?get=P001001,PCT023003,NAME&for=county:*&in=state:*
And creates the table: race. Inside this table we insert total population and total white population for all counties in the United States, with each row being identified with a county id, county name, and state census code.

processData.py

This file holds the single function, process_data which takes in the sqlite cursor and connection, the state name identified by the user, and the filename for the calculations file. The function then calls a JOIN on all three tables (income, poverty, and race) where the county id is matching and the state matches the user input. Then, it uses the resulting data to calculate total white and minority populations as well as minority and poverty percentages for each county of the state in question. The resulting list is then returned to main, where it is written to the output file, output.

visualizeData.py

This file holds multiple functions. The function visualize is called by main and is given the calculation data returned from processData.py, the name of the visualization output folder, and the state given by the user. It then sorts the data by the poverty level in all counties to better fit a visualization and calls three functions to make our three visuals. Each of these functions are given the same input and then output the visualization made as a .png file and saved to the output folder, visualizations.

make_minority_pie_chart uses matplotlib to create a pie chart of the total populations of white people to minorities for the given state. It is titled population of {state} and uses a legend titled populations to display the categories.

make_povery_graph uses matplotlib and numpy to create a double bar graph that maps the minority percentage and poverty percentage for each county in the given state to show the correlation between the two. It is titled percent minority vs in poverty for counties in {state}. It uses a legend to display the categories, county numbering on the x-axis labeled arizona county code and lists percentages on the y-axis labeled percentage. The graph also uses horizontal dashed lines and numbering above each bar to make the graph easy to follow for the user.

make_income_graph uses matplotlib and numpy to create a double bar graph that maps the minority percentage and percent of average income when compared to the national average for each county in the given state to show the correlation between the two. It is titled percent minority vs average income for counties in {state}. It uses a legend to display the categories, county numbering on the x-axis labeled arizona county code and lists percentages on the y-axis labeled percentage. The graph also uses horizontal dashed lines and numbering above each bar to make the graph easy to follow for the user.
