print('enter your weight, height')
weight=float(input('weight:'))
height=float(input('height:'))
bmi=weight/height*height
if bmi > 25:
    print('비만')
else:
    print('정상')