import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read the .csv file to get the data
data = pd.read_csv('./US_Accidents_Dec19.csv')

#Visulize the weather condition data through a horizontal bar plot
Weather = data.Weather_Condition.value_counts()
Weather_plt=Weather[['Clear','Mostly Cloudy','Overcast','Fair','Partly Cloudy','Scattered Clouds','Light Snow','Haze','Rain','Fog','Heavy Rain','Light Drizzle']]
plt.figure(figsize=(24, 18))
ax = Weather_plt.plot(kind="bar", rot=40, figsize=(40,24), fontsize=35, color='C0')
ax.set_xlabel("Weather", rotation = 0, fontsize=38)
ax.set_ylabel("Number of accidents", rotation = 0, fontsize=38)
ax.xaxis.set_label_coords(1.05,0.01)
ax.yaxis.set_label_coords(-0.05,1.02)
plt.title("Number of accidents by weather conditions", fontdict = {'fontsize': 80}, weight = 'bold', y=1.06)
plt.savefig('weather_US_horizontal.png', transparent=False)
plt.show()
