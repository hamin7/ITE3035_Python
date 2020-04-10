import csv
import sys

input_file = "orderBookSample.csv"
output_file = "marketPriceSource.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwriter = csv.writer(csv_out_file)
        next(freader)
        prevType = 0
        prevPrice = 0
        prev_row_list = []
        filtered_list = []
        for row_list in freader:
            price = row_list[0].strip() # 0번째는 가격, strip으로 문자열 양끝 공백, 탭, 개행문자 제거
            type = row_list[2].strip()  # 2번째는 type (0이면 파는, 1이면 사는)
            if prevType == '0' and type == '1':
                timeStamp = row_list[3].strip() # 현재 시간
                fwriter.writerow(prev_row_list) # 시세를 계산할 판매 희망 최소 가격
                fwriter.writerow(row_list) # 시세를 계산할 구매 희망 최대 가격
                marketPrice = (int(prevPrice)+int(price))/2     # 시세
                print (marketPrice)
                filtered_list.append('marketPrice')
                filtered_list.append(timeStamp)
                filtered_list.append(marketPrice)
                print(filtered_list)
                fwriter.writerow(filtered_list)
                filtered_list = []  # filtered_list 초기화
            prevType = type # 현재 type을 prevType에 저장
            prevPrice = price   # 현재 price를 prevPrice에 저장
            prev_row_list = row_list # 현재 row_list를 prev_row_list에 저장

