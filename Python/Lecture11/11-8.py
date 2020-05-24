import turtle as t

t.shape('circle')
poly = int(input('poly:'))
for i in range(poly):
    t.speed(1)
    t.fd(100)
    t.right(360/poly)