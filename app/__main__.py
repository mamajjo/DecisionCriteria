from pandas import read_csv
from app.configuration.config import json_config

print(json_config.dataSourceUrl)
dataset = read_csv(json_config.dataSourceUrl)

print(dataset)