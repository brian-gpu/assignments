import logging
import pandas as pd
import matplotlib
from data_process import generate_agent_df, generate_state_df
from file_access import convert_csv

def create_visualization(a_df, g_df):

    # Plot 1: Running Total - Active Contracts
    try:
        y_df = a_df.groupby(['Agent Writing Contract Start Date'])['Agent Writing Contract Start Date'].count().reset_index(name='count')
        y_df['Agent Writing Contract Start Date'] = y_df['Agent Writing Contract Start Date'].apply(lambda x: x.rstrip())
        y_df['Agent Writing Contract Start Date'] = y_df[y_df['Agent Writing Contract Start Date'] != '']
        y_df['Agent Writing Contract Start Date'] = pd.to_datetime(y_df['Agent Writing Contract Start Date'], format='%m/%d/%Y')

        y_df = y_df.set_index(['Agent Writing Contract Start Date'])
        y_df = y_df.sort_index()
    except:
        logging.warning('Datetime Error')

    try: 
        value = 0
        for index in range(0, len(y_df)):
            value += y_df.iat[index, 0]
            y_df.iat[index, 0] = value
    except:
        logging.warning('Running total error')

    try:
        plot1 = y_df.plot(lw=2, title='Running Total - Active Contracts', grid=True, legend=False, ylabel='# of Contracts', figsize=(20,15))
    except:
        logging.warning('Could not create running total plot')

    # Plot 2: Number of Agents by State
    try:
        z_df = g_df.groupby(by=['Agency State'], dropna=True)['Agency State'].count().reset_index(name='# of Agents')
        z_df = z_df.sort_values(by=['# of Agents'], ascending=True)
        z_df = z_df.set_index('Agency State')
    except:
        logging.warning('Agency data error')
    
    try:
        plot2 = z_df.plot.barh(grid=True, xlabel='US States', figsize=(15,15), title='Number of Agents by State' )
    except:
        logging.warning('Could not create agents by state plot')


    try:
        matplotlib.rcParams.update({'font.size': 14})
    except:
        logging.warning('Could not configure matplotlib')

    # Save plots
    try:
        image1 = plot1.get_figure()
        image1.savefig('plot1.png', bbox_inches='tight')
        logging.info('Saved: Running total plot - plot1.png')
    except:
        logging.warning('Could not save plot 1')

    try:
        image2 = plot2.get_figure()
        image2.savefig('plot2.png', bbox_inches='tight')
        logging.info('Saved: Agents by state plot - plot2.png')
    except:
        logging.warning('Could not save plot 2')
