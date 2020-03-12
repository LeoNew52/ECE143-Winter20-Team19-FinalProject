import csv
import datetime
import pandas as pd
from import_data import format_row
from import_data import format_column
from import_data import import_data
from import_data import type_cast

#########################################################################################
#                                                                                       #
# Definition:                                                                           #
#                                                                                       #
#    get_cali_data(fname)                                                               #
#                                                                                       #
#    A function that get all the data that has 'State' value as 'CA'.                   #
#    :input fname: string the file name of input data                                   #
#                                                                                       #
#########################################################################################
def get_cali_data(fname):
    '''
    Get all the accidents data that happened in California from the data set and put it in a file. 
    This function is only specified for this certain file. 
    :input fname: string the file name
    '''
    
    assert isinstance(fname, str)
    
    f = open(fname,'r',newline ='')
    reader = csv.reader(f)
    header = next(reader)
    
    with open('CA_data.csv','w',newline = '') as csvfile:
        writer = csv.writer(csvfile,delimiter =',',quotechar ='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for row in reader:
            if row[17] == 'CA':
                writer.writerow(row)
            else:
                pass
    f.close()