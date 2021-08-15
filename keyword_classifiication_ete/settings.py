import re

MAX_SEQUENCE_LENGTH = 250
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
labels = ['Bank account or service', 'Consumer Loan', 'Credit card', \
       'Credit reporting', 'Debt collection',
          'Money transfers', 'Mortgage', \
       'Other financial service', 'Payday loan', 'Prepaid card', \
       'Student loan']

model_file_path = ""
tokenizer_path = ""