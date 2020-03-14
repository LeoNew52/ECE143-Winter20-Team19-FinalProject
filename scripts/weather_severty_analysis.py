import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.weather_severity import create_weather_severity_df

data = pd.read_csv('./US_Accidents_Dec19.csv')
data = data[data["State"] == "CA"]

#Count total accident numbers under different severity
#Replace the index of "Severity" column from [1, 2, 3, 4] to ['least', 'less', 'moderate', 'severe']
#for a better understanding in plotted chart
data["Severity"] = data["Severity"].replace([1, 2, 3, 4], ['least', 'less', 'moderate', 'severe'])
severity = data["Severity"].value_counts()/1000

#Plot a bar chart of value counts under different severities
ax = severity.plot(kind="bar", rot=0, figsize=(50,20), fontsize = 70)
ax.set_xlabel("Severity", rotation = 0, fontsize=50, weight = 'bold')
ax.set_ylabel("Accident Numbers (k)", rotation = 0, fontsize=50, weight = 'bold')
ax.xaxis.set_label_coords(1.05,0.01)
ax.yaxis.set_label_coords(-0.05,1.02)
plt.title("Statistics of Severity", fontdict = {'fontsize': 80}, weight = 'bold', y=1.06)
plt.savefig("Statistics of Severity", transparent=True)
plt.show()

#Reverse the index of "Severity" column from ['least', 'less', 'moderate', 'severe'] to [1, 2, 3, 4]
data["Severity"] = data["Severity"].replace(['least', 'less', 'moderate', 'severe'], [1, 2, 3, 4])

#Choose desired weather condition
weather_choosed = ['Blowing Dust', 'Blowing Dust / Windy', 'Blowing Sand', 'Clear', 'Fair', 'Fog / Windy', 
                        'Hail', 'Heavy Drizzle', 'Light Freezing Rain', 'Light Rain', 'Light Snow / Windy', 
                        'Light Snow Showers', 'Mostly Cloudy', 'Thunderstorm', 'Widespread Dust / Windy']

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
weather_severity_percentage = create_weather_severity_df(data, weather_choosed)

#Plot the stacked bar chart with percentage dataframe which are calculated above
ax = weather_severity_percentage.plot(kind="barh", stacked=True, rot=0, figsize=(80,50), fontsize=70, cmap="coolwarm")
plt.legend(('least', 'less', 'moderate', 'severe'), fontsize = 80, loc='upper right', bbox_to_anchor=(1.12, 1.08), frameon = True)
ax.set_xlabel("Severity percentage", rotation = 0, fontsize=80, weight='bold')
ax.set_ylabel("Weather Condition", rotation = 0, fontsize=80, weight='bold')
ax.xaxis.set_label_coords(1.02, -0.05)
ax.yaxis.set_label_coords(-0.05, 1.02)
plt.title("Severity percentage to Weather condition", fontdict = {'fontsize': 150}, weight='bold', y=1.06)
plt.savefig("Severity percentage to Weather condition", transparent=True)
plt.show()