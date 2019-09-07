import os
import urllib.request
import shutil
import re
import pandas as pd


url = "https://hackerspace.govhack.org/challenges.csv"

pattern = "[A-Z|a-z]*.csv$"
challenges_file_name = re.search(pattern, url).group()

if not os.path.isfile(challenges_file_name):
    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(url) as response, open(challenges_file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


challenges_dataframe = pd.read_csv(challenges_file_name, na_values=['.'])
print(challenges_dataframe)
print(challenges_dataframe.info())
print(challenges_dataframe.head())

print()