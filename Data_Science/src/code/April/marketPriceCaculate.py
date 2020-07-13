import csv
import sys

input_file = "marketPriceSource.csv"
output_file = "marketPrice.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwriter = csv.writer(csv_out_file)
        next(freader)
        indexList = ['Timestamp', 'Price']
        marketPriceList = []

        fwriter.writerow(indexList)

        for row_list in freader:
            tag = str(row_list[0]).strip()  # marketPrice인 row를 찾기 위해 tag 붙임.
            if tag == 'marketPrice':
                marketPriceList.append(row_list[1].strip())
                marketPriceList.append(row_list[2].strip())
                print(marketPriceList)
                fwriter.writerow(marketPriceList)
                marketPriceList = []    # marketPriceList 초기화
