import re
import logging
import pandas as pd

def update_headers(df):
    try:
        df.rename(columns={
            "Agent Writing Contract Start Date (Carrier appointment start date)": 'Agent Writing Contract Start Date',
            "Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)": 'Agent Writing Contract Status'
        })
        logging.info('Successfully updated header')
    except:
        logging.warning('Failed to update header')

    return df

def is_phone_number(phone_number):
    match = re.match(r'[0-9]{3}.[0-9]{3}.[0-9]{4}', phone_number)
    
    if match:
        return True

    return False

def is_us_state(state):
    us_states = {
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    }

    if state in us_states:
        return True
    
    return False

def validate_phone_numbers(df, line_offset):
    agency_phone_numbers = None
    agent_phone_numbers = None

    try:
        header = 'Agency Phone Number'
        agency_phone_numbers = df[header]

        for row, phone_number in agency_phone_numbers.items():
            if is_phone_number(phone_number) == False:
                line_number = row + line_offset
                logging.info(f'Invalid {header} at line {line_number}')
    except:
        logging.warning(f'No {header} header detected')

    try:
        header = 'Agent Phone Number'
        agent_phone_numbers = df[header]

        for row, phone_number in agent_phone_numbers.items():
            if is_phone_number(phone_number) == False:
                line_number = row + line_offset
                logging.info(f'Invalid {header} at line {line_number}')
    except:
        logging.warning(f'No {header} header detected')

def validate_us_states(df, line_offset):
    agency_states = None
    
    try:
        header = 'Agent State'
        agency_states = df[header]
        
        for row, state in agency_states.items():
            if is_us_state(state) == False:
                line_number = row + line_offset
                logging.info(f'Invalid {header} at line {line_number}')
    except:
        logging.warning(f'No {header} header detected')

def is_email_address(email):
    match = None
    max_length = 321

    if len(email) < max_length:
        match = re.match(r'([a-z0-9]+)(([.-]{1}[a-z0-9]+)*)@([a-z0-9]+)(([.-]{1}[a-z0-9]+)*)(.[a-z]{2,3})', email.lower())
    
    if match:
        return True
    
    return False


def validate_email_addresses(df, line_offset):
    agent_email_addresses = None

    try:
        header = 'Agent Email Address'
        agent_email_addresses = df[header]

        for row, email in agent_email_addresses.items():
            if is_email_address(email) == False:
                line_number = row + line_offset
                logging.info(f'Invalid {header} at line {line_number}')
    except:
        logging.warning(f'No {header} header detected')