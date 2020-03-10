import pandas as pd

def which_day(date_time):
    '''
    To find out which weekday according to given timestamp
    input: datetime string with the format of 'yyyy-mm-dd hh:mm:ss'
    return: nth day of the week
    '''

    assert isinstance(data_time, string)
    assert len(data_time) > 0

    from datetime import datetime
    import calendar

    try:
        if type(date_time) is str:
            my_string=date_time.split(' ')[0]
            my_date = datetime.strptime(my_string, "%Y-%m-%d")
            return my_date.weekday()
        else:
            raise Exception("'date_time' has unexpected data type, it is expected to be a sting")

    except Exception as e:
        print(e)
