import datetime
import logging
from value_helper import format_value

def access_report(date, ws):
    '''
        Summary:
            Accesses the data related to the date, on a given worksheet
        Parameters:
            date (datetime): the date to search
            ws (Worksheet): the openpyxl worksheet to access
            
        Returns:
            list: of each entry found, in format [label, value]
    '''

    date_index = None
    report = []

    try:
        data = list(map(lambda row:
                            list(map(lambda col: col.value, row)), ws))
        dates = list(map(lambda x: x[0], data))

    except:
        logging.error("Report is inaccessible")
        return report

    for d in dates:
        try:
            if date_index == None and d.month == date.month and d.year == date.year:
                date_index = dates.index(d)
        except:
            logging.debug("Cell is not datetime")
    
    if date_index != None:
        for col in range(1, 6):
            report.append((data[0][col], data[date_index][col]))
        
    return report
    
def format_report(report):
    '''
        Summary:
            Formats the results of a searched report
        Parameters:
            report (list): the list of found entries in format [label, value] 
            
        Returns:
            str: the report in format  label : value
    '''

    output = '\n\n\n'
    for entry in report:
        value = format_value(entry[1])
        output += entry[0].lstrip().rstrip() + ' : ' + value + '\n'
    
    return output