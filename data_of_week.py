import pandas as pd
import matplotlib.pyplot as plt

def which_day(date_time):
    '''
    To find out which weekday according to given timestamp with the format 'yyyy-mm-dd hh:mm:ss'
    input: datetime string with the format of 'yyyy-mm-dd hh:mm:ss'
    return: nth day of the week
    '''

    from datetime import datetime
    import calendar

    try:
        if type(date_time) is str:
            my_string=date_time.split(' ')[0]
            my_date = datetime.strptime(my_string, "%Y-%m-%d")
            return my_date.weekday()
        else:
            raise Exception("'date_time' has unexpected data type, expected sting type")

    except Exception as e:
        print(e)


# utilize the which_day function to find the corresponding weekday
data = pd.read_csv('./US_Accidents_Dec19.csv')

nth_day=[]
date_time=[dt for dt in data['Start_Time']]
for i in range(len(date_time)):
    nth_day.append(which_day(date_time[i]))

# add four new columns 'year', 'month', 'hour', 'weekday' to future grouping
data['year'] = pd.DatetimeIndex(data['Start_Time']).year
data['month'] = pd.DatetimeIndex(data['Start_Time']).month
data['hour'] = pd.DatetimeIndex(data['Start_Time']).hour
data['weekday']=nth_day

#split data by weekdays and weekends
workday_filter = (data['weekday'].isin([0, 1, 2, 3, 4]))
weekend_filter = (data['weekday'].isin([5, 6]))
data_workday = (data.loc[workday_filter])[['hour']]
data_weekend = (data.loc[weekend_filter])[['hour']]

#plot out accidant data with respect to the weekday distribution.
dt_weekday=data.groupby(['weekday'],as_index=False).count().iloc[:,:2]
ax=dt_weekday.plot(kind='bar',width=0.8,figsize=(10, 6),legend=None)
xtick_labels=['Mon.','Tue.','Wed.','Thu.','Fri','Sat.','Sun.']
ax.set_xticks(list(dt_weekday.index))
ax.set_xticklabels(xtick_labels)
ax.set_xlabel('Weekdays',fontsize=14)
ax.set_ylabel('Number of Accidents',fontsize=14)
ax.set_title('Number of accidents by days of week',fontsize=14)
plt.show()
plt.savefig('weekday_distribution_US.png')

# plot the hourly distribution of accidents
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(6, 12),sharex=True)
ax0,ax1=axes.flatten()
kwargs = dict(bins=24,density=False,histtype='stepfilled',linewidth=3)
ax0.hist(list(data_workday['hour']),**kwargs,label='Work days')
ax0.set_ylabel('Number of accidents',fontsize=14)
ax1.hist(list(data_weekend['hour']),**kwargs,label='Only weekend')
ax1.set_ylabel('Number of accidents',fontsize=14)
ax1.set_xlabel('Hour',fontsize=14)
ax0.legend();ax1.legend()
plt.show()
plt.savefig('hourly_distribution_US.png')
