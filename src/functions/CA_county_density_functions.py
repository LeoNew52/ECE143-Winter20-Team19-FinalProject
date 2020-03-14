import os
import numpy as np
from src.functions.county_ratio import factor1_county
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import csv
from adjustText import adjust_text

def get_population_CA():
    '''
    purpose: to get a dictionary of California's population stats of each county
    :return: output, dict
    '''

    fin = open('src/files/population_county_CA.txt','r')


    population = {}

    for line in fin:
        line = line.replace('County','')
        x = line.split()
        dict_name = ''
        for word in x:
            word = word.replace(',','')
            if word.isdigit() == False:
                dict_name = dict_name + (str(word)+' ')
            else:
                pass
        population[dict_name.upper()[:-1]] = int(x[-1].replace(',',''))
    fin.close()
    return population

def get_n_vehicles_CA():
    '''
    purpose: to get a dictionary of California's number of registered vehicles stats of each county
    :return: output, dict
    '''
    fin = open('src/files/vehicles_number.txt','r')

    n_vehicles = {}

    for line in fin:
        line = line.replace(',','')
        x = line.split()
        dict_name = ''
        for word in x:
            if word.isdigit() == False:
                dict_name += (word+' ')
            else:
                pass
        n_vehicles[dict_name[:-1]] = int(x[-1])
    fin.close()
    return n_vehicles

def get_area_CA():
    '''
    purpose: to get a dictionary of California's area stats of each county
    :return: output, dict
    '''
    fin = open('src/files/county_area.txt','r')

    area = {}

    for line in fin:
        line = line.replace(',','')
        line = line.replace('sq mi','')
        line = line.replace('CA /','')
        x = line.split()
        x = x[1:-1]
        dict_name = ''
        for word in x[1:]:
            dict_name+= (word+' ')
        area[dict_name[:-1].upper()] = float(x[0])

    fin.close()
    return area

def get_n_accidents_CA():
    '''
    purpose: to get a dictionary of California's number of accidents stats of each county
    :return: output, dict
    '''
    n_accidents = factor1_county("CA_data.csv")
    n_accidents = dict(n_accidents)
    new_dict = dict([(value,key) for key, value in n_accidents.items()])
    for key,value in new_dict.items():
        new_dict[key] = value.upper()
    n_accidents = dict([(value,key) for key,value in new_dict.items()])

    return n_accidents

def data_process_CA(population,n_vehicles,area,n_accidents):
    '''
    purpose: to calcalate data/area for each county and categorize small samples into 'others'
    :param population: input, dict
    :param n_vehicles: input, dict
    :param area: input, dict
    :param n_accidents: input, dict
    :return: output, tuple
    '''


    assert isinstance(population,dict)
    assert isinstance(n_vehicles,dict)
    assert isinstance(area,dict)
    assert isinstance(n_accidents,dict)
    
    for key,value in n_accidents.items():
        n_accidents[key] = int(n_accidents[key])
    n_accidents_sum = sum(n_accidents.values())
    n_accidents['OTHERS'] = 0
    population['OTHERS'] = 0
    n_vehicles['OTHERS'] = 0
    area['OTHERS'] = 0
    keys_small = []

    for key,value in n_accidents.items():
        if key != 'OTHERS':
            if n_accidents[key]/n_accidents_sum <= 0.02:
                n_accidents['OTHERS'] += n_accidents[key]
                n_vehicles['OTHERS'] += n_vehicles[key]
                population['OTHERS'] += population[key]
                area['OTHERS'] += area[key]
                keys_small.append(key)

    for key in keys_small:
        del n_accidents[key]
        del n_vehicles[key]
        del population[key]
        del area[key]
    population_per = {}
    n_vehicles_per = {}
    n_accidents_per = {}

    for key, value in area.items():
        population_per[key] = population[key]/area[key]
        n_vehicles_per[key] = n_vehicles[key]/area[key]
        n_accidents_per[key] = n_accidents[key]/area[key] 
    
    population_per = {k:v for k,v in sorted(population_per.items(),key =lambda item:item[1])}

    return (population_per,n_vehicles_per,n_accidents_per)


    
