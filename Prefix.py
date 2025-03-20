def prefix(data):
    s = []
    operators = set(['+', '-', '*', '/', '%'])
    data = list(data)[::-1]
    for i in data:
        if i in operators:
            a1 = s.pop()
            a2 = s.pop()
            result = eval(f'{a1}{i}{a2}')
            s.append(result)
        else:
            s.append(i)
    print(s)

x = "+*123"
prefix(x)
