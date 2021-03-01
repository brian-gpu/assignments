import logging
import pandas as pd

def generate_state_df(df):
    s_df = None
    header = 'Agency State'

    try:
        s_df = df.set_index([header]).sort_index()
        logging.info(f'State DF: \n {s_df}')
    except:
        logging.warning(f'Could not index and sort by group - {header}')

    return s_df

def generate_agent_df(df):
    a_df = None
    headers = ['Agent Writing Contract Start Date', 'Date when an agent became A2O']

    try:
        a_df = df[headers]
        agent_name = df[['Agent First Name', 'Agent Middle Name', 'Agent Last Name']].agg(' '.join, axis=1)
        a_df['Agent Name'] = agent_name

        logging.info(f'Agent DF: \n {a_df}')
    except:
        logging.warning(f'Could not retreive headers - {headers}')

    return a_df
