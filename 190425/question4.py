tokens = ['<greeting>','Hello World!','</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count = count + 1
    
print(count)

#output -> 2
