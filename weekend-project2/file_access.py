import os
import re
import logging
import pandas as pd

def find_filenames():
    filenames = []

    try:
        filenames = os.listdir()
        logging.info('Accessed the current directory ')
    except:
        logging.error('Could not access the current directory')
    
    try:
        filenames = list(filter(lambda name: re.match(r'NYL_FieldAgent_[0-9]{8}.csv', name) != None, filenames))
        logging.info('Filtered the output of the current directory')
    except:
        logging.warning('Could not filter the output of the current directory')

    return filenames

def sort_filenames(filenames):
    sorted_filenames = []

    try:
        sorted_filenames = sorted(filenames, reverse=True)
        logging.info('Sorted filenames')
    except:
        logging.warning('Could not sort the filenames')
    
    return sorted_filenames

def check_filename(filename):
    destination = 'NYL.lst'
    processed_files = []

    try:
        file = open(destination, 'r')
        logging.info(f'Checked file - {destination}')
    except:
        logging.error(f'Could not open file - {destination}')

    try:
        processed_files = file.readlines()
        processed_files = list(map(lambda f: f.rstrip('\n'), processed_files))
        logging.info(f'Read from file - {destination}')
    except:
        logging.error(f'Could not read file - {destination}')
    
    try:
        file.close()
        logging.info(f'Closed file - {destination}')
    except:
        logging.error(f'Could not close file - {destination}')

    if filename in processed_files:
        raise Exception(f'Already processed {filename}')

def log_filename(filename):
    destination = 'NYL.lst'
    file = None

    try:
        check_filename(filename)
    except Exception as e:
        raise Exception(e)

    try:
        file = open(destination, 'a')
        logging.info(f'Opened file - {destination}')
    except:
        logging.error(f'Could not open file - {destination}')

    try:
        file.write(filename + '\n')
        logging.info(f'Wrote to file - {destination}')
    except:
        logging.error(f'Could not write to file - {destination}')

    try:
        file.close()
        logging.info(f'Closed file - {destination}')
    except:
        logging.error(f'Could not close file - {destination}')
    

def convert_csv(filename):
    df = None

    try:
        df = pd.read_csv(filename)
        logging.info(f'Converted csv - {filename}')
    except:
        logging.error(f'Could not convert csv - {filename}')

    return df

def check_latest_line_variance(filenames):
    latest_line_count = 0
    previous_line_count = 0
    acceptable_variance = 500

    try:
        latest_line_count = len(convert_csv(filenames[0]).index)
    except:
        logging.warning('No latest csv detected')

    try:
        previous_line_count = len(convert_csv(filenames[1]).index)
    except:
        logging.warning('No previous csv detected')

    variance = latest_line_count - previous_line_count
    
    if abs(variance) <= acceptable_variance:
        logging.info('Variance check passed')
    else:
        raise Exception('Variance check failed')
