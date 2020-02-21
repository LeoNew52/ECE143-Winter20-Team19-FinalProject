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

import addfips #https://github.com/fitnr/addfips

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
    
from urllib.request import urlopen
import json
import numpy as np
import pandas as pd
import plotly.figure_factory as ff

def plot_county_accident_rates():
    #Code template from https://plot.ly/python/choropleth-maps/
    
    #Import county geoJSON information
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
        
    #Format as dataframe with pandas
    fips=get_county_fips_code('US_Accidents_Dec19.csv', 17, 16)
    fipss=count_data(fips)
    fips_code=list(fipss.keys())
    fips_count=list(fipss.values())
    assert len(fips_code)==len(fips_count)
    for i,code in enumerate(fips_code):
        if not isinstance(code,str):
            fips_code.pop(i)
            fips_count.pop(i)
    
    plot_dict={'fips':list(fipss.keys()),'count':list(fipss.values())}
    df=pd.DataFrame(plot_dict)
    #Plot with plotly
    import plotly.express as px

    fig = px.choropleth(df, geojson=counties, locations='fips', color=np.log10(df["count"]),
                           color_continuous_scale="Viridis",
                           range_color=(0, 6),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

#fips=get_county_fips_code('US_Accidents_Dec19.csv', 17, 16)
