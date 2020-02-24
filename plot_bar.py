import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import import_data as id

#read the .csv file to get the data
data = pd.read_csv('./US_Accidents_Dec19.csv')

#Process weather condition data and visulize through a bar plot
weather=data.Weather_Condition.unique()
count_by_weather=[]
for i in data.Weather_Condition.unique():
    count_by_weather.append(data[data['Weather_Condition']==i].count()['ID'])
plt.figure(figsize=(20,10))
sns.barplot(weathers, count_by_weather,"h")
plt.savefig('weather_US_vertical.png')


#Visulize the weather condition data through a horizontal bar plot
Weather = data.Weather_Condition.value_counts()
plt.figure(figsize=(16, 16))
sns.barplot(Weather.values, Weather.index)
plt.savefig('weather_US_horizontal.png')
