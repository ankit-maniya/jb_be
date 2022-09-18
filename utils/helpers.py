
def filterArray(arrayItems, find_key, value):
    filteredData = [
        item for item in arrayItems if item[f'{find_key}'] == value
    ]

    return filteredData


def filterAmountWithArray(arrayItems, find_key, value):
    filteredData = []
    amountObj = {
        "yearWiseTotalWeight": 0,
        "yearWiseTotalDimonds": 0,
        "yearWiseTotalAmounts": 0,
    }

    for item in arrayItems:
        if item[f'{find_key}'] == value:
            amountObj['yearWiseTotalWeight'] += item['totalDimonds']
            amountObj['yearWiseTotalDimonds'] += item['totalWeight']
            amountObj['yearWiseTotalAmounts'] += item['totalAmounts']

            filteredData.append(item)

    iRes = {
        "filteredData": filteredData,
        "amountObj": amountObj
    }

    return iRes


def uniqueArrOfObjList(arrayItems, year):
    itemList = []

    for x in arrayItems:
        # check if exists in itemList or not
        if x[f'{year}'] not in itemList:
            itemList.append(x[f'{year}'])

    return itemList
