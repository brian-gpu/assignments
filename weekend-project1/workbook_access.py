import re
import datetime
import logging
from openpyxl import load_workbook

def get_workbook_date(filename):
    '''
        Summary:
            The date is extracted from the workbook filename              
        Parameters:
            filename (str): the workbook filename to be searched
        
        Returns:
            datetime: the date extracted from workbook
    '''

    filename = filename.lower()
    details = re.split('[_.]', filename)
    months = [
        'january','february','march','april','may','june',
        'july','august','september','october','november','december'
    ]
    month = ''

    for d in details:
        if(month == '' and (d in months)):
            month = d

    if(month != '' and details.index(month) < len(details)):
        index = details.index(month)
        try:
            year = int(details[index+1])
            return datetime.datetime(year, months.index(month)+1, 1)
        except:
            logging.debug('Invalid year')
    else:
            logging.debug('Invalid month')

    return None

def access_workbook(filename):
    '''
        Summary:
            The workbook is loaded              
        Parameters:
            filename (str): the workbook filename to be loaded
        
        Returns:
            Workbook: openpyxl workbook
    '''
    
    wb = None
    try:
        wb = load_workbook(filename = filename, read_only=True, data_only=True)
    except:
        logging.error('Could not open workbook')
    
    return wb

def access_worksheet(name, wb):
    '''
        Summary:
            The named worksheet is acessed from a given workbook              
        Parameters:
            name (str): the name of the worksheet
            wb (Workbook): the openpyxl workbook to be accessed
        
        Returns:
            Worksheet: openpyxl worksheet
    '''

    ws = None
    try:
        ws = wb[name]
    except:
        logging.error('Could not open worksheet')
    
    return ws

def close_workbook(wb):
    '''
        Summary:
            The openpyxl workbook is closed              
        Parameters:
            wb (Workbook): the openpyxl workbook
        
        Returns:
            N/A
    '''
    try:
        wb.close()
    except:
        logging.error('Could not close workbook')
