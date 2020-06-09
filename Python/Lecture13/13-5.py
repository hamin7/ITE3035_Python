test2 = {}      # [], ()
while True:
    dept = input('dept name:')
    if dept == 'q':
        break
    deposit = int(input('deposit:'))
    test2[dept] = deposit

while True:
    dept = input('dept(검색):')
    if dept == 'q':
        break
    if dept in test2:
        print(dept, '의 deposit', test2[dept])