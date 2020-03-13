import numpy as np
import pandas as pd

def create_weather_severity_df(data, weather_choosed):
    """
    Construct a pandas DataFrame with different accident severties under different weather condition
    args:
        data: pandas DataFrame contain all accident data with focus on California state
        Weather: pandas Series with total number of accidents under different weather conditions
        weather_choosed: Desired weather conditions
    return:
        weather_severity_percentage: pandas DataFrame with desired weather information
    """
    assert isinstance(data, pd.DataFrame)
    assert isinstance(weather_choosed, list)

    #Construct four lists stand for different severity
    #Index order follows order of weather index which is defined above (with alphabet order)
    severity_1_by_Weather = []
    severity_2_by_Weather = []
    severity_3_by_Weather = []
    severity_4_by_Weather = []
    for i in weather_choosed:
        severity_1_by_Weather.append(data[(data['Severity']==1)&(data['Weather_Condition']==i)].count()['ID'])
        severity_2_by_Weather.append(data[(data['Severity']==2)&(data['Weather_Condition']==i)].count()['ID'])
        severity_3_by_Weather.append(data[(data['Severity']==3)&(data['Weather_Condition']==i)].count()['ID'])
        severity_4_by_Weather.append(data[(data['Severity']==4)&(data['Weather_Condition']==i)].count()['ID'])

    #Count total accident numbers under different weather conditions
    Weather = data.Weather_Condition.value_counts()

    percentage_severity_1 = []
    percentage_severity_2 = []
    percentage_severity_3 = []
    percentage_severity_4 = []
    
    #Calculated the percentage of accident numbers regard to different weather conditions
    for i, val in enumerate(weather_choosed):
        percentage_severity_1.append((severity_1_by_Weather[i]/Weather[val])*100)
        percentage_severity_2.append((severity_2_by_Weather[i]/Weather[val])*100)
        percentage_severity_3.append((severity_3_by_Weather[i]/Weather[val])*100)
        percentage_severity_4.append((severity_4_by_Weather[i]/Weather[val])*100)

    #Construct a pandas DataFrame with four lists above
    weather_severity_percentage = pd.DataFrame(
        np.array([percentage_severity_1, percentage_severity_2, percentage_severity_3, percentage_severity_4]),
        columns = weather_choosed)
    
    #Use weather condition as datafrmae index
    weather_severity_percentage = weather_severity_percentage.T
    
    #Replace some weather name with a shorter one
    weather_severity_percentage = weather_severity_percentage.rename(
    {'Blowing Dust / Windy': 'Blowing Dust', 'Widespread Dust / Windy': 'Widespread Dust'}, axis='index')

    return weather_severity_percentage