from pandas import read_csv, DataFrame
from app.configuration.config import json_config
import numpy as np
from numpy import all, any, delete, transpose
import matplotlib.pyplot as pl
from pymprog import *

def minMaxCriteria(dataSet):
    # A
    minimumValuesInRows = dataSet.min(axis=1)
    indexOfMaximumOfMinimum = minimumValuesInRows.idxmax()

    # B
    maximumValuesInRows = dataSet.max()
    indexOfMinimumMaximum = maximumValuesInRows.idxmin()

    gameValue = dataSet.iloc[indexOfMaximumOfMinimum, indexOfMinimumMaximum]
    return gameValue, minimumValuesInRows.max() == maximumValuesInRows.min()

def clearDominated(dataset):
    data = dataset.values
    # rows
    for r in range(len(data)):
        for r2 in range(r+1, len(data)):
            diff = data[r] - data[r2]
            if(not any(list(map(lambda x: x > 0, diff))) and any(list(map(lambda x: x < 0, diff)))):
                data = delete(data, r, axis=0)
            if(not any(list(map(lambda x: x < 0, diff))) and any(list(map(lambda x: x > 0, diff)))):
                data = delete(data, r2, axis=0)
    # columns
    data = transpose(data)
    for r in range(len(data)):
        for r2 in range(r+1, len(data)):
            diff = data[r2] - data[r]
            if(not any(list(map(lambda x: x > 0, diff))) and any(list(map(lambda x: x < 0, diff)))):
                data = delete(data, r, axis=0)
            if(not any(list(map(lambda x: x < 0, diff))) and any(list(map(lambda x: x > 0, diff)))):
                data = delete(data, r2, axis=0)
    data = transpose(data)
    return data

def printMixedStrategy(dataset):
    data = dataset.values
    begin('game')
    # gain of player 1, a free variable
    v = var('gameValue', bounds=(None,None))
    # mixed strategy of player 2
    p = var('p', len(data[0])) 
    # probability sums to 1
    sum(p) == 1
    # player 2 chooses p to minimize v
    minimize(v) 
    # player 1 chooses the better value 
    inequalities = [v >= sum([p[i]*row[i] for i in range(len(row))]) for row in data]
    solve()
    print('Game value: %g'% v.primal)
    print("Mixed Strategy for player A:")
    print([f"A{i+1}: {x.dual}" for i,x in enumerate(inequalities)])
    print("Mixed Strategy for player B:")
    print([f"B{i+1}: {x.primal}" for i,x in enumerate(p)])
    end()

def printMsg(msg):
    print(f"-----------{msg}-----------")
def printRes(res):
    if (res[1] == True):
        print(f"There is a saddle point with value: {res[0]}")
    else:
        print(f"There is no saddle point")

dataset = read_csv(json_config.dataSourceUrl, header=None)
try:
    if(len(dataset.index) < 0):
        raise AttributeError(f"At least one row of data is required")
    dataset = DataFrame(data=clearDominated(dataset))
    printMsg("Wald's criterium")
    waldSolution = minMaxCriteria(dataSet=dataset)
    printRes(waldSolution)
    if (waldSolution[1] != True):
        printMixedStrategy(dataset)

except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))
