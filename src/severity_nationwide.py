import src.importData as iD
import pandas as pd
def is_highway(description):
    '''
    Determines from description whether or not an accident occured in a highway
    :description: list of strings
    '''
    assert isinstance(description, list)
    for x in description: assert isinstance(x,str)
    out=[False]*len(description)
    for i,line in enumerate(description):
        if '-' in line:
            out[i]=True
    return out
def get_day_of_week(time):
    out=[]
    for i in time:
        out.append(i.strftime('%A'))
    return out
def get_highway_accidents_and_severity():
    header,severity=iD.import_data('US_Accidents_Dec19.csv',read='col',samples=None,col_num=3)
    header,description=iD.import_data('US_Accidents_Dec19.csv',read='col',samples=None,col_num=11)
    header,start_time=iD.import_data('US_Accidents_Dec19.csv',read='col',samples=None,col_num=4)
    day_of_week=get_day_of_week(start_time)
    highway=is_highway(description)
    return pd.DataFrame({'Severity':severity,'Highway':highway,'Day of Week':day_of_week})
