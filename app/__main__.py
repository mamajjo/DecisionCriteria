from pandas import read_csv
from app.configuration.config import json_config

def minMaxCriteria(dataSet, labelColumn):
    number = dataset.loc[:, dataset.columns != labelColumn]
    minimumValuesInRows = dataset.min(axis=1)
    indexOfMaximumOfMinimum = minimumValuesInRows.idxmax()
    minMaxCriteriaValue = dataset.loc[indexOfMaximumOfMinimum, dataset.columns == labelColumn]
    return minMaxCriteriaValue

def optimisicCriteria(dataSet, labelColumn):
    number = dataset.loc[:, dataset.columns != labelColumn]
    maximumValuesInRows = dataset.max(axis=1)
    indexOfMaximum = maximumValuesInRows.idxmax()
    maxCriteriaValue = dataset.loc[indexOfMaximum, dataset.columns == labelColumn]
    return maxCriteriaValue

def huwriczCriteria(dataSet, labelColumn, cautionFactor):
    number = dataset.loc[:, dataset.columns != labelColumn]
    minimumValuesInRows = dataset.min(axis=1)
    maximumValuesInRows = dataset.max(axis=1)
    maxHuwricz = 0
    indexOfRow = 0
    bestRow = 0
    for i, (minValue, maxValue) in enumerate(zip(minimumValuesInRows, maximumValuesInRows)):
        huwriczValueInRow = cautionFactor * minValue + (1 - cautionFactor) * maxValue
        if maxHuwricz < huwriczValueInRow:
            maxHuwricz = huwriczValueInRow
            bestRow = i

    # for x in range(len(dataSet.index)) :
    #     print(len(dataSet.index))
    #     huwriczValueInRow = cautionFactor * minimumValuesInRows[x] + (1 - cautionFactor) * maximumValuesInRows[x]
    #     if maxHuwricz < huwriczValueInRow:
    #         maxHuwricz = huwriczValueInRow
    #         bestRow = x
    
    huwriczCriteriaValue = dataset.loc[bestRow, dataset.columns == labelColumn]
    return huwriczCriteriaValue

print(json_config.dataSourceUrl)
dataset = read_csv(json_config.dataSourceUrl)

print("-----------Kryterium Huwricza-----------")
print(huwriczCriteria(dataSet=dataset, labelColumn=json_config.labelColumn, cautionFactor=json_config.cautionFactor))
print("-----------Kryterium Optymistyczne-----------")
print(optimisicCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))
print("-----------Kryterium Walda-----------")
print(minMaxCriteria(dataSet=dataset, labelColumn=json_config.labelColumn))