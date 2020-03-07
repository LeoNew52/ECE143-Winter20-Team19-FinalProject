import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_bar_charts(data, title, plot_kind="bar", normal=False, rotation=0, stacked = False, figsize=None, 
    plot_fontsize=None, cmap = None, xlabel_name=None, xlabel_rotation=0, xlabel_fontsize=None, 
    xlabel_weight=None, ylabel_name=None, ylabel_rotation=0, ylabel_fontsize=None, ylabel_weight=None, 
    xlabel_coordinate=None, ylabel_coordinate=None, title_fontsize=None, title_weight=None, title_y=None, 
    ifledgend=False, ledgend_name=None, ledgend_fontsize=None, ledgend_location=None, bbox_to_anchor=None, 
    frameon=False):
    """
    Plot a value-count chart for different columns in the dataframe
    Args:
        data: Input dataframe or series
        title: Title for printed chart
        plot_kind: "bar" stands for vertical bar charts and "barh" stands for horizontal bar charts
        normal: If we want to normalize the counted value as percentage of total number
        rotation: Rotation for labels, default 0
        stacked: If there is more than 1 column to be plot in the dataframe, stack those columns or not
        figsize: A tuple for desired plotted chart
        plot_fontsize: Font size for labels
        cmap: Desired color map for plot
        xlabel_name: Label for x axis on plotted chart
        xlabel_rotation: Rotation for name of x axis, default 0
        xlabel_fontsize: Font size for name of x axis
        xlabel_weight: Different wight on name of x axis
        ylabel_name: Label for y axis on plotted chart
        ylabel_rotation: Rotation for name of y axis, default 0
        ylabel_fontsize: Font size for name of y axis
        ylabel_weight: Different wight on name of y axis
        xlabel_coordinate: Coordinate of x label
        ylabel_coordinate: Coordinate of y label
        title_fontsize: Font size for title
        title_weight: Different weight on title
        tilte_y: Adjust height of title
        ifledgend: If we need to mark ledgend or not
        ledgend_name: A tuple contains desired showed ledgend name
        ledgend_fontsize: Font size for ledgend
        ledgend_location: Where to put the ledgend box
        bbox_to_anchor: Coordinate of bound box for ledgend
        frameon: Show the bounding box frame or not
    Return:
        None: We plot a chart when the function is called, nothing to be return
    """
    assert isinstance(data, pd.DataFrame) or isinstance(data, pd.Series)
    assert isinstance(title, str)
    assert isinstance(plot_kind, str)
    assert isinstance(normal, bool)
    assert isinstance(rotation, int)
    assert isinstance(stacked, bool)
    if figsize: assert isinstance(figsize, tuple)
    if plot_fontsize: assert isinstance(plot_fontsize, int)
    if cmap: assert isinstance(cmap, str)
    if xlabel_name: assert isinstance(xlabel_name, str)
    assert isinstance(xlabel_rotation, int)
    if xlabel_fontsize: assert isinstance(xlabel_fontsize, int)
    if xlabel_weight: assert isinstance(xlabel_weight, str)
    if ylabel_name: assert isinstance(ylabel_name, str)
    assert isinstance(ylabel_rotation, int)
    if ylabel_fontsize: assert isinstance(ylabel_fontsize, int)
    if ylabel_weight: assert isinstance(ylabel_weight, str)
    if xlabel_coordinate: assert isinstance(xlabel_coordinate, tuple)
    if ylabel_coordinate: assert isinstance(ylabel_coordinate, tuple)
    if title_fontsize: assert isinstance(title_fontsize, int)
    if title_weight: assert isinstance(title_weight, str)
    if tilte_y: assert isinstance(tilte_y, int)
    assert isinstance(ifledgend, bool)
    if ledgend_name: assert isinstance(ledgend_name, tuple)
    if ledgend_fontsize: assert isinstance(ledgend_fontsize, int)
    if ledgend_location: assert isinstance(ledgend_location, str)
    if bbox_to_anchor: assert isinstance(bbox_to_anchor, tuple)
    assert isinstance(frameon, bool)
    

    #Save and Plot the chart 
    ax = data.plot(kind=plot_kind, stacked = stacked, rot=rotation, figsize=figsize, fontsize = plot_fontsize, cmap = cmap)
    if ifledgend:
        plt.legend(('least', 'less', 'moderate', 'severe'), fontsize = 80, loc='upper right', bbox_to_anchor=(1.12, 1.08), frameon = True)
    ax.set_xlabel(xlabel_name, rotation = xlabel_rotation, fontsize=xlabel_fontsize, weight = xlabel_weight)
    ax.set_ylabel(ylabel_name, rotation = ylabel_rotation, fontsize=ylabel_fontsize, weight = ylabel_weight)
    ax.xaxis.set_label_coords(xlabel_coordinate[0], xlabel_coordinate[1])
    ax.yaxis.set_label_coords(ylabel_coordinate[0], ylabel_coordinate[1])
    plt.title(title, fontdict = {'fontsize': title_fontsize}, weight = title_weight, y=title_y)
    plt.savefig(title, transparent=True)
    plt.show()



def main():
    """
    This is the main file for running all codes
    """

    # Load dataset
    file = "./US_Accidents_Dec19.csv"
    df = pd.read_csv(file)

    # Focus on California state
    data = df[df["State"] == "CA"]

    # Count total accident numbers under different severity
    # Replace the index of "Severity" column from [1, 2, 3, 4] to ['least', 'less', 'moderate', 'severe']
    # for a better understanding in plotted chart
    data["Severity"] = data["Severity"].replace([1, 2, 3, 4], ['least', 'less', 'moderate', 'severe'])
    severity = data["Severity"].value_counts()/1000
    
    # Value counts under different severities
    plot_bar_charts(severity, "Statistics of Severity", plot_kind="bar", figsize=(50,20), plot_fontsize=70, 
                    xlabel_name="Severity", xlabel_rotation=0, xlabel_fontsize=50, xlabel_weight='bold', 
                    ylabel_name="Accident Numbers (k)", ylabel_rotation=0, ylabel_fontsize=50, ylabel_weight='bold', 
                    xlabel_coordinate=(1.05,0.01), ylabel_coordinate=(-0.05,1.02), title_fontsize=80, title_weight='bold', title_y=1.06)
    
    # Reverse the index of "Severity" column from ['least', 'less', 'moderate', 'severe'] to [1, 2, 3, 4]
    data["Severity"] = data["Severity"].replace(['least', 'less', 'moderate', 'severe'], [1, 2, 3, 4])

    # Select desired weather conditions
    weather_choosed = ['Blowing Dust', 'Blowing Dust / Windy', 'Blowing Sand', 'Clear', 'Fair', 'Fog / Windy', 
                        'Hail', 'Heavy Drizzle', 'Light Freezing Rain', 'Light Rain', 'Light Snow / Windy', 
                        'Light Snow Showers', 'Mostly Cloudy', 'Thunderstorm', 'Widespread Dust / Windy']

    # Construct four lists stand for different severity
    # Index order follows order of weather index which is defined above (with alphabet order)
    severity_1_by_Weather = []
    severity_2_by_Weather = []
    severity_3_by_Weather = []
    severity_4_by_Weather = []
    for i in weather_choosed:
        severity_1_by_Weather.append(data[(data['Severity']==1)&(data['Weather_Condition']==i)].count()['ID'])
        severity_2_by_Weather.append(data[(data['Severity']==2)&(data['Weather_Condition']==i)].count()['ID'])
        severity_3_by_Weather.append(data[(data['Severity']==3)&(data['Weather_Condition']==i)].count()['ID'])
        severity_4_by_Weather.append(data[(data['Severity']==4)&(data['Weather_Condition']==i)].count()['ID'])

    # Count total accident numbers under different weather conditions
    Weather = data.Weather_Condition.value_counts()

    # Calculated the percentage of accident numbers regard to different weather conditions
    percentage_severity_1 = []
    percentage_severity_2 = []
    percentage_severity_3 = []
    percentage_severity_4 = []

    for i, val in enumerate(weather_choosed):
        percentage_severity_1.append((severity_1_by_Weather[i]/Weather[val])*100)
        percentage_severity_2.append((severity_2_by_Weather[i]/Weather[val])*100)
        percentage_severity_3.append((severity_3_by_Weather[i]/Weather[val])*100)
        percentage_severity_4.append((severity_4_by_Weather[i]/Weather[val])*100)

    # Construct a pandas DataFrame with four lists above
    weather_severity_percentage = pd.DataFrame(
        np.array([percentage_severity_1, percentage_severity_2, percentage_severity_3, percentage_severity_4]),
        columns = weather_choosed)

    # Use weather condition as datafrmae index
    weather_severity_percentage = weather_severity_percentage.T

    # Replace some weather name with a shorter one
    weather_severity_percentage = weather_severity_percentage.rename(
    {'Blowing Dust / Windy': 'Blowing Dust', 'Widespread Dust / Windy': 'Widespread Dust'}, axis='index')

    # Plot the stacked bar chart with percentage dataframe which are calculated above
    plot_bar_charts(weather_severity_percentage, "Severity percentage to Weather condition", plot_kind="barh", 
                    stacked = True, figsize=(80,50), plot_fontsize=70, cmap = "coolwarm", 
                    xlabel_name="Severity percentage", xlabel_rotation=0, xlabel_fontsize=80, xlabel_weight='bold', 
                    ylabel_name="Weather Condition", ylabel_rotation=0, ylabel_fontsize=80, ylabel_weight='bold', 
                    xlabel_coordinate=(1.02, -0.05), ylabel_coordinate=(-0.05, 1.02), title_fontsize=150, 
                    title_weight='bold', title_y=1.06, ifledgend=True, ledgend_name=('least', 'less', 'moderate', 'severe'), 
                    ledgend_fontsize=80, ledgend_location="upper right", bbox_to_anchor=(1.12, 1.08), frameon=True)



if __name__ == '__main__':
    main()
