import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functions.weather_severity import create_weather_severity_df

def weather_severity_analysis_demo(data):
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

def main():
    data = pd.read_csv('./US_Accidents_Dec19.csv')
    weather_severity_analysis_demo(data)

if __name__ == '__main__':
    main()