import datetime
import logging
from value_helper import format_value

def access_score(date, ws):
    '''
        Summary:
            Accesses the score data related to the date, on a given worksheet
        Parameters:
            date (datetime): the date to search
            ws (Worksheet): the openpyxl worksheet to access
            
        Returns:
            list: of each entry found, in format [label, value]
    '''
    date_index = None
    score = []

    try:
        data = list(map(lambda row:
                            list(map(lambda col: col.value, row)), ws))
        dates = list(map(lambda x: x, data[0]))

    except:
        logging.error("Score is inaccessible")
        return score

    for d in dates:
        try:
            if date_index == None and d.month == date.month and d.year == date.year:
                date_index = dates.index(d)
        except:
            logging.debug("Cell is not datetime")
    
    if date_index != None:
        label_index = 0

        for pos in range(date_index, -1, -1):
            if dates[pos] == None:
                label_index = pos
                break

        score = list(map(lambda x: [x[label_index].value, x[date_index].value], ws))
        score = score[1:]
        score = list(filter(lambda x: not(x[0] == None and x[1] == None), score))
    
    return score

def format_score(score):
    '''
        Summary:
            Formats the results of a searched score
        Parameters:
            score (list): the list of found entries in format [label, value] 
            
        Returns:
            str: the score in format  label : value, detected 
                    headers are encased in hypens
    '''

    output = '\n\n'
    for entry in score:
        entry = format_rating(entry)
        if entry[0] != None:
            if entry[1] != None:
                output += '\n' + entry[0].lstrip().rstrip()
                value = format_value(entry[1]) 
                output += ' : ' + value
            else:
                output += '\n\n' + ('-' * len(entry[0]))
                output += '\n' + entry[0].lstrip().rstrip() 
                output += '\n' + ('-' * len(entry[0]))
        else:
            value = format_value(entry[1])
            output += '\t\t' + value
    
    return output

def format_rating(score):
    '''
        Summary:
            The score is transformed if a rater label is detected -
                label is set to Promoters, Passives, or Detractors
                value is set to good or bad
                
        Parameters:
            score (list): format is label : value
        
        Returns:
            list: format is label : value
    '''

    try:
        match  = score[0].lower().split('(')
    except:
        return score

    if len(match) > 1:
        if match[1] == 'recommend score 9 to 10)':
            score[0] = 'Promoters'
            if score[1] > 200:  
                score[1] = 'good'
            else:  
                score[1] = 'bad'
        elif match[1] == 'recommend score 7 to 8)':
            score[0] = 'Passives'
            if score[1] > 100:  
                score[1] = 'good'
            else:  
                score[1] = 'bad'
        elif match[1] == 'recommend score 0 to 6)':
            score[0] = 'Detractors'
            if score[1] < 100:  
                score[1] = 'good'
            else:  
                score[1] = 'bad'

    return score