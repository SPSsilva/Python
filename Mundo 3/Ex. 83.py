parent = list()
fparent = 0
expre = str(input('Digite sua expressão: '))
for t in expre:
    if t == '(':
        parent.append('(')
    elif t == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break
if len(parent) == 0:
    print('Sua expressão está certa! ')
else:
    print('Sua expressão está errada! ')
