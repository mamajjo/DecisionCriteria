from pandas import read_csv
from app.configuration.config import json_config
import numpy as np

def minMaxCriteria(dataSet, labelColumn):
    minimumValuesInRows = dataSet.min(axis=1)
    indexOfMaximumOfMinimum = minimumValuesInRows.idxmax()
    minMaxCriteriaValue = dataSet.loc[indexOfMaximumOfMinimum, dataSet.columns == labelColumn]
    return minMaxCriteriaValue.values


def optimisticCriteria(dataSet, labelColumn):
    maximumValuesInRows = dataSet.max(axis=1)
    indexOfMaximum = maximumValuesInRows.idxmax()
    maxCriteriaValue = dataSet.loc[indexOfMaximum, dataSet.columns == labelColumn]
    return maxCriteriaValue.values


def huwriczCriteria(dataSet, labelColumn, cautionFactor):
    minimumValuesInRows = dataSet.min(axis=1)
    maximumValuesInRows = dataSet.max(axis=1)
    maxHuwricz = 0
    bestRow = 0
    for i, (minValue, maxValue) in enumerate(zip(minimumValuesInRows, maximumValuesInRows)):
        huwriczValueInRow = cautionFactor * minValue + (1 - cautionFactor) * maxValue
        if maxHuwricz < huwriczValueInRow:
            maxHuwricz = huwriczValueInRow
            bestRow = i

    huwriczCriteriaValue = dataSet.loc[bestRow, dataSet.columns == labelColumn]
    return huwriczCriteriaValue.values

def savageCriteria(dataSet, labelColumn):
    maxInColumn = np.delete(dataSet.max().values, 0)
    dataArray = dataSet.loc[:, dataSet.columns != labelColumn].values
    lowestMax = dataArray.max()
    lowestMaxIndex = 0
    for rowIndex, row in enumerate(dataArray):
        rowRelativeLoses = list(map(lambda i: maxInColumn[i[0]] - row[i[0]], enumerate(row)))
        rowMax = max(rowRelativeLoses)
        if rowMax < lowestMax:
            lowestMax = rowMax
            lowestMaxIndex = rowIndex

    return dataSet.loc[lowestMaxIndex, dataSet.columns == labelColumn].values

def bayesLaplaceCriteria(dataSet, labelColumn, probabilities):
    bestRow = 0
    bestValue = 0
    for rowIndex, row in enumerate(dataSet.loc[:, dataSet.columns != labelColumn].values):
        rowValue = 0
        for i, probability in enumerate(probabilities):
            rowValue += row[i] * probability
        if rowValue > bestValue:
            bestValue = rowValue
            bestRow = rowIndex
    bayesLaplaceCriteriaValue = dataSet.loc[bestRow, dataSet.columns == labelColumn]
    return bayesLaplaceCriteriaValue.values

def printMsg(msg):
    print(f"-----------{msg}-----------")
def printRes(res):
    print(f"{json_config.labelColumn}: {res[0]}")

dataset = read_csv(json_config.dataSourceUrl)
try:
    if(dataset.shape[1] - 1  != len(json_config.probabilities)):
        raise AttributeError('Number of probabilites mismatch number of valued colums')
    if(json_config.cautionFactor < 0 or json_config.cautionFactor > 1):
        raise AttributeError(f"Caution factor must be between 0 or 1 but is: {json_config.cautionFactor}")
    print(f"Caution factor: {json_config.cautionFactor}")
    printMsg("Kryterium Huwricza")
    printRes(huwriczCriteria(dataSet=dataset, labelColumn=json_config.labelColumn, cautionFactor=json_config.cautionFactor))
    printMsg("Kryterium Optymistyczne")
    printRes(optimisticCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
    printMsg("Kryterium Walda")
    printRes(minMaxCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
    printMsg("Kryterium Bayesa-Laplace'a")
    printRes(bayesLaplaceCriteria(dataSet=dataset, labelColumn=json_config.labelColumn, probabilities=json_config.probabilities))
    printMsg("Kryterium Savage'a")
    printRes(savageCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
except AttributeError as error:
    print('in configuration file: ' + repr(error))
except KeyError as keyError:
    print('in configuration file: ' + repr(keyError))