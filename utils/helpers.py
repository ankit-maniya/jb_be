from math import ceil
from decimal import Decimal


def filterArray(arrayItems, find_key, value):
    filteredData = [
        item for item in arrayItems if item[f'{find_key}'] == value
    ]

    return filteredData


def filterAmountWithArray(arrayItems, find_key, value):
    upList = {}

    yearWiseData = {
        "yearWiseTotalWeight": 0,
        "yearWiseTotalDimonds": 0,
        "yearWiseTotalAmounts": 0,
    }

    for x in arrayItems:
        if x[f'{find_key}'] == value:

            if upList.get('monthWiseTotal') is None:
                upList = yearWiseData
                upList["monthWiseTotal"] = []

            yearWiseData['yearWiseTotalWeight'] = Decimal(
                yearWiseData['yearWiseTotalWeight']) + Decimal(x['totalWeight'])
            yearWiseData['yearWiseTotalDimonds'] += x['totalDimonds']
            yearWiseData['yearWiseTotalAmounts'] = Decimal(
                yearWiseData['yearWiseTotalAmounts']) + Decimal(x['totalAmounts'])

            monthWiseData = {
                "monthWiseTotalWeight": 0,
                "monthWiseTotalDimonds": 0,
                "monthWiseTotalAmounts": 0,
            }

            monthWiseData['monthWiseTotalWeight'] += ceil(
                x['totalWeight']*100)/100
            monthWiseData['monthWiseTotalDimonds'] += x['totalDimonds']
            monthWiseData['monthWiseTotalAmounts'] += ceil(
                x['totalAmounts']*100)/100

            idx_month = next((i for i, item in enumerate(
                upList['monthWiseTotal']) if item['month'] == x['month']), -1)

            if idx_month < 0:
                upList['monthWiseTotal'].append(
                    {"month": x['month'], "dayWiseTotal": [x], **monthWiseData})
            else:
                upList['monthWiseTotal'][idx_month]['dayWiseTotal'].append(
                    x)
    return upList


def uniqueArrOfObjList(arrayItems, year):
    itemList = []

    for x in arrayItems:
        # check if exists in itemList or not
        if x[f'{year}'] not in itemList:
            itemList.append(x[f'{year}'])

    return itemList

# upList = []
    # # {
    # #     "year": 2021,
    # #     "monthWiseTotal": [
    # #         {
    # #             "month": 8,
    # #             "dayWiseTotal": [
    # #                 {
    # #                     "date": 1
    # #                 }
    # #             ]
    # #         }
    # #     ],
    # # }

    # # {'l_entrydate': datetime.date(2022, 1, 1), 'year': 2022, 'month': 1, 'day': 1, 'totalDateWiseLoats': 189,
    # # 'totalDimonds': 33985, 'totalWeight': Decimal('2799.85'), 'totalAmounts': 51447.74}

    # for x in arrayItems:
    #     # check if exists in itemList or not
    #     idx_year = next((i for i, item in enumerate(
    #         upList) if item['year'] == x['year']), -1)

    #     yearWiseData = {
    #         "yearWiseTotalWeight": 0,
    #         "yearWiseTotalDimonds": 0,
    #         "yearWiseTotalAmounts": 0,
    #     }
    #     if idx_year >= 0:

    #         yearWiseData['yearWiseTotalWeight'] += x['totalDimonds']
    #         yearWiseData['yearWiseTotalDimonds'] += x['totalWeight']
    #         yearWiseData['yearWiseTotalAmounts'] += x['totalAmounts']
    #         # already_exists_month = [element for element in upList[idx_year]['monthWiseTotal']
    #         #             if element['month'] == x['month']]
    #         idx_month = next((i for i, item in enumerate(
    #             upList[idx_year]['monthWiseTotal']) if item['month'] == x['month']), -1)

    #         monthWiseData = {
    #             "monthWiseTotalWeight": 0,
    #             "monthWiseTotalDimonds": 0,
    #             "monthWiseTotalAmounts": 0,
    #         }

    #         monthWiseData['monthWiseTotalWeight'] += ceil(
    #             x['totalDimonds']*100)/100
    #         monthWiseData['monthWiseTotalDimonds'] += ceil(
    #             x['totalWeight']*100)/100
    #         monthWiseData['monthWiseTotalAmounts'] += ceil(
    #             x['totalAmounts']*100)/100

    #         if idx_month < 0:
    #             upList[idx_year]['monthWiseTotal'].append(
    #                 {"month": x['month'], "dayWiseTotal": [], "amt_obj": monthWiseData})
    #         else:
    #             upList[idx_year]['monthWiseTotal'][idx_month]['dayWiseTotal'].append(
    #                 x)

    #         if upList[idx_year]['year'] != x['year']:
    #             upList.append(
    #                 {"year": x[f'{year}'], "monthWiseTotal": [], "amt_obj": yearWiseData})
    #     else:
    #         yearWiseData['yearWiseTotalWeight'] += x['totalDimonds']
    #         yearWiseData['yearWiseTotalDimonds'] += x['totalWeight']
    #         yearWiseData['yearWiseTotalAmounts'] += x['totalAmounts']

    #         upList.append(
    #             {"year": x[f'{year}'], "monthWiseTotal": [], "amt_obj": yearWiseData})
