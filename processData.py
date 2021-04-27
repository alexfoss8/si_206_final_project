import sqlite3

def process_data(cur, conn, state, filename):
    res = []
    res.append(['COUNTY_NAME', 'COUNTY_ID', 'MINORITY_%', 'POVERTY_%', 'AVG_INCOME'])
    op = """SELECT race.total_pop, race.white_pop, poverty.total_poverty, income.average_income, income.county_id, race.county
    FROM income
    JOIN poverty
      ON income.county_id = poverty.county_id AND income.state = ?
    JOIN race
      ON race.county_id = income.county_id AND race.state = ?"""
    cur.execute(op, (state,state,))
    data = cur.fetchall()
    total_pop = 0
    total_white = 0
    for row in data:
        total_pop += row[0]
        total_white += row[1]
        minority_percentage = (row[0] - row[1]) / row[0]
        poverty_percentage = row[2] / row[0]
        res.append([row[5], row[4], minority_percentage, poverty_percentage, row[3]])
    res.append(f'Total White Population: {total_white}\n')
    total_minority = (total_pop - total_white)
    res.append(f'Total Minority Population: {total_minority}\n')
    return res

