from pandas import read_csv
from app.configuration.config import json_config
import numpy as np


def minMaxCriteria(dataSet, labelColumn):
    minimumValuesInRows = dataSet.min(axis=1)
    indexOfMaximumOfMinimum = minimumValuesInRows.idxmax()
    minMaxCriteriaValue = dataSet.loc[indexOfMaximumOfMinimum, dataSet.columns == labelColumn]
    return minMaxCriteriaValue


def optimisticCriteria(dataSet, labelColumn):
    maximumValuesInRows = dataSet.max(axis=1)
    indexOfMaximum = maximumValuesInRows.idxmax()
    maxCriteriaValue = dataSet.loc[indexOfMaximum, dataSet.columns == labelColumn]
    return maxCriteriaValue


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
    return huwriczCriteriaValue


def countRelativeLoses(i, maxInColumn, row):
    return maxInColumn[i] - row[i]


def savageCriteria(dataSet, labelColumn):
    maxInColumn = np.delete(dataSet.max().values, 0)
    dataArray = dataSet.loc[:, dataSet.columns != labelColumn].values
    relativeLoses = map(countRelativeLoses, dataArray, maxInColumn)
    lowestMax = dataArray.max()
    lowestMaxIndex = 0
    for rowIndex, row in enumerate(dataArray):
        rowRelativeLoses = list(map(lambda i: countRelativeLoses(i[0], maxInColumn, row), enumerate(row)))
        rowMax = max(rowRelativeLoses)
        if rowMax < lowestMax:
            lowestMax = rowMax
            lowestMaxIndex = rowIndex

    return dataSet.loc[lowestMaxIndex, dataSet.columns == labelColumn]

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
    return bayesLaplaceCriteriaValue


print(json_config.dataSourceUrl)
dataset = read_csv(json_config.dataSourceUrl)

print("-----------Kryterium Huwricza-----------")
print(huwriczCriteria(dataSet=dataset, labelColumn=json_config.labelColumn, cautionFactor=json_config.cautionFactor))
print("-----------Kryterium Optymistyczne-----------")
print(optimisticCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
print("-----------Kryterium Walda-----------")
print(minMaxCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
print("-----------Kryterium Bayesa-Laplace'a-----------")
print(bayesLaplaceCriteria(dataSet=dataset, labelColumn=json_config.labelColumn, probabilities=json_config.probabilities))
print("-----------Kryterium Savage'a-----------")
print(savageCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
