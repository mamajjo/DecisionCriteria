from pandas import read_csv
from app.configuration.config import json_config


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
    print(maxHuwricz)
    return huwriczCriteriaValue


print(json_config.dataSourceUrl)
dataset = read_csv(json_config.dataSourceUrl)

print("-----------Kryterium Huwricza-----------")
print(huwriczCriteria(dataSet=dataset, labelColumn=json_config.labelColumn, cautionFactor=json_config.cautionFactor))
print("-----------Kryterium Optymistyczne-----------")
print(optimisticCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
print("-----------Kryterium Walda-----------")
print(minMaxCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))