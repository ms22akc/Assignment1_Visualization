import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    """
    # this function get data from xlsx
    # then store it in data variable and return the data
    """

    data_worldbank = pd.read_excel('P_Data_Extract_From_Doing_Business.xlsx')

    # return dataframe
    return data_worldbank


def define_variable(data_worldbank):
    # Define Global Variable
    global years
    global countries
    global dataset_uk
    global dataset_usa
    global dataset_pakistan
    global dataset_china
    global dataset_india

    # Set Graph Data
    dataset_uk = [data_worldbank[2016][0], data_worldbank[2017][0], data_worldbank[2018][0], data_worldbank[2019][0],
                  data_worldbank[2020][0]]
    dataset_usa = [data_worldbank[2016][1], data_worldbank[2017][1], data_worldbank[2018][1], data_worldbank[2019][1],
                   data_worldbank[2020][1]]
    dataset_pakistan = [data_worldbank[2016][2], data_worldbank[2017][2], data_worldbank[2018][2],
                        data_worldbank[2019][2], data_worldbank[2020][2]]
    dataset_china = [data_worldbank[2016][3], data_worldbank[2017][3], data_worldbank[2018][3], data_worldbank[2019][3],
                     data_worldbank[2020][3]]
    dataset_india = [data_worldbank[2016][4], data_worldbank[2017][4], data_worldbank[2018][4], data_worldbank[2019][4],
                     data_worldbank[2020][4]]

    # Define Years
    years = np.array(['2016', '2017', '2018', '2019', '2020'])

    # Define Countries
    countries = np.array(['United Kingdom', 'United States', 'Pakistan', 'China', 'India'])


def generate_avg(dataset_worldbank):
    # Calculating Average
    sum_data = 0

    # for loop, it will iterate and sum all values
    for t in dataset_worldbank:
        sum_data = sum_data + t

        # Avg variable is used to store average of data
    avg = sum_data / len(dataset_worldbank)
    return avg


def graph(diagram):
    """
    # in this function the visualization take place like
    # Line Chart,
    # Bar Chart,
    # Pie Chart
    """
    if diagram == "line":

        # Plotting data
        plt.plot(years, dataset_uk, label="United Kingdom")
        plt.plot(years, dataset_usa, label="United States")
        plt.plot(years, dataset_pakistan, label="Pakistan")
        plt.plot(years, dataset_china, label="China")
        plt.plot(years, dataset_india, label="India")

        # Add labels and title
        plt.title("Plot Multiple lines Data")
        plt.xlabel("Years")
        plt.ylabel("Dealing with construction permits")

        # Adding legend on upper right
        plt.legend(loc='upper right')

        # Generate Chart Image
        plt.savefig('line.png')

        # Show graph
        plt.show()

    elif diagram == "bar":

        # Calculate Average
        average = [generate_avg(dataset_uk), generate_avg(dataset_usa), generate_avg(dataset_pakistan),
                   generate_avg(dataset_china),
                   generate_avg(dataset_india)]

        # Calculate Average set Arrange
        x_pos = np.arange(len(countries))

        # Plotting bar graph
        plt.bar(x_pos, average, color=['#C94845', '#4958B5', '#49D845', '#777777'])

        # Add labels and title
        plt.title("Plot Bar Graph Data")
        plt.xlabel("Countries")
        plt.ylabel("Dealing with construction permits")

        # Adding Ticks
        plt.xticks(x_pos, countries)

        # Generate Chart Image
        plt.savefig('bar.png')

        # Show graph
        plt.show()

    elif diagram == "pie":

        # Calculate Average
        average = [generate_avg(dataset_uk), generate_avg(dataset_usa), generate_avg(dataset_pakistan),
                   generate_avg(dataset_china),
                   generate_avg(dataset_india)]

        # Plotting pie chart
        plt.pie(average, labels=countries)

        # Add labels and title
        plt.title("Plot Pie Graph Data")

        # Generate Chart Image
        plt.savefig('pie.png')

        # Show graph
        plt.show()


# Get Data
dataset_worldbank = get_data()

# set variable
define_variable(dataset_worldbank)

# Line Plot Graph
graph('line')

# Bar Chart Graph
graph('bar')

# Pie Chart Graph
graph('pie')
