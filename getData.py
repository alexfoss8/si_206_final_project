import requests


def get_income_and_poverty(cur, conn):
    income_and_poverty_API = 'https://api.census.gov/data/timeseries/poverty/saipe?get=SAEPOVALL_PT,SAEMHI_PT,NAME&for=county:*&in=state:*&time=2010'
    # set up tables
    cur.execute("CREATE TABLE IF NOT EXISTS income (average_income INTEGER, county_id TEXT PRIMARY KEY, county TEXT, state Integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS poverty (total_poverty INTEGER, county_id TEXT PRIMARY KEY, county TEXT, state Integer)")
    length = 0
    start_range = 0
    end_range = 25
    id_set = set()
    while start_range < 225:
        response = requests.get(income_and_poverty_API)
        response = response.json()
        data = response[1:]
        length = len(data)
        for i in range(start_range, end_range):
            # get data from income and poverty api
            county_id = f'{data[i][4]}-{data[i][5]}'
            if county_id in id_set: continue
            id_set.add(county_id)
            average = data[i][1]
            total = data[i][0]
            county = data[i][2]
            state = data[i][4]
            if average == None or total == None or county == None or state == None: continue
            # labels = ["poverty_total", "income_average", "county_name", "year", "state", "county_id"]
            cur.execute("INSERT or IGNORE INTO income (average_income, county_id, county, state) VALUES (?,?,?,?)",
                        (int(average), county_id, county, int(state))), (county_id)
            cur.execute("INSERT or IGNORE INTO poverty (total_poverty, county_id, county, state) VALUES (?,?,?,?)",
                        (int(total), county_id, county, int(state)))
        # increment range
        start_range += 25
        end_range += 25
        if end_range > 200:
            end_range = length
    conn.commit()


def get_race(cur, conn):
    # race api map
    # race_map = {
    #     'white': 'PCT023003',
    #     'black': 'PCT023004',
    #     'native_american': 'PCT023005',
    #     'asain': 'PCT023006',
    #     'pacific_islander': 'PCT023014'
    # }
    #get data from race api
    race_API = f'https://api.census.gov/data/2010/dec/sf1?get=P001001,PCT023003,NAME&for=county:*&in=state:*'
    cur.execute("CREATE TABLE IF NOT EXISTS race (total_pop INTEGER, white_pop INTEGER, county_id TEXT PRIMARY KEY, county TEXT, state Integer)")
    length = 0
    start_range = 0
    end_range = 25
    id_set = set()
    while start_range < 225:
        response = requests.get(race_API)
        response = response.json()
        data = response[1:]
        length = len(data)
        for i in range(start_range, end_range):
            # get data from income and poverty api
            county_id = f'{data[i][3]}-{data[i][4]}'
            if county_id in id_set: continue
            id_set.add(county_id)
            total_pop = data[i][0]
            white_pop = data[i][1]
            county = data[i][2]
            state = data[i][3]
            # labels = ["total_pop", "race_pop", "county_name", "state", "county_id"]
            cur.execute("INSERT or IGNORE INTO race (total_pop, white_pop, county_id, county, state) VALUES (?,?,?,?,?)",
                        (int(total_pop), int(white_pop), county_id, county, int(state)))
        start_range += 25
        end_range += 25
        if end_range > 200:
            end_range = length
        
    conn.commit()






