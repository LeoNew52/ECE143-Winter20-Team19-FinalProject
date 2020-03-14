import collections
import csv
def factor1_county(fname):
    '''
    Find the number of accidents happened in each county and their ratio.
    :input fname: string the file name
    :output percentage: the percentage of accidents happened in each county
    '''
    

    assert isinstance(fname, str)
    
    f = open(fname,'r',newline ='')
    reader = csv.reader(f)
    header = next(reader)
    
    county_list = []

    for row in reader:
        county_list.append(row[16])
        
    
    freq = collections.Counter(county_list)
    percentage = {}
    total_case = sum(freq.values())
    for key,value in freq.items():
        percentage[key] = value/total_case
    
    
    
    f.close()
    return freq.items()
