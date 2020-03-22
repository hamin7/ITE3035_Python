# example_1
print("tell me your favorite stuff.")
fruit=input("Your favorite fruite : ")
flower=input("Your favorite flower : ")
drink=input("Your favorite drink : ")
print("you entered :", fruit, flower, drink)

# example_2
input() + "10"      # output=='10010'
input() + 100       # input의 결과는 string이기 때문에 int와 concatenate 불가능.
score = input()     # output없이 변수 score에 string 100이 저장.
score/100           # score는 string이므로 int인 100과 / 연산자 수행 불가능.



# example_3
choiceNum=input("주문 할 상품번호를 적어주세요 1.총,균,쇠 / 2.최고의 교육 / 3.햄릿 :")
if choiceNum == "1":
    choice="1.총,균,쇠"
elif choiceNum == "2":
    choice="2.최고의 교육"
elif choiceNum == "3":
    choice="3.햄릿"
count=input("주문 할 상품의 갯수를 적어주세요: ")
print("당신의 주문내역 : 상품명 :",choice, "갯수 :",count, "주문 완료!")

