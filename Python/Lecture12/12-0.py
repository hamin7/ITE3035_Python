colors=['black','red','white','blue','pink']
print(colors)
colors.append('test')
print(colors)
colors.insert(0,'test2')
print(colors)
del colors[0]
print(colors)
colors.remove('test')
print(colors)
colors[1]='grey'
print(colors)

wears=['skirt','shirts']
clothes=[colors,wears,'hat']
print(clothes)