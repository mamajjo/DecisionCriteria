from pandas import read_csv, DataFrame
from app.configuration.config import json_config
import numpy as np
from numpy import all, any, delete, transpose
import matplotlib.pyplot as pl
from pymprog import *


def printMsg(msg):
    print(f"-----------{msg}-----------")


dataset = read_csv(json_config.dataSourceUrl, header=None)
try:
    if(len(dataset.index) < 0):
        raise AttributeError(f"At least one row of data is required")

except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))
