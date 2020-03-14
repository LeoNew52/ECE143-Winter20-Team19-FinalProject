import numpy as np
from functions.county_ratio import factor1_county
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
from adjustText import adjust_text
from functions.CA_county_density_functions import get_population_CA,get_n_vehicles_CA,get_area_CA,get_n_accidents_CA,data_process_CA
from functions.get_cali_data import get_cali_data


def CA_county_density_demo(filename):
    '''
    purpose: To obtain California's accident, population and vehicle number density plot.
    :param filename:input, str
    '''

    assert isinstance(filename,str)
    
    #Separate CA data from US data
    get_cali_data(filename)

    #get population of each county
    population = get_population_CA()

    #get number of vehicles of each county
    n_vehicles = get_n_vehicles_CA()

    #get area of each county
    area = get_area_CA()

    #get number of accidents in each county
    n_accidents = get_n_accidents_CA()

    #categorize small samples to 'others', get population, number of vehicles and number of accidents per sq mi
    population_per,n_vehicles_per,n_accidents_per = data_process_CA(population,n_vehicles,area,n_accidents)

    #plot
    labels = []
    population_plot = []
    n_vehicles_plot =[]
    n_accidents_plot =[]

    for key,value in population_per.items():
        labels.append(key)
        population_plot.append(value)
        n_vehicles_plot.append(n_vehicles_per[key])
        n_accidents_plot.append(n_accidents_per[key])


    
    #get scatter plot
    fig1 = plt.figure(figsize = (10,5))
    texts =[]
    for i,county in enumerate(labels):
        x = population_plot[i]
        y = n_accidents_plot[i]
        plt.scatter(x,y,marker = 'o',color = 'blue')
        texts.append(plt.text(x+0.3,y+0.3,county,fontsize = 10))


    adjust_text(texts)
    coeff1 = np.polyfit(population_plot,n_accidents_plot,1)
    poly1d_fn = np.poly1d(coeff1)
    plt.plot(population_plot,poly1d_fn(population_plot),'-',color = 'red')
    plt.tick_params(axis="both", labelsize=14)
    ax = plt.axes()
    ax.yaxis.set_label_coords(-0.05,1.02)
    plt.title('correlation between population and number of accidents per square mile',fontsize = 12)
    plt.xlabel('population per sq mi',fontsize = 12)
    plt.ylabel('number of accidents\n per sq mi',fontsize = 12,rotation = 0)

    fig1.savefig('pop.png', transparent=True)
    plt.show()

    #get scatter plot
    fig2 = plt.figure(figsize = (10,5))
    texts =[]
    for i,county in enumerate(labels):
        x = n_vehicles_plot[i]
        y = n_accidents_plot[i]
        plt.scatter(x,y,marker = 'o',color = 'blue')
        texts.append(plt.text(x+0.3,y+0.3,county,fontsize = 10))

    adjust_text(texts)
    coeff2 = np.polyfit(n_vehicles_plot,n_accidents_plot,1)
    poly1d_fn2 = np.poly1d(coeff2)
    plt.plot(n_vehicles_plot,poly1d_fn2(n_vehicles_plot),'-',color = 'red')

    plt.tick_params(axis="both", labelsize=14)
    ax = plt.axes()
    ax.yaxis.set_label_coords(-0.05,1.02)
    plt.title('correlation between number of vehicles and number of accidents per square mile',fontsize = 12)
    plt.xlabel('number of vehicles per sq mi',fontsize = 12)
    plt.ylabel('number of accidents\n per sq mi',fontsize = 12,rotation = 0)
    fig2.savefig('vehicle.png', transparent=True)
    plt.show()

def main():
    CA_county_density_demo('./US_Accidents_Dec19.csv')

if __name__ == '__main__':
    main()
