def which_day(date_time):
    '''
    To find out which weekday according to given timestamp
    input: datetime string with the format of 'yyyy-mm-dd hh:mm:ss'
    return: nth day of the week
    '''

    assert isinstance(date_time, str)
    assert len(date_time) > 0

    from datetime import datetime
    import calendar
    import pandas as pd

    try:
        if type(date_time) is str:
            my_string=date_time.split(' ')[0]
            my_date = datetime.strptime(my_string, "%Y-%m-%d")
            return my_date.weekday()
        else:
            raise Exception("'date_time' has unexpected data type, it is expected to be a sting")

    except Exception as e:
        print(e)
