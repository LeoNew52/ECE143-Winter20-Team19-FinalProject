import csv
from datetime import datetime #for time related data entries

#Examples:
#header,data=import_data('US_Accidents_Dec19.csv',samples=10)
#header,data=import_data('US_Accidents_Dec19.csv',read='col',samples=10,col_num=4)

def type_cast(func,data_entry,*args):
    """
    Applies 'func' on 'data_entry'. It is used as a type casting function. It takes care of edge cases.
    Retruns None if data_entry is uncastable
    :data_entry: string
    :func: function
    """
    assert isinstance(data_entry,str)
    assert callable(func)
    try:
        out=func(data_entry,*args)
    except:
        out=None
    return out

def format_row(row):
    """
    A formatting function specific to our US accidents dataset
    :row: input list, which is a row from the dataset
    """
    assert isinstance(row,list)
    
    data_row=[0]*len(header) #Formatted data row to be output and appeneded to 'data'
    
    for i in [0,1,11,13,14,15,16,17,19,20,21,28,31,45,46,47,48]: data_row[i]=row[i] #emptry string will NOT return None
    for i in [2,3,12,18]: data_row[i]=type_cast(lambda x: int(float(x)),row[i])
    for i in [6,7,8,9,10,23,24,25,26,27,29,30]: data_row[i]=type_cast(float,row[i])
    for i in [4,5,22]: data_row[i]=type_cast(datetime.strptime,row[i],'%Y-%m-%d %H:%M:%S')
    for i in range(32,45):
        if row[i]=='False': data_row[i]=False #bool('False') returns True!
        elif row[i]=='True': data_row[i]=True
        else: data_row[i]=None
    return data_row

def format_column(data,col_num):
    """
    Similar to format_row, except it takes a single data entery with its column number to typecast it
    based on its column number.
    :data: variable to by typecasted
    :col_num: int, assigned column number
    """
    assert isinstance(col_num,int) and col_num>=0
    
    if col_num in [0,1,11,13,14,15,16,17,19,20,21,28,31,45,46,47,48]: return data #emptry string will NOT return None
    if col_num in [2,3,12,18]: return type_cast(lambda x: int(float(x)),data)
    if col_num in [6,7,8,9,10,23,24,25,26,27,29,30]: return type_cast(float,data)
    if col_num in [4,5,22]: return type_cast(datetime.strptime,data,'%Y-%m-%d %H:%M:%S')
    if col_num in range(32,45):
        if data=='False': return False #bool('False') returns True!
        elif data=='True': return True
        else: return None
    
def import_data(fname,read='row',samples=None,col_num=None):
    """
    A function that imports the data from a csv file 'fname'. It returns the header and data as lists.
    You can return a partial sample by specifying the number of samples. Otherwise, it will return all samples
    :fname: string
    :read: str to indicate wether to read rows or columns
    :samples: int
    :col_num: column number to read from if read=='col'
    """
    assert isinstance(fname,str)
    assert (isinstance(samples,int) and n>0) or samples is None
    assert read=='row' or (read=='col' and isinstance(col_num,int) and col_num>=0)
    
    #import CSV file
    
    f=open(fname,'r',newline='')
    reader=csv.reader(f)
    header=next(reader)
    data=[]
    
    #Format database, since CSV is all strings. If data empty or formatted incorrectly, then return None.
    
    #Row import
    if read=='row':
        if isinstance(samples,int): #Import sample
            for j in range(samples):
                row=next(reader)
                data.append(format_row(row))
        elif samples is None: #Import all
            for row in reader:
                data.append(format_row(row))
        else:
            raise 'samples variable error'
    
    #Column import
    if read=='col':
        if isinstance(samples,int): #Import sample
            for j in range(samples):
                row=next(reader)
                data.append(format_column(row[col_num],col_num))
        elif samples is None: #Import all
            for row in reader:
                data.append(format_column(row[col_num],col_num))
        else:
            raise 'samples variable error'
            
    return header,data
