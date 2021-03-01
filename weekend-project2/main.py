import sys
import logging

from file_access import find_filenames, sort_filenames, log_filename, convert_csv, check_latest_line_variance
from data_validation import update_headers, validate_phone_numbers, validate_us_states, validate_email_addresses
from data_process import generate_state_df, generate_agent_df
from data_visualize import create_visualization
from email_send import send_email

# Setup logging
logging.basicConfig(filename='weekend-project2.log', level=logging.INFO, format='%(asctime)s  %(name)s  %(levelname)s  %(message)s')
logging.info("Start logging")

# Access filenames and files
filenames = find_filenames()
filenames = sort_filenames(filenames)

try:
    log_filename(filenames[0])
except Exception as e:
    logging.error(f'Log failed: {e}')
    sys.exit()

try:
    check_latest_line_variance(filenames)
except Exception as e:
    logging.error(f'Check failed: {e}')
    sys.exit()


df = convert_csv(filenames[0])
df = update_headers(df)

# Validation
line_offset = 2
validate_phone_numbers(df, line_offset)
validate_us_states(df, line_offset)
validate_email_addresses(df, line_offset)

# Data processing
logging.info(f'General dataframe:\n {df}')
s_df = generate_state_df(df)
a_df = generate_agent_df(df)

# Data Visualization
create_visualization(a_df, df)

# Send email and stop logging
try:
    send_email()
except Exception as e:
    logging.error(f'Login error - {e}')

logging.info("Stop logging")

