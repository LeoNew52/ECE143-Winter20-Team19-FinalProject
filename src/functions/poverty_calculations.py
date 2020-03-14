from src.functions.import_data import *
from urllib.request import urlopen
import json
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import addfips #https://github.com/fitnr/addfips
import csv


def count_data(inlist):
    '''
    A counter function that counts the occurance of each element in the list and returns in into a dictionary
    with keys representing elements and values representing occurances.
    :inlist: list to be counted
    '''
    assert isinstance(inlist,list)
    outdict={}
    for element in list(set(inlist)): 
        outdict[element]=0 #initialize
    for element in inlist:
        outdict[element]+=1 #Count
    return outdict

def get_day_of_week():
    '''
    A function specific to our dataset that reterns the number of accidents in each day of the week
    '''
    header,data= import_data('US_Accidents_Dec19.csv',read='col',samples=None,col_num=4) #Import start_time column
    counter=[0]*7 #weekday counter, 0:=Monday,6:=Sunday
    for day in data:
        counter[day.weekday()]+=1
    return counter
    #counter=[507255, 543725, 537474, 526138, 537749, 170349, 151645]
    
def sort_by_state():
    '''
    A function specific to our dataset that reterns the number of accidents in each state
    '''
    header,states= import_data('US_Accidents_Dec19.csv',read='col',samples=None,col_num=17)
    return count_data(states)

def sort_by_county():
    '''
    A function specific to our dataset that reterns the number of accidents in each county
    '''
    header,counties= import_data('US_Accidents_Dec19.csv',read='col',samples=None,col_num=16)
    return count_data(counties)

def get_county_fips_code(fname, state_col,county_col):
    '''
    A function that uses the addfips library to assign fips codes accordingly to our data.
    FIPS codes help with geographic plots for our dataset, as they are unified numbers for
    states and counties.
    :fname: string. Name of input file to get FIPS codes from
    :state_col: column number where state name is located
    :county_col: column number where county name is stored.
    '''
    assert isinstance(fname,str) and isinstance(state_col,int) and isinstance(county_col,int)
    assert state_col>=0 and county_col>=0
    af=addfips.AddFIPS()
    header,state= import_data(fname,read='col',samples=None,col_num=state_col)
    header,county= import_data(fname,read='col',samples=None,col_num=county_col)
    assert len(state)==len(county)
    fips=[0]*len(state)
    for i in range(len(state)):
        fips[i]=af.get_county_fips(county[i], state[i])
    return fips

def get_population_per_county():
    '''
    Returns a dictionsary with fips codes as keys and population estimate in 2018 as its value
    Make sure to download the PEP_2018 file form GitHub
    '''
    out_dict={}
    f=open('PEP_2018_PEPANNRES_with_ann.csv','r',newline='',encoding='latin-1')
    reader=csv.reader(f)
    header1=next(reader)
    header2=next(reader)
    for row in reader:
            out_dict[row[1]]=int(row[13])
    return out_dict, header1, header2
    

def plot_county_accident_rates(fname):
    '''
    Creates scatterplot of addcident per capita vs poverty rate
    :fname: string containing name of dataframe
    '''
    #Code template from https://plot.ly/python/choropleth-maps/ for the choropleth map portion only
    
    #Import county geoJSON information
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
        
    #Obtain accidents per county
    fips=get_county_fips_code(fname, 17, 16)
    fipss=count_data(fips)
    fips_code=list(fipss.keys())
    fips_count=list(fipss.values())
    assert len(fips_code)==len(fips_count)

    #Remove None types
    for i,code in enumerate(fips_code):
        if not isinstance(code,str):
            fips_code.pop(i)
            fips_count.pop(i)
            
    #Get poverty rates per county
    #make sure to install xlrd 'pip install xlrd'
    df_pov=pd.read_excel('est18all.xlsx',converters={'State FIPS Code':str,'County FIPS Code':str})
    df_pov['FIPS Code']=df_pov.apply(lambda df_pov: df_pov['State FIPS Code']+df_pov['County FIPS Code'], axis=1)
    
    #Get population data and obtain accidents per capita
    pop,h1,h2=get_population_per_county()
    accident_per_capita={}
    for x in fips_code:
        if x in pop.keys():
            accident_per_capita[x]=(fipss[x]/pop[x])
    plot_dict={'FIPS Code':list(accident_per_capita.keys()),'Accident Per Capita':list(accident_per_capita.values())}
    df_apc=pd.DataFrame(plot_dict)

    #Plot accidents per capita with plotly
    fig1 = px.choropleth(df_apc, geojson=counties, locations='FIPS Code', color=np.log10(df_apc['Accident Per Capita']),
                        color_continuous_scale="Viridis",
                        scope="usa",
                        labels={'apc':'Accidents Per Capita'},
                        title='Accidents Per Capita (Logarithmic)')
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig1.show()
    
    #Combine APC and poverty into single df and plot scatter
    df=pd.merge(df_pov,df_apc)
    df=df.drop([index for index, row in df.iterrows() if row['Accident Per Capita']>0.1]) #drop 3 outliers
    plt.scatter(df['Poverty Percent, All Ages'],df['Accident Per Capita'],alpha=0.2)
    plt.xlabel('Poverty Percentage')
    plt.ylabel('Accident Per Capita')
    plt.title('Distribution of Accidents per County')

    #Find correlation
    df['Poverty Percent, All Ages']=df['Poverty Percent, All Ages'].astype('float')
    df.corr()
    
    
    return df
    #fips=get_county_fips_code('US_Accidents_Dec19.csv', 17, 16)
