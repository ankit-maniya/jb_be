
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

            yearWiseData['yearWiseTotalWeight'] = round(
                yearWiseData['yearWiseTotalWeight'] + x['totalWeight'], 2)
            yearWiseData['yearWiseTotalDimonds'] += x['totalDimonds']
            yearWiseData['yearWiseTotalAmounts'] = round(
                yearWiseData['yearWiseTotalAmounts'] + x['totalAmounts'], 2)

            idx_month = next((i for i, item in enumerate(
                upList['monthWiseTotal']) if item['month'] == x['month']), -1)

            if idx_month < 0:

                monthWiseData = {
                    "monthWiseTotalWeight": round(x['totalWeight'], 2),
                    "monthWiseTotalDimonds": x['totalDimonds'],
                    "monthWiseTotalAmounts": round(x['totalAmounts'], 2),
                }

                upList['monthWiseTotal'].append(
                    {"month": x['month'], "dayWiseTotal": [x], **monthWiseData})
            else:
                upList['monthWiseTotal'][idx_month]['monthWiseTotalWeight'] = round(
                    upList['monthWiseTotal'][idx_month]['monthWiseTotalWeight'] + x['totalWeight'], 2)
                upList['monthWiseTotal'][idx_month]['monthWiseTotalDimonds'] += x['totalDimonds']
                upList['monthWiseTotal'][idx_month]['monthWiseTotalAmounts'] = round(
                    upList['monthWiseTotal'][idx_month]['monthWiseTotalAmounts'] + x['totalAmounts'], 2)

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
    # # 'totalDimonds': 33985, 'totalWeight': round('2799.85'), 'totalAmounts': 51447.74}

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


def filterDataWithCuttingTypeArray(arrayItems, find_key, value):
    upList = {}

    year_Data = {
        "year_TotalAmounts": 0.0,
        "year_TotalWeight": 0.0,
        "year_TotalDimonds": 0,
        "year_Dimond_TotalAmount": 0.0,
        "year_Dimond_TotalWeight": 0.0,
        "year_Dimond_TotalDimonds": 0,
        "year_Weight_TotalAmount": 0.0,
        "year_Weight_TotalWeight": 0.0,
        "year_Weight_TotalDimonds": 0
    }

    for x in arrayItems:
        if x[f'{find_key}'] == value:

            if upList.get('month_details') is None:
                upList = year_Data
                upList["month_details"] = []

            year_Data['year_TotalWeight'] = round(
                year_Data['year_TotalWeight'] + x['TotalWeight'], 2)
            year_Data['year_TotalDimonds'] += x['TotalDimonds']
            year_Data['year_TotalAmounts'] = round(
                year_Data['year_TotalAmounts'] + x['TotalAmounts'], 2)

            year_Data['year_Dimond_TotalWeight'] = round(
                year_Data['year_Dimond_TotalWeight'] + x['DimondWiseTotalWeight'], 2)
            year_Data['year_Dimond_TotalDimonds'] += x['DimondWiseTotalDimonds']
            year_Data['year_Dimond_TotalAmount'] = round(
                year_Data['year_Dimond_TotalAmount'] + x['DimondWiseTotalAmount'], 2)

            year_Data['year_Weight_TotalWeight'] = round(
                year_Data['year_Weight_TotalWeight'] + x['WeightWiseTotalWeight'], 2)
            year_Data['year_Weight_TotalDimonds'] += x['WeightWiseTotalDimonds']
            year_Data['year_Weight_TotalAmount'] = round(
                year_Data['year_Weight_TotalAmount'] + x['WeightWiseTotalAmount'], 2)

            idx_month = next((i for i, item in enumerate(
                upList['month_details']) if item['l_month'] == x['l_month']), -1)

            if idx_month < 0:

                month_Data = {
                    "month_TotalWeight": round(x['TotalWeight'], 2),
                    "month_TotalDimonds": x['TotalDimonds'],
                    "month_TotalAmounts": round(x['TotalAmounts'], 2),

                    "month_Dimond_TotalWeight": round(x['DimondWiseTotalWeight'], 2),
                    "month_Dimond_TotalDimonds": x['DimondWiseTotalDimonds'],
                    "month_Dimond_TotalAmount": round(x['DimondWiseTotalAmount'], 2),

                    "month_Weight_TotalWeight": round(x['WeightWiseTotalWeight'], 2),
                    "month_Weight_TotalDimonds": x['WeightWiseTotalDimonds'],
                    "month_Weight_TotalAmount": round(x['WeightWiseTotalAmount'], 2),
                }

                upList['month_details'].append(
                    {"l_month": x['l_month'], "day_details": [x], **month_Data})
            else:
                upList['month_details'][idx_month]['month_TotalWeight'] = round(
                    upList['month_details'][idx_month]['month_TotalWeight'] + x['TotalWeight'], 2)
                upList['month_details'][idx_month]['month_TotalDimonds'] += x['TotalDimonds']
                upList['month_details'][idx_month]['month_TotalAmounts'] = round(
                    upList['month_details'][idx_month]['month_TotalAmounts'] + x['TotalAmounts'], 2)

                upList['month_details'][idx_month]['month_Dimond_TotalWeight'] = round(
                    upList['month_details'][idx_month]['month_Dimond_TotalWeight'] + x['DimondWiseTotalWeight'], 2)
                upList['month_details'][idx_month]['month_Dimond_TotalDimonds'] += x['DimondWiseTotalDimonds']
                upList['month_details'][idx_month]['month_Dimond_TotalAmount'] = round(
                    upList['month_details'][idx_month]['month_Dimond_TotalAmount'] + x['DimondWiseTotalAmount'], 2)

                upList['month_details'][idx_month]['month_Weight_TotalWeight'] = round(
                    upList['month_details'][idx_month]['month_Weight_TotalWeight'] + x['WeightWiseTotalWeight'], 2)
                upList['month_details'][idx_month]['month_Weight_TotalDimonds'] += x['WeightWiseTotalDimonds']
                upList['month_details'][idx_month]['month_Weight_TotalAmount'] = round(
                    upList['month_details'][idx_month]['month_Weight_TotalAmount'] + x['WeightWiseTotalAmount'], 2)

                upList['month_details'][idx_month]['day_details'].append(
                    x)
    return upList
