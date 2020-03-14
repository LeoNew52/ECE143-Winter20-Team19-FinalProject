import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.functions.which_day import which_day

def time_distribution_analysis_demo(data):
    ''' Run the analysis for gneral analysis of nationwide dataset regarding diffrent days of a week and differenet hours per day
        input: data: input pandas DataFrame
    '''
    assert isinstance(data, pd.DataFrame)

    # use the which_day function to find the corresponding weekday
    nth_day=[]
    date_time=[dt for dt in data['Start_Time']]
    for i in range(len(date_time)):
        nth_day.append(which_day(date_time[i]))

    # add four new columns 'year', 'month', 'hour', 'weekday'
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year
    data['month'] = pd.DatetimeIndex(data['Start_Time']).month
    data['hour'] = pd.DatetimeIndex(data['Start_Time']).hour
    data['weekday']=nth_day

    #split data into weekdays and weekends
    wday_filt = (data['weekday'].isin([0, 1, 2, 3, 4]))
    weekend_filt = (data['weekday'].isin([5, 6]))
    data_workday = (data.loc[wday_filt])[['hour']]
    data_weekend = (data.loc[weekend_filt])[['hour']]

    #plot out accidant data with respect to the weekday distribution
    dt_weekday=data.groupby(['weekday'], as_index=False).count().iloc[:,:2]
    ax=dt_weekday.plot(kind='bar',rot=0,width=1.0,figsize=(10, 6),fontsize=16,legend=None)
    xtick_labels=['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri', 'Sat.', 'Sun.']
    ax.set_xticks(list(dt_weekday.index))
    ax.set_xticklabels(xtick_labels)
    ax.set_xlabel('Weekdays',rotation=0, fontsize=16)
    ax.set_ylabel('Number of Accidents',rotation=0, fontsize=16)
    ax.set_title('    Number of accidents by days of week', fontsize=20)
    ax.xaxis.set_label_coords(1.08,0.00)
    ax.yaxis.set_label_coords(0.02,1.01)
    plt.savefig('#Accidents_days_of_week.png',transparent=False)
    plt.show()

    #plot out distributon divided into weekdays and weekends
    fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(6, 12),sharex=True)
    ax0,ax1=axes.flatten()
    kwargs = dict(bins=24,density=False,histtype='stepfilled',linewidth=3)
    ax0.hist(list(data_workday['hour']),**kwargs,label='Only Work days')
    ax0.set_ylabel('Number of accidents',fontsize=16,rotation=0)
    ax0.yaxis.set_label_coords(0.09,1.02)
    ax1.hist(list(data_weekend['hour']),**kwargs,label='Only weekend')
    ax1.set_ylabel('Number of accidents',fontsize=16,rotation=0)
    ax1.set_xlabel('Hour',fontsize=16)
    ax1.yaxis.set_label_coords(0.09,1.02)
    ax0.legend(); ax1.legend()
    plt.savefig('hourly_distribution_US.png',transparent=False)
    plt.show()

def main():
    #read the .csv file to get the data
    data = pd.read_csv('./US_Accidents_Dec19.csv')
    time_distribution_analysis_demo(data)

if __name__ == '__main__':
    main()
