import matplotlib
import matplotlib.pyplot as plt

def make_minority_pie_chart(data, output_folder, state):
    print(data[-2])
    total_white = data[-2].split()[-1]
    total_minority = data[-1].split()[-1]
    labels = ["white", "minority"]
    populations = [total_white, total_minority]
    colors = ['lightskyblue', 'lightcoral']
    # plot
    fig = plt.figure()
    plt.pie(populations, labels=labels, colors=colors, autopct ='%1.1f%%', startangle=0)
    plt.axis('equal')
    plt.title(f'population of {state}')
    plt.savefig(output_folder + state + '_pie_chart.png')
    # plt.show()


def visualize(data, output_folder, state):
    make_minority_pie_chart(data, output_folder, state)