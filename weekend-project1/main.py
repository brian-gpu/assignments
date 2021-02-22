import sys
import datetime
import logging

from workbook_access import access_workbook, access_worksheet, close_workbook, get_workbook_date
from report_access import access_report, format_report
from score_access import access_score, format_score

# Setup logging
logging.basicConfig(filename='mini-project.log', level=logging.INFO, format='%(asctime)s  %(name)s  %(levelname)s  %(message)s')
logging.info("Start logging")

# Retrieve filename
filename = ''
try:
    filename = sys.argv[1]
except:
    logging.error("Filename not provided")

# Retrieve date info and acces workbook
date = get_workbook_date(filename)
wb = access_workbook(filename)

# Access, format, and log info from 'Summary Rolling MoM'
worksheet1 = 'Summary Rolling MoM'
ws = access_worksheet(worksheet1, wb)
report = access_report(date, ws)
logging.info(format_report(report))

# Access, format, and log info from 'VOC Rolling MoM'
worksheet2 = 'VOC Rolling MoM'
ws = access_worksheet(worksheet2, wb)
score = access_score(date, ws)
score = format_score(score)
logging.info(score)

# Close workbook and quit logging
close_workbook(wb)
logging.info("Quit logging")