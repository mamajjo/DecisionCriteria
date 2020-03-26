from pathlib import Path
from pandas import read_json

class Config(object):
    def __init__(self, dataSourceUrl):
        self.dataSourceUrl = dataSourceUrl

def as_config(dict):
    dataSetName = dict['chosenDataSet'][0]
    print(dict[dataSetName])
    return Config(
        dict[dataSetName]['dataSourceUrl']
    )

# configuration = json.loads(Path("configuration.json").read_text(), object_hook = as_config)
configuration = read_json("./configuration.json")
json_config = as_config(configuration)