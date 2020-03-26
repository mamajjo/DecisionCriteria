from pathlib import Path
from pandas import read_json

class Config(object):
    def __init__(self, dataSourceUrl, labelColumn, cautionFactor):
        self.dataSourceUrl = dataSourceUrl
        self.labelColumn = labelColumn
        self.cautionFactor = cautionFactor
        
def as_config(dict):
    dataSetName = dict['chosenDataSet'][0]
    return Config(
        dict[dataSetName]['dataSourceUrl'],
        dict[dataSetName]['labelColumn'],
        dict[dataSetName]['cautionFactor'],
    )

# configuration = json.loads(Path("configuration.json").read_text(), object_hook = as_config)
configuration = read_json("./configuration.json")
json_config = as_config(configuration)