def prec(c):
    if c == '^':
        return 3
    elif c=="/" or c=='*':
        return 2
    elif c=='+' or c=='-':
        return 1
    else:
        return -1
def postfix(s):
    st = []
    result = ""
    for i in range(len(s)):
        c = s[i]
        if (c >='a' and c<='z') or (c>='A' and c<='Z') or (c>='0' and c<='8'):
            result += c
        elif c =='(':
            st.append(c)
        elif c==')':
            while st[-1] != '(':
                result += st.pop()
            st.pop()
        else:
            while st and (prec(c) < prec(st[-1]) or prec(c)==prec(st[-1])):
                result += st.pop()
            st.append(c)
    while st:
        result += st.pop()
    print(result)
x = "a+b*(x-s)"
postfix(x)