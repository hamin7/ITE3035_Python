# 100 만큼 앞으로 간다
# 90도 꺽는다
import turtle as t
t.shape('turtle')

i = 1
while i <= 4:
    t.fd(100)
    t.speed(1)
    t.right(360/4)
    i=i+1