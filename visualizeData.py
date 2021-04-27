import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def make_minority_pie_chart(data, output_folder, state):
    # make lists of all the data
    total_white = data[-2].split()[-1]
    total_minority = data[-1].split()[-1]
    labels = ["white", "minority"]
    populations = [total_white, total_minority]
    colors = ['lightskyblue', 'lightcoral']
    # plot
    fig = plt.figure()
    plt.pie(populations, colors=colors, autopct ='%1.1f%%', startangle=0)
    plt.axis('equal')
    plt.title(f'population of {state}')
    plt.legend(title="populations", labels=labels)
    plt.savefig(output_folder + state + '_pie_chart.png')
    # plt.show()


def make_poverty_graph(data, output_folder, state):
    # make lists of all the data
    counties = []
    minority_percentage = []
    poverty_percentage = []
    for row in data:
        counties.append(row[1].split('-')[1])
        minority_percentage.append(int(row[2] * 100))
        poverty_percentage.append(int(row[3] * 100))
    # plot
    x = np.arange(len(counties)) # label locations
    width = 0.35 # width of bars
    fig, ax = plt.subplots()
    # make bars
    a_array = np.array(minority_percentage)
    a = ax.bar(x - width/2, a_array, color = 'b', width=width, label='minority %')
    b_array = np.array(poverty_percentage)
    b = ax.bar(x + width/2, b_array, color = 'r', width=width, label='poverty %')
    # set labels
    ax.set_ylabel('percentage')
    ax.set_xlabel(f'{state} county code')
    ax.set_title(f'percent minority vs in poverty for counties in {state}')
    ax.set_xticks(x)
    ax.set_xticklabels(counties)
    ax.legend()
    ax.bar_label(a, padding=3, fontsize='6')
    ax.bar_label(b, padding=3, fontsize='6')
    # add only horizonatal dashed gridlines
    ax.yaxis.grid(ls='-.')
    plt.savefig(output_folder + state + '_poverty_graph.png')
    


def make_income_graph(data, output_folder, state):
    # make lists of all the data
    counties = []
    minority_percentage = []
    average_income = []
    for row in data:
        counties.append(row[1].split('-')[1])
        minority_percentage.append(int(row[2] * 100))
        # Real median household income in the United States in 2010 was $49,445 per census.gov
        average_income.append(int(row[4]/49445 * 100))
    # plot
    x = np.arange(len(counties)) # label locations
    width = 0.35 # width of bars
    fig, ax = plt.subplots()
    # make bars
    a_array = np.array(minority_percentage)
    a = ax.bar(x - width/2, a_array, color = 'b', width=width, label='minority %')
    b_array = np.array(average_income)
    b = ax.bar(x + width/2, b_array, color = 'r', width=width, label='% of real median houshold income')
    # set labels
    ax.set_ylabel('percentage')
    ax.set_xlabel(f'{state} county code')
    ax.set_title(f'percent minority vs average income for counties in {state}')
    # ax.set_ylim((0))
    ax.set_xticks(x)
    ax.set_xticklabels(counties)
    ax.legend()
    ax.bar_label(a, padding=3, fontsize='6')
    ax.bar_label(b, padding=3, fontsize='6')
    # add only horizonatal dashed gridlines
    ax.yaxis.grid(ls='-.')
    plt.savefig(output_folder + state + '_income_graph.png')
    plt.show()

    
def visualize(data, output_folder, state):
    # make a pie chart showing total state diversity
    make_minority_pie_chart(data, output_folder, state)
    # sort by poverty level for visual
    data = sorted(data[1:-2], key=lambda x: x[2])
    # make graphs correlationg minority % in county to poverty % and average income
    make_poverty_graph(data, output_folder, state)
    make_income_graph(data, output_folder, state)
